from django.urls import path
from . import views, views_login


urlpatterns = [

    path('login',views_login.login, name = 'login'),
    path('rooms/', views.get_rooms),
    path('detail_room/<pk>/', views.detail_room),
    path('detail_room/<pk>/messages/', views.get_messages)
]