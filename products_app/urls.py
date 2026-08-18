from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='index'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('history/', views.view_history, name='view_history'),
]
