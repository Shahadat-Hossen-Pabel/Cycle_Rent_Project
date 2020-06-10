from django.shortcuts import render
from .models import Slider,Service,Motivation
from rent.models import Bike

def home_view(request):
	slider_components = Slider.objects.filter(active=True)
	service_section = Service.objects.all()[:1]
	motivation_section = Motivation.objects.all()

	latest_bike = Bike.objects.all()[:4]

	context = {
		'slider': slider_components,
		'services':service_section,
		'motivations':motivation_section,
		'latest_bike':latest_bike

	}
	return render(request,'home.html',context)
