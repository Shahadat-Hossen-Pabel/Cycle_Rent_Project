from django.shortcuts import render
from .models import Slider,Service,Motivation
# Create your views here.

def home_view(request):
	slider_components = Slider.objects.filter(active=True)
	service_section = Service.objects.all()[:1]
	motivation_section = Motivation.objects.all()

	context = {
		'slider': slider_components,
		'services':service_section,
		'motivations':motivation_section,

	}
	return render(request,'home.html',context)



def property_view(request):
	return render(request,'property.html')