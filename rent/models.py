from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


class Header(models.Model):
	title = models.CharField(max_length=120)
	text = models.CharField(max_length=12)

	def __str__(self):
		return self.title



def image_upload_to_bike(instance,filename):
	title = instance.name
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_file_name = "%s-%s.%s" %(slug,instance.id,file_extension)
	return "bike/%s/image/%s" %(slug,new_file_name)

class Bike(models.Model):
	name = models.CharField(max_length=20)
	price = models.IntegerField()
	slug = models.SlugField(unique=True)
	rent_title = models.CharField(max_length=12)
	speed = models.CharField(max_length=12)
	speed_limit = models.CharField(max_length=12,blank=True,null=True)
	brand = models.CharField(max_length=20)
	brand_name = models.CharField(max_length=20,blank=True,null=True)
	model = models.CharField(max_length=20)
	model_name = models.CharField(max_length=20,blank=True,null=True)
	bike_image = models.ImageField(upload_to=image_upload_to_bike)
	categories = models.ManyToManyField('BikeCategory',blank=True)
	default = models.ForeignKey('BikeCategory',related_name='default_category',null=True,blank=True, on_delete=models.CASCADE)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	def get_cart_url(self):
		return reverse("rent:bike_detail", kwargs={
            'slug': self.slug
        })

	def get_add_bike_url(self):
		return reverse("rent:add_to_bike", kwargs={
            'slug': self.slug
        })


class BikeCategory(models.Model):
	title = models.CharField(max_length=120,unique=True)
	slug = models.SlugField(unique=True)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("rent:bike_category", kwargs={
            'slug': self.slug
        })


class SelectPoint(models.Model):
	select_point = models.CharField(max_length=120)

	def __str__(self):
		return self.select_point

	

class NotUse(models.Model):
	title = models.CharField(max_length=12)
	dont_use =  models.ForeignKey(SelectPoint, on_delete=models.CASCADE,blank=True,null=True)

	def __str__(self):
		return self.title

	def add_to_area(self):
		return reverse("rent:add_to_area", kwargs={
            'id': self.dont_use.id
        })



class PickupPoint(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	banner_image = models.ImageField()
	banner_title = models.CharField(max_length=120)
	banner_year_title = models.CharField(max_length=120)
	banner_creative_title = models.CharField(max_length=120)


class BookedArea(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	selectet_area = models.ForeignKey(SelectPoint, on_delete=models.CASCADE)

	def __str__(self):
		return self.selectet_area.select_point

class BookedBike(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	bike = models.ForeignKey(Bike, on_delete=models.CASCADE)

	def __str__(self):
		return self.bike.name

class FinalRent(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	email = models.EmailField(unique=True)
	number = models.CharField(max_length=120)
	start_date = models.DateField()
	start_time = models.TimeField()
	end_date = models.DateField()
	end_time = models.TimeField()

	def __str__(self):
		return self.user.username








