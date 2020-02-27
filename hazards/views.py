from django.http import HttpResponse
from django.shortcuts import render
from random import choice

# Create your views here.
from django.views.decorators.http import require_GET, require_http_methods

from hazards.forms import HazardPartForm
from hazards.models import HazardPart


@require_GET
def get_random_hazard(request):
    part1 = HazardPart.objects.filter(hazard_part='1')
    part2 = HazardPart.objects.filter(hazard_part='2')
    part3 = HazardPart.objects.filter(hazard_part='3')
    part4 = HazardPart.objects.filter(hazard_part='4')
    hazard = f'{choice(part1).part_text} {choice(part2).part_text} {choice(part3).part_text} {choice(part4).part_text}'
    return render(request, 'hazards/index.html', {'hazard': hazard})


@require_http_methods(["GET", "POST"])
def hazard_part(request):
    if request.method == 'POST':
        post_form = HazardPartForm(request.POST)
        if post_form.is_valid():
            data = post_form.data
            HazardPart(part_text=data.get('part_text'), hazard_part=data.get('hazard_part')).save()
    form = HazardPartForm()
    return render(request, 'hazards/part_form.html', {'form': form})
