from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('advisory/',views.advisory,name='advisory'),
    path("diagnosis/", views.diagnosis, name="diagnosis"),
    path("brics-hub/", views.brics_hub, name="brics_hub"),

]