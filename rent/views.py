from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Bike,Header,BikeCategory,DestinitionSelect
from django.views.generic import ListView,DetailView


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
	queryset = Bike.objects.all()

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(*args,**kwargs)
		context["destinition"] = DestinitionSelect.objects.filter(active=True)
		return context



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


	