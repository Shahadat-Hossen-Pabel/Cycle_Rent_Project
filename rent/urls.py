from django.urls import path
from .views import BikeListView,CategoryDetailView,BikeDetailView

app_name = 'rent'

urlpatterns = [
	path('', BikeListView.as_view(), name='bike_list'),
	path('Go_to/<slug>/', BikeDetailView.as_view(), name='bike_detail'),
	path('<slug>/', CategoryDetailView.as_view(), name='bike_category'),
]