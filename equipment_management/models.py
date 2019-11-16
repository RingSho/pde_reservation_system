from django.db import models
from django.utils import timezone

class Band(models.Model):
  band_name = models.CharField(max_length=255, verbose_name='バンド名')
  responsible_person_name = models.CharField(max_length=255, verbose_name='責任者名')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.band_name

class Schedule(models.Model):
  band_id = models.ForeignKey(Band, on_delete=models.CASCADE)
  pa_name = models.CharField(max_length=255, verbose_name='PA担当者名')
  start_at = models.DateTimeField(default=timezone.now)
  end_at = models.DateTimeField(default=timezone.now)
  text = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return str(self.start_at) + ' -> ' + str(self.end_at)