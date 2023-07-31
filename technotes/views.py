"""Module providingFunction render, get object and error if not found"""
import random
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, View

from .models import Tech,TechCategory
from .forms import TechForm,TechCategoryForm

# Create your views here.
def home_page (request):
    display_item = 5
    alltechcat = TechCategory.objects.all()
    alltechs = list(Tech.objects.all())
    if len(alltechs) >= 1:
        if len(alltechs) >= display_item:
            techs = random.sample(alltechs, 5)
        else:
            techs = alltechs
    else:
        techs=None
    tccount = len(alltechcat)
    return render(request, 'technotes/home.html', {
        "techs": techs,
        'tcount': tccount
        }
    )

def tech_summary_page (request):
    category = TechCategory.objects.all()
    context = {
        'category' : category,
        'count': len(category)
    }
    return render(request,"technotes/tech-summary.html", context)

def tech_filter_page (request, cat):
    items = Tech.objects.filter(category__name=cat)
    cat_id = TechCategory.objects.get(name=cat).id
    context = {
        'items' : items,
        'category' : cat,
        'count': items.count(),
        'cat_id': int(cat_id)
    }
    return render(request,"technotes/tech-filter.html", context)


def tech_details (request, slug):
    item = get_object_or_404(Tech, slug=slug)
    saved_list = request.session.get("review_lists")
    if saved_list is not None:
        to_save = item.id in saved_list
    else:
        to_save = False
    return render (request, "technotes/tech-details.html", {
        "item": item,
        "to_save": to_save
    })

def tech_form (request):
    if request.method == "POST":
        form = TechForm(request.POST)
        if form.is_valid():
            data = form
            data.save()
            return HttpResponseRedirect('tech/tech-summary/')
    else:
        form = TechForm()
    return render (request, 'technotes/form.html',{
        'form': form
    })

def tech_category_form(request):
    if request.method == 'POST':
        form = TechCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('tech/tech-summary/')
    else:
        form = TechCategoryForm()
    return render(request, 'technotes/form.html',{
        'form': form
    })

class TechUpdateView(UpdateView):  # pylint: disable=too-many-ancestors
    model = Tech
    fields = '__all__'
    template_name = 'technotes/update-form.html'
    def get_success_url(self):
        return f"/tech-detail/{self.object.slug}"
class TechCatUpdateView(UpdateView): # pylint: disable=too-many-ancestors
    model = TechCategory
    fields = '__all__'
    template_name = 'technotes/update-form.html'
    def get_success_url(self):
        item = TechCategory.objects.get(pk=self.kwargs['pk'])
        return f"/tech/{item.name}"

class ReviewListView(View):
    def get(self, request):
        review_lists = request.session.get("review_lists")
        context ={}
        if review_lists is None or len(review_lists) == 0:
            context['items'] = []
            context['is_review_list'] = False
        else:
            items = Tech.objects.filter(pk__in=review_lists)
            context['items'] = items
            context['is_review_list'] = True

        return render(request, 'technotes/review-list.html', context)

    def post(self, request):
        review_lists = request.session.get("review_lists")
        if review_lists is None:
            review_lists = []

        item_id = int(request.POST["review"])
        item = Tech.objects.get(pk=item_id)
        if item_id not in review_lists:
            review_lists.append(item_id)
        else:
            review_lists.remove(item_id)
        request.session["review_lists"]=review_lists
        return HttpResponseRedirect('tech-detail/'+item.slug)
