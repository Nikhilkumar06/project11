from specific.views import *
from django.urls import path
app_name='specific'
urlpatterns=[
    path('kaleenbhayya/',kaleenbhayya,name='kaleenbhayya'),
    path('beena/',beena,name='beena'),
]