from django.urls import path
from . import views

app_name = 'equipment'

urlpatterns = [
  path('month/', views.MonthCalendar.as_view(), name='month'),
  path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),
  path('add_band/', views.add_band, name='add_band'),
  path('add_schedule/', views.add_schedule, name='add_schedule'),
  path('show_band_list', views.show_band_list, name='show_band_list'),
  path('updete_schedule/<int:pk>/', views.update_schedule, name='update_schedule'),
  path('delete_schedule/<int:pk>/', views.delete_schedule, name='delete_schedule'),
  path('delete_band/<int:pk>/', views.delete_band, name='delete_band'),
  path('schedule_by_band/<int:pk>', views.schedule_by_band, name='schedule_by_band'),
  path('day_schedule/<int:year>/<int:month>/<int:day>', views.day_schedule, name='day_schedule'),
]
