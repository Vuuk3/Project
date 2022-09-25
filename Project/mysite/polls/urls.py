from django.urls import path

from . import views


urlpatterns = [
    path('', views.str1, name='str1'),
    ]