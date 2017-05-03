from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name = 'www'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^discussion/$', views.discussion, name='discussion'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^questions/$', views.questions, name='questions'),
    url(r'^new-question/$', views.new_question, name='new-question'),
]
