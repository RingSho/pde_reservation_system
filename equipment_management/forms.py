from django import forms
from .models import Band, Schedule


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

  def clean_end_at(self):
    start_at = self.cleaned_data['start_at']
    end_at = self.cleaned_data['end_at']
    if end_at <= start_at:
      raise forms.ValidationError(
        '終了時間は、開始時間よりも後にしてください'
        )
    return end_at

  
