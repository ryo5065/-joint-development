from django.shortcuts import render,redirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import School
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
class Top(TemplateView):
    template_name = "top.html"

def zoom(request,pk):
    return render(request,'zoom_list.html') #ここはエラーが出ないように適当に書いてるだけなので乾くん後はよろしくです
    


