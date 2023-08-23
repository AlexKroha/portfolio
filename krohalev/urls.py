from django.urls import path
from .views import *

app_name = 'krohalev'
urlpatterns = [
    path('', home, name='home'),
]
