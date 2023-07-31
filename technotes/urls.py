from django.urls import path
from . import views
urlpatterns =[
    path("", views.home_page, name="home-page"),
    path("tech/tech-summary/", views.tech_summary_page, name="tech-sum"),
    path("tech/<str:cat>", views.tech_filter_page, name="tech-filter"),
    path("tech-detail/<slug:slug>", views.tech_details, name = "tech-detail"),
    path("tech-form", views.tech_form, name = "tech-form"),
    path("tech-cat-form", views.tech_category_form, name = "tech-cat-form"),
    path("tech/update/<slug:slug>", views.TechUpdateView.as_view(), name = "tech-update"),
    path("techcat/update/<int:pk>", views.TechCatUpdateView.as_view(), name = "cat-update"),
    path("review-list",views.ReviewListView.as_view(), name = 'review-list')
]
