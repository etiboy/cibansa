# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from account.forms import LoginForm

# Create your views here.
def account_login(request):
    context = {
        login_form: LoginForm
    }