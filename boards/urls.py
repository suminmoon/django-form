from django.urls import path
from . import views

# 경로 앱 이름 지정 'boards:detail'
app_name = 'boards'

# boards/
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:board_pk>/', views.detail, name='detail'),  # boards/3/
    path('create/', views.create, name='create'),
    path('<int:board_pk>/delete/', views.delete, name='delete'),
    path('<int:board_pk>/update/', views.update, name='update'),
]
