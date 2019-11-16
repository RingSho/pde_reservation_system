from django.shortcuts import render, redirect
from .models import Band, Schedule
from .forms import BandCreateForm, ScheduleCreateForm


def index(request):
  context ={
      'bands' : Band.objects.all(),
      'schedules' : Schedule.objects.all(),
  }
  return render(request, 'equipment_management/index.html', context)

def add_band(request):

  form = BandCreateForm(request.POST or None)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('equipment:index')

  context = {
    'form' : BandCreateForm()
  }
  return render(request, 'equipment_management/band_form.html', context)
