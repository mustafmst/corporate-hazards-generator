from django.db import models

# Create your models here.


class HazardPart(models.Model):
    part_text = models.CharField(max_length=250)
    HAZARD_PARTS = ['1', '2', '3', '4']
    hazard_part = models.CharField(max_length=1, choices=HAZARD_PARTS, default='1')
