from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
from face_biometric_app.camera import VideoCamera
from face_biometric_app.models import Employee, Detected, unreg, Checking, Checking_One, Checking_Two, Checking_Three, \
	Checking_Four, Checking_Five, Upload_image, Proof
from .forms import EmployeeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import datetime
from face_biometric_app.data import  load_images, get_frame,reload
from face_biometric_app.my_face_recognition import f_main
from face_biometric_app.data import loading
from django.db.models import Q
from face_biometric_app.image import img, delete
from face_biometric_app.f_Face_info import get_face_info
import traceback
import numpy as np
from face_biometric_app.my_face_recognition import f_storage as st
from face_biometric_app.my_face_recognition import f_main
import cv2
import os
from threading import Thread
from face_biometric_app import f_Face_info
import imutils
# Create your views here.


def index(request):
	date_formatted = datetime.datetime.today().date()
	date = request.GET.get('search_box', None)
	if date is not None:
		date_formatted = datetime.datetime.strptime(date, "%Y-%m-%d-%s").date()
	det_list = Detected.objects.filter(time_stamp__date=date_formatted).order_by('time_stamp').reverse()
	# print(det_list)

	# date_formatted = datetime.datetime.today().date()
	det_list = Detected.objects.filter(time_stamp__date=date_formatted).order_by('time_stamp').reverse()[:6]
	emp_list = Employee.objects.all()
	if request.method == "POST":
		form = EmployeeForm(request.POST, request.FILES)
		if form.is_valid():
			emp = form.save()
			print(emp)
			return HttpResponseRedirect(reverse('registerd_people'))
	else:
		form = EmployeeForm()
	return render(request,'index.html',{'det_list':det_list,'date': date_formatted,'emp_list': emp_list,'form':form})


def refresh(request):
    return HttpResponseRedirect(reverse('index'))

def search_result(request):
    result = None
    Query = None
    if 'q' in request.GET:
        Query = request.GET.get('q')
        result = Detected.objects.all().filter(Q(time_stamp__icontains=Query))

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            emp = form.save()
            print(emp)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = EmployeeForm()
    return render(request,'serch-result.html',{'result':result,'form':form})



def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')





def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')




def unregisterd(request):
	# result = unreg.objects.all().order_by('-id')[:3]
	result = unreg.objects.all().order_by('-id')
	return render(request,'unregisterd.html',{'result':result})


def search_result(request):
	result = None
	Query = None
	if 'q' in request.GET:
		Query = request.GET.get('q')
		result = Detected.objects.all().filter(Q(time_stamp__icontains=Query))

	if request.method == "POST":
		form = EmployeeForm(request.POST, request.FILES)
		if form.is_valid():
			emp = form.save()
			print(emp)
			return HttpResponseRedirect(reverse('index'))
	else:
		form = EmployeeForm()
	return render(request,'serch-result.html',{'result':result,'form':form})





def training(request):
	reload()
	# st.load_images_to_database()
	# get_frame()
	# load_images()
	return HttpResponseRedirect(reverse('index'))


def registerd_people(request):
	result = Employee.objects.all().order_by('-id')
	return render(request,'registerd_people.html', {'result':result})



def registered_people_edit(request,reg_id):
	obj = Employee.objects.filter(id=reg_id).first()
	if request.method == 'POST':
		form = EmployeeForm(request.POST,request.FILES,instance=obj)
		if form.is_valid():
			form.save()
			return redirect('registerd_people')
	else:
		obj = Employee.objects.filter(id=reg_id).first()
		form = EmployeeForm(instance=obj)
	return render(request,'edit.html',{'form':form})



def registered_people_delete(request,reg_id):
	obj = Employee.objects.filter(id=reg_id)
	obj.delete()
	return redirect('registerd_people')



def unknown_search(request):
	if request.method == 'POST':
		name = request.POST.get('q')
		result = unreg.objects.filter(date_time__icontains=name)
		# print(result.count())
	return render(request,'unknown-search.html',{'result':result})

checking_people=['']
def checking_individual(request):
	if request.method == 'POST':
		obj = request.POST.get('q')
		checking_people.append(obj)
		print(obj)
		print(checking_people[-1])
		# for i in checking_people:
		# 	print(i)

	return HttpResponseRedirect(reverse('index'))
	# return render(request, 'checking_people.html')

def check_list():
	name= checking_people[-1]
	# for i in checking_people:
	# 	return i

	return name


def uncheck(request):
	result = Checking.objects.all().order_by('-id')
	return render(request, 'checking_people.html', {'result': result})

