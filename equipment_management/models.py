from django.db import models
from django.utils import timezone


def two_hours_hence():
    return timezone.now() + timezone.timedelta(hours=2)

class Band(models.Model):
  band_name = models.CharField(max_length=255,
                               verbose_name="Band's Name",
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
  active_date = models.DateField(default=timezone.now)
  start_at = models.TimeField(default=timezone.now)
  end_at = models.TimeField(default=two_hours_hence)
  text = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return str(self.start_at) + ' -> ' + str(self.end_at)