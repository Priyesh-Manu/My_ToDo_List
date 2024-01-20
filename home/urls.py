from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home' ),
    path('completed/<str:task_name>/',views.completed_task, name='completed' ),
]
