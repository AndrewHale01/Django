from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='index'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('history/', views.view_history, name='view_history'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/add/', views.course_add, name='course_add'),
    path('admin-panel/edit/<int:pk>/', views.course_edit, name='course_edit'),
    path('admin-panel/delete/<int:pk>/', views.course_delete, name='course_delete'),
]
