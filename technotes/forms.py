from django.forms import ModelForm
from .models import Tech, TechCategory

class TechForm(ModelForm):
    class Meta:
        model = Tech
        fields = ["title", "description", "category"]


class TechCategoryForm(ModelForm):
    class Meta:
        model = TechCategory
        fields = ['name']
        error_messages = {
            'name': {
                'unique': 'The value is already exit. Please use different one.'
            }
        }
