from django.shortcuts import render
from .models import Band, Schedule

def index(request):
  context ={
      'bands' : Band.objects.all(),
      'schedules' : Schedule.objects.all(),
  }
  return render(request, 'equipment_management/index.html', context)