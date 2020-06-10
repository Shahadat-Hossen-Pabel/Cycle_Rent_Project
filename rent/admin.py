from django.contrib import admin
from .models import Header,Bike,BikeCategory,PickupPoint,SelectPoint,BookedArea,NotUse,FinalRent,BookedBike


admin.site.register(Header)
admin.site.register(Bike)
admin.site.register(BikeCategory)
admin.site.register(PickupPoint)

admin.site.register(SelectPoint)
admin.site.register(BookedArea)
admin.site.register(NotUse)
admin.site.register(FinalRent)
admin.site.register(BookedBike)


