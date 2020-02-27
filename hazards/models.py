from django.db import models

# Create your models here.


class HazardPart(models.Model):
    part_text = models.CharField(max_length=250)
    HAZARD_PARTS = [('1', 'PART I'), ('2', 'PART II'), ('3', 'PART III'), ('4', 'PART IV')]
    hazard_part = models.CharField(max_length=1, choices=HAZARD_PARTS, default='1')

    def __str__(self):
        return f'{self.hazard_part} | {self.part_text}'