one_lst=['']
def checking_one(request):
	if request.method == 'POST':
		obj = request.POST.get('q')
		one_lst.append(obj)
		print(obj)
		print(one_lst[-1])
		# for i in checking_people:
		# 	print(i)

	return HttpResponseRedirect(reverse('index'))

def check_one():
	name= one_lst[-1]
	# for i in checking_people:
	# 	return i

	return name

def uncheck_one(request):
	result = Checking_One.objects.all().order_by('-id')
	return render(request, 'one.html', {'result': result})

def one_search(request):
	if request.method == 'POST':
		name = request.POST.get('q')
		result = Checking_One.objects.filter(date_time__icontains=name)
		# print(result.count())
	return render(request,'one-search.html',{'result':result})




two_lst=['']
def checking_two(request):
	if request.method=='POST':
		obj=request.POST.get('q')
		two_lst.append(obj)
		print(obj)
		print(two_lst[-1])

	return HttpResponseRedirect(reverse('index'))


def check_two():
	name= two_lst[-1]
	# for i in checking_people:
	# 	return i

	return name

def uncheck_two(request):
	result = Checking_Two.objects.all().order_by('-id')
	return render(request, 'two.html', {'result': result})


def two_search(request):
	if request.method == 'POST':
		name = request.POST.get('q')
		result = Checking_Two.objects.filter(date_time__icontains=name)
		# print(result.count())
	return render(request,'two-search.html',{'result':result})




three_lst=['']
def checking_three(request):
	if request.method=='POST':
		obj=request.POST.get('q')
		three_lst.append(obj)
		print(obj)
		print(three_lst[-1])
	return HttpResponseRedirect(reverse('index'))


def check_three():
	name= three_lst[-1]
	# for i in checking_people:
	# 	return i

	return name

def uncheck_three(request):
	result = Checking_Three.objects.all().order_by('-id')
	return render(request, 'three.html', {'result': result})

def three_search(request):
	if request.method == 'POST':
		name = request.POST.get('q')
		result = Checking_Three.objects.filter(date_time__icontains=name)
		# print(result.count())
	return render(request,'three-search.html',{'result':result})



four_lst=['']
def checking_four(request):
	if request.method=='POST':
		obj=request.POST.get('q')
		four_lst.append(obj)
		# print(obj)
		# print(four_lst[-1])
	return HttpResponseRedirect(reverse('index'))

def check_four():
	name= four_lst[-1]
	# for i in checking_people:
	# 	return i

	return name

def uncheck_four(request):
	result = Checking_Four.objects.all().order_by('-id')
	return render(request, 'four.html', {'result': result})

def four_search(request):
	if request.method == 'POST':
		name = request.POST.get('q')
		result = Checking_Four.objects.filter(date_time__icontains=name)
		# print(result.count())
	return render(request,'four-search.html',{'result':result})




five_lst=['']
def checking_five(request):
	if request.method=='POST':
		obj=request.POST.get('q')
		five_lst.append(obj)
		# print(obj)
		# print(five_lst[-1])
	return HttpResponseRedirect(reverse('index'))


def check_five():
	name= five_lst[-1]
	return name

def uncheck_five(request):
	res = Checking_Five.objects.all().order_by('-id')
	return render(request, 'five.html', {'result': res})

def five_search(request):
	if request.method == 'POST':
		name = request.POST.get('q')
		results = Checking_Five.objects.filter(date_time__icontains=name)
		# print(result.count())
	return render(request,'five-search.html',{'result':results})

def check_search(request):
	return render(request, 'check.html')

ip_lst=[0]

def ip_cam(request):
	if request.method == 'POST':
		ip = request.POST.get('ip')
		ip_lst.append('rtsp://'+ip)
		# ip_lst.append(ip)
		print(ip)
		return redirect('index')
	else:
		return HttpResponse('Error')


def ip_check():
	name_ip = ip_lst[-1]
	return name_ip

def images_upload(request):
	img=None
	if request.method == "POST":
		print(request.POST)
		img = Upload_image.objects.create(image=request.FILES.get('img'))
		img.save()
	return render(request, 'upload.html',{'img':img})


def finding(request):
	fnd = img()
	print(fnd)
	result = Employee.objects.filter(name=fnd)
	return render(request, 'upload.html',{'img':fnd,'result':result})


def cancel(request):
	cncl=delete()
	return render(request, 'upload.html', {'cncl': cncl})


def proofing(request):

	result = Proof.objects.all().order_by('-id')
	return render(request,'proof.html',{'result':result})


def proof_search(request):
	if request.method == 'POST':
		name = request.POST.get('q')
		result = Proof.objects.filter(date_time__icontains=name).order_by('-id')
	# print(result.count())
	return render(request, 'proof-search.html', {'result': result})











