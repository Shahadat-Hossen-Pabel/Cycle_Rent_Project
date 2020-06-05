from django.db import models
from django.utils.text import slugify
# Create your models here.


class Header(models.Model):
	title = models.CharField(max_length=120)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.title


def image_upload_to_banner(instance,filename):
	title = instance.banner_title
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_file_name = "%s-%s.%s" %(slug,instance.id,file_extension)
	return "aboutBanner/%s/image/%s" %(slug,new_file_name)

def image_upload_to_founder(instance,filename):
	title = instance.founder_name
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_file_name = "%s-%s.%s" %(slug,instance.id,file_extension)
	return "founder/%s/image/%s" %(slug,new_file_name)


class CeoBanner(models.Model):
	banner_image = models.ImageField(upload_to=image_upload_to_banner)
	banner_title = models.CharField(max_length=120)
	banner_year_title = models.CharField(max_length=120)
	banner_creative_title = models.CharField(max_length=120)
	founder_image = models.ImageField(upload_to=image_upload_to_founder)
	extra_title = models.CharField(max_length=120,blank=True,null=True)
	founder_name = models.CharField(max_length=120)
	founder_title = models.CharField(max_length=120)
	desciption_one = models.TextField()
	desciption_two = models.TextField()
	active = models.BooleanField(default=True)


	def __str__(self):
		return self.founder_title


def image_upload_to_team(instance,filename):
	title = instance.person_name
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_file_name = "%s-%s.%s" %(slug,instance.id,file_extension)
	return "team/%s/image/%s" %(slug,new_file_name)



class Team(models.Model):
	person_image = models.ImageField(upload_to=image_upload_to_team)
	person_name = models.CharField(max_length=120)
	description = models.TextField()
	persom_number = models.CharField(max_length=120)
	person_email = models.EmailField()
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.person_name