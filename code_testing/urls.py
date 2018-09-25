from django.urls import path

from . import views

app_name = 'code_testing'
urlpatterns = [
    path('', views.index, name='index'),
]