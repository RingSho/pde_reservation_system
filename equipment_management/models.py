from django.db import models
from django.utils import timezone
import datetime


def nine_hours_hence():
    return timezone.now() + timezone.timedelta(hours=9)

def two_hours_hence():
    return timezone.now() + timezone.timedelta(hours=11)

class Band(models.Model): 
  band_name = models.CharField(max_length=255,
                               verbose_name="Band's Name",
                               unique=True,
                               )
  responsible_person_name = models.CharField(max_length=255,
                                             verbose_name="Band Master's Name")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.band_name


class Schedule(models.Model):
  band_id = models.ForeignKey(Band, on_delete=models.CASCADE)
  pa_name = models.CharField(max_length=255, verbose_name='PA担当者名')
  active_date = models.DateField(default=timezone.now, verbose_name='予約日')
  start_at = models.TimeField(default= nine_hours_hence(), verbose_name='開始時間')
  end_at = models.TimeField(default=two_hours_hence, verbose_name='終了時間')
  text = models.TextField(blank=True, verbose_name='備考欄')
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.band_id.band_name + ': ' +  str(self.active_date) + ' ' + str(self.start_at) + ' - ' + str(self.end_at)

  def is_avaiable(self):
    today = datetime.date.today()
    current_time = datetime.datetime.now().time()
    if today < self.active_date:
      return True
    elif (today == self.active_date) and (current_time < self.start_at):
      return True
    else:
      return False
