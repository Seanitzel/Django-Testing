from django.conf.urls import url

from .views import PersonListView, PersonDetailView, PersonCreateView

urlpatterns = [
    url(r'^$', PersonListView.as_view(), name='list'),
    url(r'^create/$', PersonCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', PersonDetailView.as_view(), name='detail'),
]
