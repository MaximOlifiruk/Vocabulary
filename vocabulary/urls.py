from django.urls import path
from vocabulary import views
 
urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/', views.read),
    path('create/word/',  views.create_word),
    path('read/edit/<int:id>/', views.edit),
    path('read/delete/<int:id>/', views.delete),
]