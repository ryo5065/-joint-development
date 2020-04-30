from django.shortcuts import render,redirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import School
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import FormModel

# Create your views here.
class Top(TemplateView):
    template_name = "top.html"

def zoom(request,pk):
    # 大学によって違う掲示板を表示することに一応成功
    # object_list = FormModel.objects.all()
    # ここでpk指定したい
    if pk == 1:
        object = FormModel.objects.filter(school__name = '関西大学')
    elif pk == 2:
        object = FormModel.objects.filter(school__name = '関西学院大学')
    elif pk == 3:
        object = FormModel.objects.filter(school__name = '同志社大学')
    else:
        object = FormModel.objects.filter(school__name = '立命館大学')
    
    
    return render(request, 'zoom_list_base.html', {'object':object}) 

# フォーム投稿用
class ZoomCreate(CreateView):
    template_name = 'create.html'
    # とりあえずエラー回避のため
    model = FormModel
    fields = ('title','date','camera','name','content')

    # def get_success_url(self, pk):
    #   return reverse_lazy("zoom", kwargs={'pk':self.kwargs['pk']} )
    success_url = reverse_lazy('create')




 

