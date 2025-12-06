from django.urls import path
from .api_views import *


app_name = 'accounts_api'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    
]