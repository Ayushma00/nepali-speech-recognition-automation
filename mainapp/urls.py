from django.urls import path,include
from . import views

urlpatterns=[
path("",views.main,name="index"),
path("aa/",views.download,name="download"),
]
