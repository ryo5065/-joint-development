from django.shortcuts import render,redirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import School
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import FormKuModel, FormKgModel, FormDuModel, FormRuModel

# Create your views here.
class Top(TemplateView):
    template_name = "top.html"

def zoom(request,pk):
    # 大学によって違う掲示板を表示することに一応成功
    # object_list = FormModel.objects.all()
    # ここでpk指定したい
    if pk == 1:
        file = 'zoom_list_1.html'
        object_list = FormKuModel.objects.all()
    elif pk == 2:
        file = 'zoom_list_2.html'
        object_list = FormKgModel.objects.all()
    elif pk == 3:
        file = 'zoom_list_3.html'
        object_list = FormDuModel.objects.all()
    else:
        file = 'zoom_list_4.html'
        object_list = FormRuModel.objects.all()
    
    return render(request, file, {'object_list':object_list}) 

# フォーム投稿用
class ZoomCreate(CreateView):
    template_name = 'create.html'
    # とりあえずエラー回避のため
    model = FormKuModel
    fields = ('title','date','camera','name','content')

    # def get_success_url(self, pk):
    #   return reverse_lazy("zoom", kwargs={'pk':self.kwargs['pk']} )
    success_url = reverse_lazy('create')




 

