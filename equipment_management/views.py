from django.shortcuts import render, redirect, get_object_or_404
from .models import Band, Schedule
from .forms import BandCreateForm, ScheduleCreateForm
from . import mixins
from django.views import generic
import datetime


def add_band(request):
  form = BandCreateForm(request.POST or None)
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('equipment:show_band_list')
  context = {
    'form' : BandCreateForm(),
    'title' : 'バンド登録',
  }
  return render(request, 'equipment_management/band_form.html', context)

def add_schedule(request):
  form = ScheduleCreateForm(request.POST or None)
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('equipment:month')
  context = {
    'form' : ScheduleCreateForm(),
    'title' : '機材予約',
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
    return redirect('equipment:month')

  context = {
      'form': form,
  }
  return render(request, 'equipment_management/band_form.html', context)


def delete_schedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        schedule.delete()
        return redirect('equipment:month')

    context = {
        'schedule': schedule,
    }
    return render(request, 'equipment_management/schedule_confirm_delete.html', context)

def delete_band(request, pk):
    band = get_object_or_404(Band, pk=pk)
    if request.method == 'POST':
        band.delete()
        return redirect('equipment:show_band_list')

    context = {
        'band': band,
    }
    return render(request, 'equipment_management/band_confirm_delete.html', context)

def schedule_by_band(request, pk):
  band_name = Band.objects.get(pk=pk)

  context ={
      'band_name' : band_name,
      'schedules' : Schedule.objects.filter(band_id=band_name),
  }
  return render(request, 'equipment_management/schedule_by_band.html', context)

def day_schedule(request, year, month, day):
  target_date = datetime.date(year, month, day)
  context ={
      'schedules' : Schedule.objects.filter(active_date=target_date).order_by('-active_date'),
      'target_date' : target_date,
  }
  return render(request, 'equipment_management/day_schedule.html', context)

class MonthCalendar(mixins.MonthCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'equipment_management/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        today_date = datetime.date.today()
        context['schedules'] = Schedule.objects.filter(active_date=today_date).order_by('-active_date')
        context['today'] = today_date
        return context