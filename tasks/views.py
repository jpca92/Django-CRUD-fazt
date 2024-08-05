from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone

from .forms import TaskForm
from .models import Task


def helloworld (request):
    title = 'Hello World'
    return render(request, 'signup.html',{
        'form': UserCreationForm,

    })

def home(request):
    return render(request, 'home.html',)

def signup(request):

    if request.method == 'GET':
        print('enviando formulario')
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                }) 
        return render(request, 'signup.html',{
            'form': UserCreationForm,
            'error': 'Password do not match'
        })

        print(request.POST)
        print('obteniendo datos' )
    return render(request, 'signup.html',{
        'form': UserCreationForm
    })

def tasks (request):
    # user = request.user solo muestra las tareas creadas por ese usuario
    # datecompleted__isnull solo muestra tareas sin terminar
    tasks = Task.objects.filter(user = request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {'tasks': tasks})

def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull = False).order_by('-datecompleted')
    return render (request, 'tasks.html',{'tasks':tasks})

def create_task(request):
    if request.method == 'GET':
        return render (request, 'create_task.html', {
            'form':TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            print(new_task)
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html',{
                'form': TaskForm,
                'error': 'Please enter valid data'
            })
        
def task_detail(request, task_id):
    if request.method == 'GET':
        # Esta linea arroja una pagina 404 si no encuentra la task con el id que solicitemos
        task = get_object_or_404(Task, pk=task_id)
        # task = Task.objects.get(pk=task_id)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {
            'task': task,
            'form': form
            })
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user = request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {
                'task': task, 
                'form': form,
                'error': 'Error updating task'
            })

def complete_task (request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')
    
def delete_task (request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    # renderiza el formulario
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        # if method == 'POST', estamos enviando datos al servidor y pasa lo siguiente
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(request.POST)
        # si el usuario no existe
        if user is None:
            return render(request, 'signin.html',{
            'form': AuthenticationForm,
            'error': 'username or password incorrect'
            })
        # Si user si tiene algo entonces, user existe
        else:
            login(request, user)
            return redirect('tasks')
    
