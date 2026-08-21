from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='index'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('history/', views.view_history, name='view_history'),
    path('favorites/', views.favorites, name='favorites'),
    path('favorites/<int:pk>/toggle/', views.toggle_favorite, name='toggle_favorite'),
    path('cart/<int:pk>/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/<int:pk>/remove/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/add/', views.course_add, name='course_add'),
    path('admin-panel/edit/<int:pk>/', views.course_edit, name='course_edit'),
    path('admin-panel/delete/<int:pk>/', views.course_delete, name='course_delete'),
]
