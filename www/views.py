# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def categories(request):
    return render(request, 'category-list.html')

def topics(request):
    return render(request, 'list-topic.html')

def questions(request):
    return render(request, 'questions.html')

def new_question(request):
    return render(request, 'post-question.html')

def discussion(request):
    return render(request, 'discussion.html')
