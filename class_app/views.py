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
    
def clubfunc(request,pk):
    school = School.objects.get(pk=pk)
    clubs = school.clubs.all()
    lists = []
    for club in clubs:
        lists2 = []
        club_name = club.name
        circle = club.circle_set.filter(school_id=pk) #ここまでは行けてるぽい。大学ごとのサークル取り出せている
        lists2 += (club_name,circle)
        lists.append(lists2)
    school_name = school.name
    q_word = request.GET.get("query")
    if q_word:
        clubs = clubs.filter(
            Q(name__icontains=q_word))
    x = {
        'school_name':school_name,
        'clubs1':clubs,
        'lists1':lists
    }
    return render(request,"club.html",x)




