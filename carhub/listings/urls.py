from django.urls import path
from . import views

# IMPORTANT: This variable must be named exactly 'urlpatterns'
urlpatterns = [
    path('', views.index, name='index'),
]