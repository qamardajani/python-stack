from django.urls import path
from django.urls import path
from . import views
urlpatterns = [
    path ('', views.index),
    path ('add',views.add),
    path ('add1',views.add1)
]