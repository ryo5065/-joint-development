from django.contrib import admin
from django.urls import path,include
from .views import Top,zoom,clubfunc,postfunc


urlpatterns = [
    path('',Top.as_view(),name="top"),
    path('zoom/<int:pk>',zoom,name="zoom"),
    path('zoom_post/<int:pk>',postfunc,name="post"),
    path('club/<int:pk>',clubfunc,name="club")
]
