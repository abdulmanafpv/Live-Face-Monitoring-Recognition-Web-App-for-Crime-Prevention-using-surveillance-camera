import cv2
import numpy as np
import face_recognition

# from gen_detection import Gender_Model
# from race_detection import Race_Model

from face_biometric_app .models import Employee, Detected
from cachetools import TTLCache
import datetime, time
from face_biometric_app .my_face_recognition import f_main
cache = TTLCache(maxsize=20, ttl=60)



# instanciar detectores
# age_detector = Age_Model()
# gender_detector =  Gender_Model()
# race_detector = Race_Model()
# emotion_detector = predict_emotions()
rec_face = f_main.rec()
#----------------------------------------------


def identify1(frame, name, buf, buf_length, known_conf):
    if name in cache:
        return
    count = 0
    for ele in buf:
        count += ele.count(name)

    if count >= known_conf:
        # timestamp = datetime.datetime.now(tz=timezone.utc)
        timestamp = datetime.datetime.today()
        print(name, timestamp)
        cache[name] = 'detected'
        path = 'detected/{}_{}.jpg'.format(name, timestamp)
        write_path = 'media/' + path
        cv2.imwrite(path, frame)
        try:
            emp = Employee.objects.get(name=name)
            emp.detected_set.create(time_stamp=timestamp, photo=path)
        except:
            pass

global buf_length, known_conf ,i
buf_length = 10
known_conf = 6
i = 0





def get_face_info(im):
    # face detection
    boxes_face = face_recognition.face_locations(im)
    out = []
    if len(boxes_face)!=0:
        for box_face in boxes_face:
            # segmento rostro
            box_face_fc = box_face
            x0,y1,x1,y0 = box_face
            box_face = np.array([y0,x0,y1,x1])
            face_features = {
                "name":[],
                # "age":[],
                # "gender":[],
                # "race":[],
                # "emotion":[],
                "bbx_frontal_face":box_face
            }

            face_image = im[x0:x1,y0:y1]

            # -------------------------------------- face_recognition ---------------------------------------
            face_features["name"] = rec_face.recognize_face2(im,[box_face_fc])[0]

            # -------------------------------------- age_detection ---------------------------------------
            # age = age_detector.predict_age(face_image)
            # face_features["age"] = str(round(age,2))

            # -------------------------------------- gender_detection ---------------------------------------
            # face_features["gender"] = gender_detector.predict_gender(face_image)

            # -------------------------------------- race_detection ---------------------------------------
            # face_features["race"] = race_detector.predict_race(face_image)

            # -------------------------------------- emotion_detection ---------------------------------------
            # _,emotion = emotion_detector.get_emotion(im,[box_face])
            # face_features["emotion"] = emotion[0]

            # -------------------------------------- out ---------------------------------------
            out.append(face_features)
    else:
        face_features = {
            "name":[],
            # "age":[],
            # "gender":[],
            # "race":[],
            # "emotion":[],
            "bbx_frontal_face":[]
        }
        out.append(face_features)
    return out


face_names=[]

def bounding_box(out,img):
    buf = [[]] * buf_length
    i = 0
    # face_names=[]
    lst=[]
    for data_face in out:
        box = data_face["bbx_frontal_face"]
        if len(box) == 0:
            continue
        else:
            x0,y0,x1,y1 = box
            img = cv2.rectangle(img,
                            (x0,y0),
                            (x1,y1),
                            (0,255,0),2);
            thickness = 2
            fontSize = 0.75
            step = 13

            # try:
            #     cv2.putText(img, "age: " +data_face["age"], (x0, y0-7), cv2.FONT_HERSHEY_SIMPLEX, fontSize, (0,0,255), thickness)
            # except:
            #     pass
            # try:
            #     cv2.putText(img, "gender: " +data_face["gender"], (x0, y0-step-10*1), cv2.FONT_HERSHEY_SIMPLEX, fontSize, (0,255,0), thickness)
            # except:
            #     pass
            # try:
            #     cv2.putText(img, "race: " +data_face["race"], (x0, y0-step-10*3), cv2.FONT_HERSHEY_SIMPLEX, fontSize, (0,255,0), thickness)
            # except:
            #     pass
            # try:
            #     cv2.putText(img, "emotion: " +data_face["emotion"], (x0, y0-step-10*2), cv2.FONT_HERSHEY_SIMPLEX, fontSize, (0,0,255), thickness)
            # except:
            #     pass
            try:
                cv2.putText(img, "name: " +data_face["name"], (x0, y0-step-10*1), cv2.FONT_HERSHEY_SIMPLEX, fontSize, (0,0,255), thickness)
                # identify1(img, data_face["name"], buf, buf_length, known_conf)
                # face_names.append(data_face['name'])

            except:
                pass
            # identify1(img, data_face['name'], buf, buf_length, known_conf)
            # face_names.append(data_face['name'])
            # buf[i] = face_names
            # i = (i + 1) % buf_length

    return img


def name(out):
    for data_face in out:
        # box = data_face["bbx_frontal_face"]
        data=data_face['name']
        return data
        # if len(box) == 0:
        #     continue
        # else:
        #     x0, y0, x1, y1 = box
        #     img = cv2.rectangle(img,
        #                         (x0, y0),
        #                         (x1, y1),
        #                         (0, 255, 0), 2);
        #     thickness = 2
        #     fontSize = 1.0
        #     step = 13



def det():
   return face_names

