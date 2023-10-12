from django.urls import path
from . import views

urlpatterns = [
    path("", views.ArticleAPIViewV1.as_view()),
]


