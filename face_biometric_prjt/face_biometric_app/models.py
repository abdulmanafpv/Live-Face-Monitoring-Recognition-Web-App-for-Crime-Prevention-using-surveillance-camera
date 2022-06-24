
from django.db import models
from datetime import datetime
import os
import base64

# Create your models here.

sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female'),
	('Other', 'Other')
)

class Employee(models.Model):
	id = models.IntegerField(primary_key=True, max_length=10)

	name = models.CharField(max_length=50)

	gender = models.CharField(max_length=50, choices=sex_choice,blank=True,null=True)

	# photo = models.ImageField(upload_to='test_app/facerec/detected/', blank=True, null=True)
	photo = models.ImageField(upload_to='face_biometric_app/pictures/', blank=True, null=True)


	# contact_number = models.CharField(max_length=50)
	# date_of_birth = models.CharField(max_length=50)
	# date_of_joining = models.CharField(max_length=50)
	# department = models.CharField(max_length=50)
	# designation = models.CharField(max_length=50)
	# team = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	def num_photos(self):
		try:
			DIR = f"test_app/facerec/dataset/{self.name}_{self.id}"
			img_count = len(os.listdir(DIR))
			return img_count
		except:
			return 0

class Proof(models.Model):
	image=models.ImageField(upload_to='face_biometric_app/proof', blank=True, null=True)
	date_time=models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Detected(models.Model):
	emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
	time_stamp = models.DateTimeField()
	photo = models.ImageField(upload_to='test_app/facerec/detected', default='test_app/facerec/detected/noimg.png')

	# def __str__(self):
	# 	return self.emp_id
	def __str__(self):
		emp = Employee.objects.get(name=self.emp_id)
		return f"{emp.name} {self.time_stamp} {self.photo}"



class unreg(models.Model):
	# photo = models.ImageField(upload_to='media/face_biometric_app/pictures',blank=True, null=True)
	photo = models.ImageField(upload_to='face_biometric_app/image',blank=True, null=True)
	date_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)


class Checking(models.Model):
	image=models.ImageField(upload_to='face_biometric_app/check', blank=True, null=True)
	date_time=models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Checking_One(models.Model):
	image=models.ImageField(upload_to='face_biometric_app/one', blank=True, null=True)
	date_time=models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Checking_Two(models.Model):
	image=models.ImageField(upload_to='face_biometric_app/two', blank=True, null=True)
	date_time=models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Checking_Three(models.Model):
	image=models.ImageField(upload_to='face_biometric_app/three', blank=True, null=True)
	date_time=models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Checking_Four(models.Model):
	image=models.ImageField(upload_to='face_biometric_app/four', blank=True, null=True)
	date_time=models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Checking_Five(models.Model):
	image=models.ImageField(upload_to='face_biometric_app/five', blank=True, null=True)
	date_time=models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Upload_image(models.Model):
	image=models.ImageField(upload_to='face_biometric_app/upload', blank=True, null=True)
	date_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

