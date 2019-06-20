from django.urls import path
from . import views

# boards:index 앱 name 역할
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name = 'update'),
    path('password/', views.change_password, name='change_password'),
    path('delete/', views.delete, name='delete'),

]
