from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import School
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


class Top(TemplateView):
    template_name = "top.html"


def zoom(request, pk):
    return render(request, 'zoom_list.html')


def clubfunc(request, pk):
    school = School.objects.get(pk=pk)
    clubs = school.clubs.all()
    lists = []
    alert = ""
    for club in clubs:
        lists2 = []
        club_name = club.name
        # ここまではいけてるぽい。大学ごとのサークル取り出せている
        circle = club.circle_set.filter(school_id=pk)
        lists2 += (club_name, circle)
        lists.append(lists2)
    q_word1 = request.GET.get("query1")
    q_word2 = request.GET.get("query2")
    if q_word2:
        lists = []
        lists3 = []
        try:
            clubs = clubs.get(
                Q(name__icontains=q_word2))
            club_name = clubs.name
            circle = clubs.circle_set.filter(school_id=pk)
            lists3 += (club_name, circle)
            lists.append(lists3)
        except:
            alert = "検索に一致するものがありませんでした。"
    if q_word1 and not q_word2:
        clubs = school.clubs.filter(types=q_word1)
        lists = []
        alert = ""
        for club in clubs:
            lists4 = []
            club_name = club.name
            circle = club.circle_set.filter(school_id=pk)
            lists4 += (club_name, circle)
            lists.append(lists4)
       
    paginator = Paginator(lists, 10)  # 1ページに10件表示
    page_num = request.GET.get('page', 1)
    # pages = paginator.page(page_num) これのせいでtry exceptきいてなかった
    try:
        pages = paginator.page(page_num)
    except PageNotAnInteger:
        # 数字じゃなかったら1ページ目を表示
        pages = paginator.page(1)

    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
        # 4以降の数字の場合、最後のページを表示
    x = {
        'school': school,
        'clubs1': clubs,
        'page_obj': pages,
        'alert1': alert,
        'is_paginated': pages.has_other_pages,
    }
    return render(request, "club.html", x)
