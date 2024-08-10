from django.urls import path

from . import views

urlpatterns = [
    path("testpaper", views.testpaper),
    path("result/", views.result),
]
