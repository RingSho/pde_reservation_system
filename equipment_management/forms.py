from django import forms
from .models import Band, Schedule
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'

class BandCreateForm(forms.ModelForm):

  class Meta:
    model = Band
    fields = ('band_name', 'responsible_person_name')


class ScheduleCreateForm(forms.ModelForm):

  class Meta:
    model = Schedule
    fields = '__all__'
    widgets = {
        'active_date': DateInput(),
    }

  def clean(self):
    start_at = self.cleaned_data['start_at']
    end_at = self.cleaned_data['end_at']
    active_date = self.cleaned_data['active_date']
    schedules = Schedule.objects.filter(active_date=active_date)

    for schedule in schedules:
      if not ((start_at >= schedule.end_at) or (end_at <= schedule.start_at)):
        raise forms.ValidationError(
          '指定された時刻には既に予約が入っています'
          )

    if end_at <= start_at:
      raise forms.ValidationError(
        '終了時間は、開始時間よりも後にしてください'
        )
  
    if active_date < datetime.date.today():
      raise forms.ValidationError(
        '今日より前の日付に予約はできません'
        )


    return self.cleaned_data

  # def clean_end_at(self):
  #   start_at = self.cleaned_data['start_at']
  #   end_at = self.cleaned_data['end_at']

  #   if end_at <= start_at:
  #     raise forms.ValidationError(
  #       '終了時間は、開始時間よりも後にしてください'
  #       )
  #   return end_at

  # def clean_active_date(self):
  #   active_date = self.cleaned_data['active_date']
  #   print(active_date, datetime.date.today())
  #   if active_date < datetime.date.today():
  #     raise forms.ValidationError(
  #       '今日より前の日付に予約はできません'
  #       )
  #   return active_date


