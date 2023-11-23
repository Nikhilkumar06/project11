from generic.views import *
from django.urls import path
app_name='generic'
urlpatterns=[
    path('munnabhayya/',munnabhayya,name='munnabhayya'),
    path('guddubhayya/',guddubhayya,name='guddubhayya'),
]