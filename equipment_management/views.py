from django.shortcuts import render, redirect, get_object_or_404
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

def add_schedule(request):
  form = ScheduleCreateForm(request.POST or None)
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('equipment:index')
  context = {
    'form' : ScheduleCreateForm()
  }
  return render(request, 'equipment_management/band_form.html', context)


def show_band_list(request):
  context ={
      'bands' : Band.objects.all(),
  }
  return render(request, 'equipment_management/band_list.html', context)


def update_schedule(request, pk):
  schedule = get_object_or_404(Schedule, pk=pk)

  form = ScheduleCreateForm(request.POST or None, instance=schedule)
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('equipment:index')

  context = {
      'form': form,
  }
  return render(request, 'equipment_management/band_form.html', context)


def delete_schedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        schedule.delete()
        return redirect('equipment:index')

    context = {
        'schedule': schedule,
    }
    return render(request, 'equipment_management/schedule_confirm_delete.html', context)