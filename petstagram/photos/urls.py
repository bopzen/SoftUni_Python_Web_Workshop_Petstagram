from django.urls import path, include
from petstagram.photos import views


urlpatterns = [
    path('add/', views.add_photo, name='photo-add'),
    path('<int:pk>/', include([
        path('', views.show_photo_details, name='photo-details'),
        path('edit/', views.edit_photo, name='photo-edit')
    ]))
]