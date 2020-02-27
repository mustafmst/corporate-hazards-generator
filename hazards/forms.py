from django import forms
from hazards.models import HazardPart


class HazardPartForm(forms.Form):
    part_text = forms.CharField(label="Tekst części:", max_length=250)
    hazard_part = forms.ChoiceField(choices=HazardPart.HAZARD_PARTS)
