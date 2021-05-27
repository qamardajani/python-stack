from django.urls import path     
from . import views
urlpatterns = [
    path('',views.ind),
    path('shows/', views.index),
    path('shows/new/',views.new),
    path('shows/create',views.create),
    path('shows/<int:id>', views.data),
    path('shows/<int:id>/edit', views.renderedit),
    path('edit/<int:id>', views.edit),
    path ('delete/<int:id>',views.delete),

]