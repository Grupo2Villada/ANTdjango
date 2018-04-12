from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.conf import settings
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
# Create your views here.
from .models import *
from .forms import *
from django import forms
import time

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

def grade_post(request):
    if request.method == "POST":
        form = FormGrade(request.POST)
        if form.is_valid():
            post = form.instance
            post.user = request.user
            post.published_date = timezone.now()
            post.save() 
            time.sleep(3)
        return redirect('/')
    else:
        form = FormGrade() 
    return render(request, 'index.html', {'form': form})