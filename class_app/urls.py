from django.contrib import admin
from django.urls import path,include
from .views import Top,zoom,clubfunc


urlpatterns = [
    path('',Top.as_view(),name="top"),
    path('zoom/<int:pk>',zoom,name="zoom"),
    path('club/<int:pk>',clubfunc,name="club")
]
