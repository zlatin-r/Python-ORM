from django.urls import path
from Fruitipedia.fruits import views

urlpatterns = (
    path('', views.index, name='index'),
)
