from django.urls import path
from . import views

app_name ='projx'
urlpatterns = [
    path('',views.home,name='home'),
]
