from django.urls import path
from numpy import delete
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>',views.room, name="room"),
    path('create-room', views.create_room, name="create-room"),
    path('room_form/<str:pk>', views.update_room, name="update-room"),
    path('delete-room/<str:pk>', views.delete_room, name="delete-room")

]