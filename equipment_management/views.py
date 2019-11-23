from django.shortcuts import render, redirect, get_object_or_404
from .models import Band, Schedule
from .forms import BandCreateForm, ScheduleCreateForm
from . import mixins
from django.views import generic
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator


@login_required
def add_band(request):
  form = BandCreateForm(request.POST or None)
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('equipment:show_band_list')
  context = {
    'form' : BandCreateForm(),
    'title' : 'バンド登録',
  }
  if request.method == 'POST' and not form.is_valid():
    context['error_message'] = "※ 既に登録されたバンド名が入力されています。"
  return render(request, 'equipment_management/band_form.html', context)

@login_required
def add_schedule(request):
  form = ScheduleCreateForm(request.POST or None)
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('equipment:month')
  context = {
    'form' : ScheduleCreateForm(),
    'title' : '機材予約',
  }
  if not form.is_valid():
    for error in form.errors.values():
      context['error_message'] = error
  return render(request, 'equipment_management/band_form.html', context)

@login_required
def show_band_list(request):
  context ={
      'bands' : Band.objects.all(),
  }
  return render(request, 'equipment_management/band_list.html', context)

@login_required
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

@login_required
def delete_schedule(request, pk):
  schedule = get_object_or_404(Schedule, pk=pk)
  if request.method == 'POST':
    schedule.delete()
    return redirect('equipment:month')

  context = {
    'schedule': schedule,
  }
  return render(request, 'equipment_management/schedule_confirm_delete.html', context)

@login_required
def delete_band(request, pk):
  band = get_object_or_404(Band, pk=pk)
  if request.method == 'POST':
      band.delete()
      return redirect('equipment:show_band_list')

  context = {
      'band': band,
  }
  return render(request, 'equipment_management/band_confirm_delete.html', context)

@login_required
def schedule_by_band(request, pk):
  band_name = Band.objects.get(pk=pk)

  context ={
      'band_name' : band_name,
      'schedules' : Schedule.objects.filter(band_id=band_name).order_by('-active_date'),
  }
  return render(request, 'equipment_management/schedule_by_band.html', context)

@login_required
def day_schedule(request, year, month, day):
  target_date = datetime.date(year, month, day)
  context ={
      'schedules' : Schedule.objects.filter(active_date=target_date).order_by('-active_date'),
      'target_date' : target_date,
  }
  return render(request, 'equipment_management/day_schedule.html', context)

@method_decorator(login_required, name='dispatch')
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