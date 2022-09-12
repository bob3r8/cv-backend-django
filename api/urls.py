from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.index, name='index')
]
