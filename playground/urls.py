from django.urls import path
from . import views
import playground

urlpatterns = [
    path('home/', views.index)
]