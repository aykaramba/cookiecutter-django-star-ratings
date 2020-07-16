from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

@login_required
def index(request):
    #return HttpResponse('why, hellooooo  there dahling') 
    tasks = Task.objects.all()
    form = FormTaskCreate()
    if request.method == 'POST':
        form = FormTaskCreate(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
        return redirect('app_todo:url_list')
    context = {'tasks':tasks, 'form':form}
    return render(request, 'app_todo/list.html', context)

def updateTask(request, pk):
    #return HttpResponse('why, hellooooo  there dahling') 
    task = Task.objects.get(id=pk)
    form = FormTaskUpdate(instance=task)
    if request.method == 'POST':
        form = FormTaskUpdate(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('app_todo:url_list')
    context = {'task':task, 'form':form}
    return render(request, 'app_todo/update_task.html', context)

def deleteTask(request, pk):
    #return HttpResponse('why, hellooooo  there dahling') 
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('app_todo:url_list')
    context = {'item':item}
    return render(request, 'app_todo/delete.html', context )


