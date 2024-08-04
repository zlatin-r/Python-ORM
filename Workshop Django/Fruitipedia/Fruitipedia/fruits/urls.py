from django.urls import path, include

from Fruitipedia.fruits import views

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-category/', views.create_category, name='create_category'),
    path('create-fruit/', views.create_view, name='create-fruit'),
    path('<int:pk>/', include([
        path('edit-fruit/', views.edit_view, name='edit-fruit'),
        path('delete-fruit/', views.delete_view, name='delete-fruit'),
        path('details-fruit/', views.details_view, name='details-fruit'),
    ]))
)
