from django.shortcuts import render , redirect, get_object_or_404
from .models import Tasks

def main(request):
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)

def add_task(request):
    if request.method == "POST":
        cont = request.POST.get('addNewTask')
        if cont :
            data = Tasks(content = cont)
            data.save()
            return redirect('home')

def mark_as_completed(request, task_id):
    task = get_object_or_404(Tasks, id = task_id)
    task.is_completed = True
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return redirect('home')

def delete_all_tasks(request):
    task = Tasks.objects.all()
    task.delete()
    return redirect('home')

def incomplete_task(request):
    if request.method == 'POST':
        tasks = Tasks.objects.filter(is_completed=False)
        context = {'tasks': tasks}
        return render(request, 'index.html', context)
    else:
        return redirect('index')

def complete_task(request):
    if request.method == 'POST':
        tasks = Tasks.objects.filter(is_completed=True)
        context = {'tasks': tasks}
        return render(request, 'index.html', context)
    else:
        return redirect('index')
    
def see_all_tasks(request):
    if request.method == 'POST':
        tasks = Tasks.objects.all()
        context = {'tasks': tasks}
        return render(request, 'index.html', context)
    else:
        return redirect('home')
