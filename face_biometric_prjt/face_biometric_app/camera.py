import cv2
import time
import imutils
import os
from face_biometric_app import f_Face_info
from cachetools import TTLCache
import pyautogui
import datetime, time
from face_biometric_app .f_Face_info import det
from face_biometric_app .f_Face_info import name
from .models import Employee, Detected
from .forms import EmployeeForm
from .models import unreg

import numpy as np
from face_biometric_app .data import main
from face_biometric_app .data import img
from face_biometric_app .data import lst,check_listing,check_main,check_one,check_main_one
from face_biometric_app .data import check_two, check_main_two, check_three, check_main_three, check_four, check_main_four
from face_biometric_app .data import check_five, check_main_five
from face_biometric_app import views
import face_recognition
from django.conf import settings
cache = TTLCache(maxsize=20, ttl=60)


from face_biometric_app .models import Employee, Detected
from cachetools import TTLCache
import datetime, time
from face_biometric_app .my_face_recognition import f_main
rec_face = f_main.rec()



def identify1(frame, name):

    # timestamp = datetime.datetime.now(tz=timezone.utc)
    timestamp = datetime.datetime.today()
    # timestamp = datetime.datetime.second

    print(name, timestamp)
    # cache[name] = 'detected'
    path = 'detected/{}_{}.jpg'.format(name, timestamp)
    # write_path = 'media/' + path
    cv2.imwrite(path, frame)
    try:
        emp = Employee.objects.get(name=name)
        emp.detected_set.create(time_stamp=timestamp, photo=path)
    except:
        pass


def unknown(out):
    if name(out) == 'unknown':
        release=cv2.VideoCapture(0).release()
        return release





global buf_length, known_conf ,i
buf_length = 10
known_conf = 6
i = 0









