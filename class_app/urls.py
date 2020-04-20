from django.contrib import admin
from django.urls import path,include
from .views import Top,zoom


urlpatterns = [
    path('',Top.as_view(),name="top"),
    path('zoom/<int:pk>',zoom,name="zoom")
]
