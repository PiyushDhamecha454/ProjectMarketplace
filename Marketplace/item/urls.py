from django.urls import path

from . import views
import item
app_name = 'item'
urlpatterns = [
    path('', views.items, name='items'),
    path('<int:pk>/', views.details, name = 'detail'),
    path('<int:pk>/delete/', views.delete, name = 'delete'),
    path('<int:pk>/edit/', views.edit, name = 'edit'),
    path('new/', views.new, name='new'),
    ]