from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm


def index(request):
    tasks = Tasks.objects.order_by('-id')
    return render(request, 'main/home.html', {'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def add(request):
    error = ''
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'ERROR'
    form = TasksForm()
    return render(request, 'main/add.html', {'form': form, 'error': error})