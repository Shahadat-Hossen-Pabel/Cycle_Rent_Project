from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Bike,Header,BikeCategory,PickupPoint,SelectPoint,BookedArea,NotUse
from django.views.generic import ListView,DetailView
from django.views.generic.base import View
from django.views.generic.edit import FormMixin


"""def pickup_view(request):
	return render(request,'pickup.html')"""

"""class PickUpDetailView(DetailView):
	model = SelectPoint
	template_name = "rent/pickup.html"""


@login_required
def pickup_view(request):
	pickpoint = PickupPoint.objects.get(user=request.user)
	select_pickup = SelectPoint.objects.all()
	not_use = NotUse.objects.all()[:1]


	context = {
		'object': pickpoint,
		'objects': select_pickup,
		'not_use': not_use

	}
	return render(request,'rent/pickup.html',context)


def add_to_area(request,id):
	#get the area.
	get_selected_area = get_object_or_404(SelectPoint,id=id)
	#create the area into BookedArea
	create_area = BookedArea.objects.create(
		user=request.user,
		selectet_area=get_selected_area
	)
	return redirect("rent:bike_list")


class BikeListView(ListView):
	model = Bike
	queryset = Bike.objects.all()
	paginate_by = 12

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(*args,**kwargs)
		context["header"] = Header.objects.all()[:1]
		context["category"] = BikeCategory.objects.filter(active=True)
		context["query"] = self.request.GET.get("q")
		return context

	def get_queryset(self, *args, **kwargs):
		qs = super().get_queryset(*args,**kwargs)
		query = self.request.GET.get("q")
		if query:
			qs = self.model.objects.filter(
					Q(name__icontains=query) |
					Q(model_name__icontains=query)
				)
			try:
				qs2 = self.model.objects.filter(Q(brand_name=query))
				qs = (qs | qs2).distinct()
			except:
				pass
		return qs



class BikeDetailView(DetailView):
	model = Bike
	
	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(*args,**kwargs)
		context["booked"] = BookedArea.objects.all()
		return context


def message_view(request):

	return render(request,'messages.html')





class CategoryDetailView(DetailView):
	model = BikeCategory
	queryset = BikeCategory.objects.all()
	paginate_by = 3

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		obj = self.get_object()
		bike_set = obj.bike_set.all()
		print(bike_set)
		default_bikes = obj.default_category.all()
		print(default_bikes)
		bikes = ( bike_set | default_bikes ).distinct()
		context["bikes"] = bikes
		context["category"] = BikeCategory.objects.all()
		return context


	