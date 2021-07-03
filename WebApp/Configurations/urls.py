from django.conf import settings
from django.conf.urls import handler404, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.core.mail import send_mail
from django.urls import include, path, re_path
from django.views.generic import RedirectView, TemplateView

urlpatterns = [

   path('admin/', admin.site.urls),
   path('', include('Stock.urls')),   
   path('django_plotly_dash/', include('django_plotly_dash.urls')),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)

urlpatterns += [
# re_path(r'^(?P<path>.*)$', TemplateView.as_view(template_name='angular.html'), name="home"),
]