class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(views.ip_check())
        # self.video = cv2.VideoCapture(0)

        # self.video = cv2.VideoCapture('192.168.1.2')

        # self.video = cv2.VideoCapture('rtsp://admin:RWHOJO@192.168.1.18:h264_stream')

        self.buf = [[]] * buf_length
        # self.buf = [] * buf_length
        self.i = 0
        self.buf_length = 10
        self.known_conf = 6
        # self.resolution = (640, 480)
        self.resolution = (240, 320)
        self.fps = 5
        self.codec = cv2.VideoWriter_fourcc(*"XVID")
        # self.codec = cv2.VideoWriter_fourcc(*'MP4V')

        self.now= datetime.datetime.now()
        self.rec= 'vid_{}.avi'.format(str(self.now).replace(":",''))
        # self.rec= 'vid_{}.mp4'.format(str(self.now).replace(":",''))

        self.filename = os.path.sep.join(['face_biometric_app/video',self.rec])
        self.filename_one = os.path.sep.join(['media/face_biometric_app/video',self.rec])

        self.out= cv2.VideoWriter(self.filename, self.codec, self.fps, self.resolution)
        self.out_one= cv2.VideoWriter(self.filename_one, self.codec, self.fps, self.resolution)


    def __del__(self):
        self.video.release()





    def get_frame(self):
        star_time = time.time()
        ret, frame = self.video.read()
        self.out.write(frame)
        self.out_one.write(frame)






        face_names = []

        frame = imutils.resize(frame, width=720)
        # frame = imutils.resize(frame, width=640)




        # obtenego info del frame
        out = f_Face_info.get_face_info(frame)


        # pintar imagen
        frame  = f_Face_info.bounding_box(out, frame)

        end_time = time.time() - star_time
        FPS = 1 / end_time
        # cv2.putText(frame , f"FPS: {round(FPS, 3)}", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame , f"FPS: {round(FPS, 3)}", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 255), 1)

        # cv2.putText(frame)

        # print(name(out))

        # identify1(frame,name(out),self.buf,self.buf_length,self.known_conf)
        identify1(frame,name(out))

        if name(out) == "unknow":
            # self.video.release()
            now = datetime.datetime.today()
            pht="detected{}.jpg".format(str(now).replace(":", ''))
            # p=os.path.sep.join(['face_biometric_app/image', "detected{}.jpg".format(str(now).replace(":", ''))])
            # p=os.path.sep.join(['face_biometric_app/image', pht])
            p1= os.path.sep.join(['face_biometric_app/image',pht])
            p2= os.path.sep.join(['media/face_biometric_app/image',pht])

            # p=os.path.sep.join(['face_biometric_app/image', "detected.png".replace(":", '')])

            # cv2.imwrite(saving(), frame)
            cv2.imwrite(p1, frame)
            cv2.imwrite(p2, frame)
            lst()
            main()

            # unreg()


        # face_names.append(name(out))
        elif name(out) == views.check_list():
            now = datetime.datetime.today()
            pht = "detected{}.jpg".format(str(now).replace(":", ''))
            # p=os.path.sep.join(['face_biometric_app/image', "detected{}.jpg".format(str(now).replace(":", ''))])
            # p=os.path.sep.join(['face_biometric_app/image', pht])
            s1 = os.path.sep.join(['face_biometric_app/check', pht])
            s2 = os.path.sep.join(['media/face_biometric_app/check', pht])
            cv2.imwrite(s1, frame)
            cv2.imwrite(s2, frame)
            check_listing()
            check_main()

        elif name(out) == views.check_one():
            now = datetime.datetime.today()
            pht = "detected{}.jpg".format(str(now).replace(":", ''))
            # p=os.path.sep.join(['face_biometric_app/image', "detected{}.jpg".format(str(now).replace(":", ''))])
            # p=os.path.sep.join(['face_biometric_app/image', pht])
            s1 = os.path.sep.join(['face_biometric_app/one', pht])
            s2 = os.path.sep.join(['media/face_biometric_app/one', pht])
            cv2.imwrite(s1, frame)
            cv2.imwrite(s2, frame)
            check_one()
            check_main_one()

        elif name(out) == views.check_two():
            now = datetime.datetime.today()
            pht = "detected{}.jpg".format(str(now).replace(":", ''))
            # p=os.path.sep.join(['face_biometric_app/image', "detected{}.jpg".format(str(now).replace(":", ''))])
            # p=os.path.sep.join(['face_biometric_app/image', pht])
            s1 = os.path.sep.join(['face_biometric_app/two', pht])
            s2 = os.path.sep.join(['media/face_biometric_app/two', pht])
            cv2.imwrite(s1, frame)
            cv2.imwrite(s2, frame)
            check_two()
            check_main_two()

        elif name(out) == views.check_three():
            now = datetime.datetime.today()
            pht = "detected{}.jpg".format(str(now).replace(":", ''))
            # p=os.path.sep.join(['face_biometric_app/image', "detected{}.jpg".format(str(now).replace(":", ''))])
            # p=os.path.sep.join(['face_biometric_app/image', pht])
            s1 = os.path.sep.join(['face_biometric_app/three', pht])
            s2 = os.path.sep.join(['media/face_biometric_app/three', pht])
            cv2.imwrite(s1, frame)
            cv2.imwrite(s2, frame)
            check_three()
            check_main_three()

        elif name(out) == views.check_four():
            now = datetime.datetime.today()
            pht = "detected{}.jpg".format(str(now).replace(":", ''))
            # p=os.path.sep.join(['face_biometric_app/image', "detected{}.jpg".format(str(now).replace(":", ''))])
            # p=os.path.sep.join(['face_biometric_app/image', pht])
            s4 = os.path.sep.join(['face_biometric_app/four', pht])
            s5 = os.path.sep.join(['media/face_biometric_app/four', pht])
            cv2.imwrite(s4, frame)
            cv2.imwrite(s5, frame)
            check_four()
            check_main_four()

        elif name(out) == views.check_five():
            now = datetime.datetime.today()
            pht = "detected{}.jpg".format(str(now).replace(":", ''))
            # p=os.path.sep.join(['face_biometric_app/image', "detected{}.jpg".format(str(now).replace(":", ''))])
            # p=os.path.sep.join(['face_biometric_app/image', pht])
            s6 = os.path.sep.join(['face_biometric_app/five', pht])
            s7 = os.path.sep.join(['media/face_biometric_app/five', pht])
            cv2.imwrite(s6, frame)
            cv2.imwrite(s7, frame)
            check_five()
            check_main_five()









        self.buf[self.i] = name(out)
        self.i = (self.i + 1) % self.buf_length



        # print(det(out,frame))



        # for item in f_Face_info.get_face_info(frame):
        #
        #     face_names.append(item)
        #     self.buf[self.i] = face_names
        #     self.i = (self.i + 1) % self.buf_length
        ret, frame = cv2.imencode('.jpg', frame)

        return frame.tobytes()

        # ret, buffer = cv2.imencode('.jpg', frame)
        # frame = buffer.tobytes()
        # yield (b'--frame\r\n'
        #        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')








