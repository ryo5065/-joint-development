from django.contrib import admin
from django.urls import path,include
from .views import Top, zoom, ZoomCreate

urlpatterns = [
    path('',Top.as_view(),name="top"),
    path('zoom/<int:pk>',zoom,name="zoom"),
    path('create/', ZoomCreate.as_view(), name="create"),
]
