from django.conf import settings
from django.conf.urls import handler404, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.core.mail import send_mail
from django.urls import include, path, re_path
from django.views.generic import RedirectView, TemplateView

from . import views

urlpatterns = [
path('', views.index, name='index'),
 path('predict/<name>', views.predictionView, name='predict'),
  path('train/<name>', views.trainView, name='train'),
  #  path('train/<name>', views.TView.as_view(), name='train'),

  
]

