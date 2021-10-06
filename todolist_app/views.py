from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def todolist(request):
    if request.method == "POST":
        form=TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
            messages.success(request,"New task added!")
        return redirect('todolist')
    else:
        allTasks=TaskList.objects.filter(manage=request.user)  #only shows user's tasks

        paginator=Paginator(allTasks, 5)   # on what objects?, how many objects on a single page?
        page=request.GET.get("pg")
        allTasks=paginator.get_page(page)

        return render(request, 'todolist.html', {'allTasks':allTasks})


def delete_task(request, task_id):  #task_id is required to delete the particular task
    task=TaskList.objects.get(pk=task_id)  # pk=primary key
    task.delete()  #task deleted
    messages.success(request,"Task deleted!")
    return redirect('todolist')


def edit_task(request, task_id):
    if request.method == "POST":
        task=TaskList.objects.get(pk=task_id)  # pk=primary key
        form=TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,"Task edited!")
        return redirect('todolist')
    else:
        task_obj=TaskList.objects.get(pk=task_id)  # pk=primary key
        return render(request, 'edit.html', {'task_obj':task_obj})


def complete_task(request, task_id):
    task=TaskList.objects.get(pk=task_id)  # pk=primary key
    task.done=True
    task.save()
    return redirect('todolist')

def pending_task(request, task_id):
    task=TaskList.objects.get(pk=task_id)  # pk=primary key
    task.done=False
    task.save()
    return redirect('todolist')






def index(request):
   return render(request, 'index.html', {'Welcome_Text':"Welcome to home page","title":"HomePage"}) 

def contact(request):
    return render(request, 'contact.html', {'Welcome_Text':"Welcome to contact page","title":"Contact"})


def about(request):
    return render(request, 'about.html', {'Welcome_Text':"Welcome to about page","title":"About Us"})