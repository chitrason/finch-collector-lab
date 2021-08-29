from django.urls import path
from . import views #importing views from views.py. when we hit this route run this function

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finches_index, name='finches_index'),
  path('finches/<int:finch_id>/', views.finches_detail, name='finches_detail')
]


