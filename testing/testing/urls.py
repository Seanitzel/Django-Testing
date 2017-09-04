from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import TemplateView
from website1.views import Weights,WeightListView,WeightDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^weight/$', Weights, name='weight'),
    url(r'^weight/$', WeightListView.as_view(), name='weight'),
    #url(r'^weight/(?P<slug>\w+)$', WeightListView.as_view(), name='weight'),
    #url(r'^weight/(?P<pk>\w+)$', WeightDetailView.as_view(), name='weight'),   # View with the get_context_data function
    url(r'^weight/(?P<per_id>\w+)$', WeightDetailView.as_view(), name='weight'), #view with the get_object function
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
