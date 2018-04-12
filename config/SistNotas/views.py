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

import json
from django.core.serializers.json import DjangoJSONEncoder

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

def get_alumnos(request):
    id_materia = request.GET.get('id_materia', None)
    if id_materia:
        alumnos = Subject.objects.get(pk=int(id_materia)).students.all().values("id","last_name","first_name")
        serialized_alumnos = json.dumps(list(alumnos), cls=DjangoJSONEncoder)
        print serialized_alumnos
    return JsonResponse(serialized_alumnos, safe=False)

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

def get_subjects(request):
    if not request.user.is_authenticated():
        print "No user"
    elif request.user.is_superuser:
        print "Superuser"
    else:
        #print request.user
        subjects = Subject.objects.filter(professors__user=request.user).values("id","name")
        serialized_subjects = json.dumps(list(subjects), cls=DjangoJSONEncoder)
        print serialized_subjects
    return JsonResponse(serialized_subjects, safe=False)


    