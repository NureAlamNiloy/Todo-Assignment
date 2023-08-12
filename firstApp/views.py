from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.

def home(request):
    return render(request, 'home.html')

def addTask(request):
    if request.method == 'POST':
        task = forms.taskForm(request.POST)
        if task.is_valid():
            task.save()
            print(task.cleaned_data)
            return redirect('showTask')
    else:
        task = forms.taskForm()
    return render(request, 'add.html',{'form' : task})


def showTask(request):
    task = models.taskModel.objects.all()
    print(task)
    return render(request, 'show-task.html',{'data' : task})

def editTask(request,id):
    edtask = models.taskModel.objects.get(pk = id)
    form = forms.taskForm(instance = edtask) 
    if request.method == 'POST':
        edtask = forms.taskForm(request.POST, instance = edtask)
        if edtask.is_valid():
            edtask.save()
            return redirect('showTask') 
    return render(request, 'add.html',{'form' : form})

def deleteTask(request,id):
    task = models.taskModel.objects.get(pk = id).delete()
    return redirect('showTask') 

def completeTask(request, id):
    task = models.taskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('showTask')


def completeTasks(request):
    completed_tasks = models.taskModel.objects.filter(is_completed=True)
    return render(request, 'complete.html', {'completed_tasks': completed_tasks})