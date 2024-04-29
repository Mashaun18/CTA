from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.cta_dashboard, name='cta_dashboard'),
    path('execute_command/', views.execute_command, name='execute_command'),
    path('add_section/', views.add_section, name='add_section'),
    path('create_section/', views.create_section, name='create_section'),
    path('delete_section/', views.delete_section, name='delete_section'),
]