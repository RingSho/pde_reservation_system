from django.urls import path
from . import views

app_name = 'equipment'

urlpatterns = [
  path('', views.index, name='index'),
  path('add_band/', views.add_band, name='add_band'),
  path('add_schedule/', views.add_schedule, name='add_schedule'),
]
