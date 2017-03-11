from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^answers/$', DuckList.as_view(), name='answers'),
]