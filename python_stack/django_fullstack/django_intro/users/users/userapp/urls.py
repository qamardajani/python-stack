from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path ('display',views.add),
    path ('get/<id>', views.get),
]