from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import TemplateView
from website1.views import Weights,SeanWeightListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^weight/$', Weights, name='weight'),
    url(r'^weight/sean/$', SeanWeightListView.as_view(), name='weight'),
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
