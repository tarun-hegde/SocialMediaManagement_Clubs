from django.shortcuts import render,redirect
from .forms import RegistrationForm,TaskForm,ClubForm,SubTaskForm
from .models import Task,SubTasks
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
# Create your views here.
#superuser:taruser
#password:1@2@3
#username:taru
#password:321321321@
#username:tsh
#password:@321321321
#username:one
#password:1one1one1one

@login_required(login_url='/login')
def base(request):
 return render(request,'first/base.html')
def case(request):
    return render(request,'first/case.html')
@login_required(login_url='/login')
def home(request):
    tasks=Task.objects.all()
    if request.method=="POST":
     task_id=request.POST.get("task-id")
     task=Task.objects.filter(id=task_id).first()
     if task and task.author==request.user:
        task.delete()
    return render(request,'first/home.html',{"tasks":tasks})
 
@login_required(login_url='/login')
def task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.author=request.user
            task.save()
            return redirect('/home')
    else:
        form=TaskForm()
    return render(request,'first/task.html',{"form":form}) 
@login_required(login_url='/login')
def subtask(request):
    tasks=SubTasks.objects.all()
    if request.method=="POST":
     task_id=request.POST.get("task-id")
     task=SubTasks.objects.filter(id=task_id).first()
     if task and task.author==request.user:
        task.delete()
    return render(request,'first/subtask.html',{"tasks":tasks})
 
@login_required(login_url='/login')
def subtasks(request):
    if request.method=='POST':
        form=SubTaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.author=request.user
            task.save()
            return redirect('/subtask')
    else:
        form=SubTaskForm()
    return render(request,'first/subtasks.html',{"form":form}) 
@login_required(login_url='/login')
def submit(request):
     return render(request,'first/submit.html') 
@login_required(login_url='/login')
def none(request):
    if request.method=='POST':
        form=ClubForm(request.POST)
        if form.is_valid():
            club=form.save(commit=False)
            club.author=request.user
            club.save()
            return redirect('/base')
    else:
        form=ClubForm()
    return render(request,'first/none.html',{"form":form}) 
def sign_up(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/login')
    else:
        form=RegistrationForm()
    return render(request,'registration/sign_up.html',{"form":form})
    
