from django.contrib import admin
from face_biometric_app.models import Detected,Employee,unreg,Checking, Checking_One, Checking_Two, Checking_Three
from face_biometric_app.models import Checking_Four, Checking_Five, Upload_image
# Register your models here.
admin.site.register(Detected),
admin.site.register(Employee),
admin.site.register(unreg),
admin.site.register(Checking),
admin.site.register(Checking_One),
admin.site.register(Checking_Two),
admin.site.register(Checking_Three),
admin.site.register(Checking_Four),
admin.site.register(Checking_Five),
admin.site.register(Upload_image),

