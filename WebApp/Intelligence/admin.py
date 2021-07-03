from Configurations.auto_create_super_user import *
from django.contrib import admin

from Intelligence.models import Prediction, Video

# Register your models here.
admin.site.register(Prediction)
admin.site.register(Video)
