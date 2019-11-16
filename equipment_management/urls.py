from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add_band/', views.add_band, name='add_band'),
]
