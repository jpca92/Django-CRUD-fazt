from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def helloworld (request):
    title = 'Hello World'
    return render(request, 'signup.html',{
        'form': UserCreationForm,

    })

