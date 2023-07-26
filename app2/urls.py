from django.urls import path
from app2.views import*
app_name="app2"
urlpatterns=[
    path('new3/',new3,name='new3'),
    path('new4/',new4,name='new4'),
]