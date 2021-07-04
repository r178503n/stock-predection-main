from django.conf import settings
from django.conf.urls import handler404, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.core.mail import send_mail
from django.urls import include, path, re_path
from django.views.generic import RedirectView, TemplateView

from . import views

urlpatterns = [
path('list', views.StockList.as_view(), name='index'),
path('train', views.TrainModelView.as_view(), name='train'),
 path('predict/<name>', views.predictionView, name='predict'),
 # path('train/<name>', views.trainView, name='train'),
  #  path('train/<name>', views.TView.as_view(), name='train'),

# re_path(r'^(?P<path>.*)$', TemplateView.as_view(template_name='angular.html'), name="home"),
]

