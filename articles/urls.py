from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_template_with_articles),
    path("articles/pk", views.main_template_with_articles),
]


