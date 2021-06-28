from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('files/', views.getFiles, name='files_dir'),
]
