import cv2
from face_biometric_app import f_Face_info
import glob
from face_biometric_app .f_Face_info import name
from face_biometric_app.camera import identify1
import os
import shutil

def delete():
    files = glob.glob('media/face_biometric_app/upload/*')
    for f in files:
        os.remove(f)



cpy_img_lst=['']


img_path='media/face_biometric_app/upload'
chck_img=[]
def load_img():
    for image in glob.iglob(f'{img_path}/*'):
        cpy_img_lst.append(image)
        print(cpy_img_lst.append(image))
        photo = cpy_img_lst[-1]
        return photo
    # for image in glob.iglob(f'{img_path}/*'):
    #     chck_img.append(image)
    #     print(chck_img.append(image))
    #     photo = chck_img[-1]
    #     return photo



def img():
    load_img()
    frame=cv2.imread(load_img())
    out= f_Face_info.get_face_info(frame)
    frame= f_Face_info.bounding_box(out,frame)
    identify1(frame, name(out))
    names=name(out)
    print(names)
    # frame = cv2.imencode('.jpg', frame)
    return names
    # cv2.imshow('Face info', frame)
    # cv2.waitKey(0)

