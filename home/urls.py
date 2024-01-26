from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home' ),
    path('completed/<int:id>/',views.completed_task, name='completed' ),
    path('delete/<int:id>/',views.delete_completed_task, name='delete' ),
    path('redo/<int:id>/',views.redo_completed_task, name='redo' ),
    path('edit/<int:id>/',views.edit_task, name='edit' ),
    path('about/',views.about, name='about' ),
    path('contact/',views.contact, name='contact' ),
]
