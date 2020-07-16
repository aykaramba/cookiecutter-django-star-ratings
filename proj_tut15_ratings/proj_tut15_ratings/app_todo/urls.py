
from django.urls import path
from . import views

app_name = 'app_todo'

urlpatterns = [
    path('', views.index, name='url_list'),
    path('update/<str:pk>/', views.updateTask, name='url_update_task'),
    path('delete/<str:pk>/', views.deleteTask, name='url_delete'),
]

