from django.urls import path
from .views import (
	BikeListView,
	CategoryDetailView,
	BikeDetailView,
	pickup_view,
	add_to_area,
	message_view
	)

app_name = 'rent'

urlpatterns = [
	path('add_to_area/<id>/', add_to_area, name='add_to_area'),
	path('bike_list/', BikeListView.as_view(), name='bike_list'),
	path('', pickup_view, name='picup_point'),
	path('message/', message_view, name='message'),
	path('Go_to/<slug>/', BikeDetailView.as_view(), name='bike_detail'),
	path('<slug>/', CategoryDetailView.as_view(), name='bike_category'),
]