from django.conf.urls import url
from .views import AnswerList

urlpatterns = [
    url(r'^answers/$', AnswerList.as_view(), name='answers'),
]