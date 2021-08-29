from django.urls import path
from . import views #importing views from views.py. when we hit this route run this function

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about')
]


