from django.urls import path,include
from . import views

urlpatterns=[
path("",views.main,name="index"),
path("download/<str:text>",views.download,name="download"),
]
