from django.urls import path
from . import views

app_name = 'equipment'

urlpatterns = [
  path('', views.index, name='index'),
  path('add_band/', views.add_band, name='add_band'),
  path('add_schedule/', views.add_schedule, name='add_schedule'),
  path('show_band_list', views.show_band_list, name='show_band_list'),
  path('updete_schedule/<int:pk>/', views.update_schedule, name='update_schedule'),
  path('delete_schedule/<int:pk>/', views.delete_schedule, name='delete_schedule'),
]
