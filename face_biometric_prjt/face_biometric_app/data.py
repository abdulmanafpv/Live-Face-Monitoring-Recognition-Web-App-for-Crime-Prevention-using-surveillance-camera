import sqlite3
import os
import cv2
import  sys
from PIL import Image
from face_biometric_app.models import  unreg,Checking, Checking_One, Checking_Two, Checking_Three, Checking_Four, Checking_Five
import glob
from face_biometric_app.models import Detected
import shutil
import os
import face_biometric_app.config as cfg
import cv2
import numpy as np
from face_biometric_app.my_face_recognition import f_main
import imutils
from face_biometric_app import f_Face_info
from importlib import reload

from .models import Employee
from face_biometric_app.my_face_recognition import f_storage as st
import traceback




path='face_biometric_app/image'
# path='image'




list=['']
def lst():
    for image in glob.iglob(f'{path}/*'):
        list.append(image)


def main():
    img=list[-1]
    obj1=unreg.objects.create(photo=img)
    #     print(obj1)
    obj1.save()





check_path= 'face_biometric_app/check'
chck_list=['']
def check_listing():
    for image in glob.iglob(f'{check_path}/*'):
        chck_list.append(image)

def check_main():
    photo=chck_list[-1]
    obj2= Checking.objects.create(image=photo)
    obj2.save()




check_one_path= 'face_biometric_app/one'
chck_one=['']

def check_one():
    for image in glob.iglob(f'{check_one_path}/*'):
        chck_one.append(image)


def check_main_one():
    photo=chck_one[-1]
    obj= Checking_One.objects.create(image=photo)
    obj.save()

check_two_path= 'face_biometric_app/two'
chck_two=['']

def check_two():
    for image in glob.iglob(f'{check_two_path}/*'):
        chck_two.append(image)

def check_main_two():
    photo=chck_two[-1]
    obj= Checking_Two.objects.create(image=photo)
    obj.save()

check_three_path= 'face_biometric_app/three'
chck_three=['']

def check_three():
    for image in glob.iglob(f'{check_three_path}/*'):
        chck_three.append(image)

def check_main_three():
    photo=chck_three[-1]
    obj= Checking_Three.objects.create(image=photo)
    obj.save()

check_four_path= 'face_biometric_app/four'
chck_four=['']
def check_four():
    for image in glob.iglob(f'{check_four_path}/*'):
        chck_four.append(image)

def check_main_four():
    photo=chck_four[-1]
    obj= Checking_Four.objects.create(image=photo)
    obj.save()

check_five_path= 'face_biometric_app/five'
chck_five=['']
def check_five():
    for image in glob.iglob(f'{check_five_path}/*'):
        chck_five.append(image)

def check_main_five():
    photo=chck_five[-1]
    obj= Checking_Five.objects.create(image=photo)
    obj.save()





def loading():
    list_images = os.listdir(cfg.path_images)
    return list_images
    # names,features = st.load_images_to_database()
    # return names,features


def load_images():
    list_images = os.listdir(cfg.path_images)
    # filto los archivos que no son imagenes
    list_images = [File for File in list_images if File.endswith(('.jpg','.jpeg','JPEG','.png'))]

    # inicalizo variables
    name = []
    Feats = []

    # ingesta de imagenes
    for file_name in list_images:
        im = cv2.imread(cfg.path_images+os.sep+file_name)

        # obtengo las caracteristicas del rostro
        box_face = f_main.rec_face.detect_face(im)
        feat = f_main.rec_face.get_features(im,box_face)
        if len(feat)!=1:
            '''
            esto significa que no hay rostros o hay mas de un rostro
            '''
            continue
        else:
            # inserto las nuevas caracteristicas en la base de datos
            new_name = file_name.split(".")[0]
            if new_name == "":
                continue
            name.append(new_name)
            if len(Feats)==0:
                Feats = np.frombuffer(feat[0], dtype=np.float64)
            else:
                Feats = np.vstack((Feats,np.frombuffer(feat[0], dtype=np.float64)))


def get_frame():
    ret, frame = cv2.VideoCapture(0).read()

    frame = imutils.resize(frame, width=720)

    # obtenego info del frame
    f_Face_info.get_face_info(frame)




def reload():
    from importlib import reload  # Python 3.4+
    from face_biometric_app import f_Face_info


    f_Face_info = reload(f_Face_info)
    return f_Face_info

def img():
    detected = Detected.objects.all()
    det= detected.emp_id.order_by('-id')
    return det