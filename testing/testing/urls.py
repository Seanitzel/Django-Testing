from django.conf.urls import url
from django.contrib import admin

from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView

from website1.views import Weights, WeightListView, WeightDetailView, WeightCreateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(), name = 'login'),
    url(r'^weight/$', WeightListView.as_view()),
    url(r'^weight/create/$', WeightCreateView.as_view()),
    url(r'^weight/(?P<slug>[\w-]+)/$', WeightDetailView.as_view()), #view with the get_object function
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
