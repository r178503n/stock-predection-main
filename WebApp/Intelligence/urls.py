from django.conf import settings
from django.conf.urls import handler404, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.core.mail import send_mail
from django.urls import include, path, re_path
from django.views.generic import RedirectView, TemplateView

from . import views

urlpatterns = [
  path('post', views.UploadVideoView.as_view(), name='intelligence'),
  path('split-images', views.SplitImagesFromVideo.as_view(), name='split-images'),
  path('start-prediction', views.PredictView.as_view(), name='process-prediction'),
  path('predicted-list', views.PredictedListView.as_view(), name='predicted-list'),
  
]

