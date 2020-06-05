from django.shortcuts import render
from .models import Header,CeoBanner,Team



def about_view(request):
	header_text = Header.objects.filter(active=True)[:1]
	banner = CeoBanner.objects.filter(active=True)[:1]
	team = Team.objects.filter(active=True)[:4]

	context = {
		'header_text':header_text,
		'banner':banner,
		'team':team,
	}
	return render(request,'about.html',context)
