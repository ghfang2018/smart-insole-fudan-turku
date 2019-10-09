from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="steplab-home"),
    path('recordings/', views.recordings, name="steplab-recordings"),
    path('diagnosis/new', views.newDiagnose, name="steplab-diagnosis-new"),
    path('diagnosis/', views.diagnosis, name="steplab-diagnosis"),
    path('about/', views.about, name="steplab-about"),
]
