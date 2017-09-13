from django.conf.urls import url
from django.contrib import admin

from Website1.views import home, about, contact

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home, name='home'),
    url(r'^about/', about, name='about'),
    url(r'^contact/', contact, name='contact'),
]
