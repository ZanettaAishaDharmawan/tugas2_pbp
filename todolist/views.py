import datetime

from django.shortcuts import render
from todolist.models import Task
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = Task.objects.filter(user=request.user)
    context = {
        'list_todo': data,
        'username': request.user.username,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password')
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == 'POST':
        date = datetime.datetime.now()
        title = request.POST.get('todolist')
        description = request.POST.get('description')
        user = request.user
        is_finished = False
        obj = Task.objects.create (date=date, title=title, description=description, user=user, is_finished=is_finished)
        obj.save()
        response = HttpResponseRedirect(reverse("todolist:show_todolist"))
    return render(request, 'tambah.html')

def delete_task(request, pk):
    Task.objects.filter(id=pk).delete()
    return redirect('todolist:show_todolist')

def change_task(request, pk):
    data = Task.objects.get(id=pk)
    data.is_finished = not(data.is_finished)
    data.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def show_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', task), content_type='application/json')

def add_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        user = request.user
        is_finished = False
        item = Task(title=title, description=description, date=date, user=user, is_finished=is_finished)
        item.save()
    return JsonResponse({"instance": "Proyek Dibuat"},status=200)

@csrf_exempt    
def delete(request, pk):
    if request.method == 'DELETE':
        Task.objects.filter(id=pk).delete()
    return JsonResponse({"instance": "Proyek Dihapus"},status=200)