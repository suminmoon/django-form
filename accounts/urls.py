from django.urls import path
from . import views

# accounts:index 앱 name 역할
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),


]