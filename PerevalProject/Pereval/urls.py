from django.urls import path
from .views import *

urlpatterns = [
    path('submitData', PerevalAddAPI.as_view())
    ]