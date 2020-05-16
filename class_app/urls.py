from django.contrib import admin
from django.urls import path,include
from .views import Top,clubfunc,exfunc,spatialfunc,exspfunc,zoom,postfunc


urlpatterns = [
    path('',Top.as_view(),name="top"),
    path('club/<int:pk>',clubfunc,name="club"),
    path('ex/<int:pk>',exfunc,name="explanation"),
    path('spatial/<int:pk>',spatialfunc,name="spatial"),
    path('exsp/<str:space>/<int:pk>',exspfunc,name="exsp"),
    path('zoom/<int:pk>',zoom,name="zoom"),
    path('zoom_post/<int:pk>',postfunc,name="post"),
]
