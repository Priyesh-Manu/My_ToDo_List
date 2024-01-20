from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home' ),
    path('completed/<int:id>/',views.completed_task, name='completed' ),
    path('delete/<int:id>/',views.delete_completed_task, name='delete' ),
]
