from django.db import models
from django.utils.text import slugify


def image_upload_to_slider(instance,filename):
	title = instance.title
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_file_name = "%s-%s.%s" %(slug,instance.id,file_extension)
	return "slider/%s/image/%s" %(slug,new_file_name)


class Slider(models.Model):
	color_title = models.CharField(max_length=120)
	title = models.CharField(max_length=120)
	button_title = models.CharField(max_length=120)
	back_image = models.ImageField(upload_to=image_upload_to_slider)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.color_title


class Service(models.Model):
	first_title = models.CharField(max_length=120)
	first_description = models.TextField()
	second_title = models.CharField(max_length=120)
	second_description = models.TextField()
	third_title = models.CharField(max_length=120)
	third_description = models.TextField()

	def __str__(self):
		return self.first_title


def image_upload_to_speaker(instance,filename):
	title = instance.speaker_name
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_file_name = "%s-%s.%s" %(slug,instance.id,file_extension)
	return "speaker/%s/image/%s" %(slug,new_file_name)


def image_upload_to_main(instance,filename):
	title = instance.speaker_name
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_file_name = "%s-%s.%s" %(slug,instance.id,file_extension)
	return "main/%s/image/%s" %(slug,new_file_name)


class Motivation(models.Model):
	speaker_name = models.CharField(max_length=120)
	speaker_image = models.ImageField(upload_to=image_upload_to_speaker)
	description = models.TextField()
	main_image = models.ImageField(upload_to=image_upload_to_main)

	def __str__(self):
		return self.speaker_name






