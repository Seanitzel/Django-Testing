from django.conf.urls import url

from .views import WeightListView, WeightDetailView, WeightCreateView

urlpatterns = [
    url(r'^$', WeightListView.as_view(), name='list'),
    url(r'^create/$', WeightCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', WeightDetailView.as_view(), name='detail'),
]
