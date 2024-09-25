# chatapp/urls.py
from django.urls import path
from . import views

app_name = 'chatapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('get/', views.get_bot_response, name='get_bot_response'),
]
