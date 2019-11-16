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
