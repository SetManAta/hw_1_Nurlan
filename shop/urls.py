from django.urls import path, include

from . import views

urlpatterns = [
    path('greetings/', views.index, name='index'),
]
