from django.urls import path
from .api import *
from knox import views as knox_views


urlpatterns = [
    path(route = 'register/', view = RegisterApi.as_view(), name = 'register'),
    path(route = 'login/', view = LoginView.as_view(), name = 'login'),    
    path(route = 'logout/', view = knox_views.LogoutView.as_view(), name = 'logout'),
]