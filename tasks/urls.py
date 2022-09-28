from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('update/<str:pk>/', views.update_todo, name='update'),
    path('delete/<str:pk>/', views.delete_todo, name='delete')
]