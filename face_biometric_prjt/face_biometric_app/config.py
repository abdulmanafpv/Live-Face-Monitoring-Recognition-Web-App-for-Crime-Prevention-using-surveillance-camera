# -------------------------------------- emotion_detection ---------------------------------------
# modelo de deteccion de emociones
# path_model = 'face_biometric_app/emotion_detection/Modelos/model_dropout.hdf5'
# Parametros del modelo, la imagen se debe convertir a una de tamaño 48x48 en escala de grises
w,h = 48,48
rgb = False
labels = ['angry','disgust','fear','happy','neutral','sad','surprise']

# -------------------------------------- face_recognition ---------------------------------------
# path imagenes folder
# path_images = "face_biometric_app/images_db"

# from .models import Employee
#
# def fetch():
#     img = Employee.objects.values_list('photo').order_by('-id')
#     print(type(img))


# img = Employee.objects.values_list('photo').order_by('-id')

# list=[]
# list.append(img)
# photo=list[-1]

path_images = "media/face_biometric_app/pictures"
# path_images = "face_biometric_app/images_db"


# path_images = img



