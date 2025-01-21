from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks:task_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Filtre par utilisateur connecté

    # Filtrage par date d'échéance
    due_date = request.GET.get('due_date')
    if due_date:
        tasks = tasks.filter(due_date=due_date)

    # Filtrage par priorité
    priority = request.GET.get('priority')
    if priority:
        tasks = tasks.filter(priority=priority)
        
    category = request.GET.get('category')
    if category:
        tasks = tasks.filter(category=category)

    # Context avec les tâches et les choix de priorité pour le formulaire de filtrage
    context = {
        'tasks': tasks,
        'priorities': Task.PRIORITY_CHOICES,  # Passer les choix de priorité au template
        'categories': Task.CATEGORY_CHOICES, # Passer les categoies de priorité au template de categories
    }

    return render(request, 'tasks/task_list.html', context)


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Associe la tâche à l'utilisateur connecté
            task.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # Assure que la tâche appartient à l'utilisateur
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # Assure que la tâche appartient à l'utilisateur
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


# from django.shortcuts import render,redirect, reverse , get_list_or_404, get_object_or_404

# # Create your views here.
# from .models import Task
# from .forms import TaskForm

# def task_list(request):
#     tasks = Task.objects.all()
#     context = {'tasks': tasks}
#     return render(request, 'tasks/task_list.html', context)


# def task_create(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('tasks:task_list')
#     else:
#         form = TaskForm()
#     return render(request, 'tasks/task_form.html', {'form': form})


# def task_update(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('tasks:task_list')
#     else:
#         form = TaskForm(instance=task)
#     return render(request, 'tasks/task_form.html', {'form': form, 'task': task})


# def task_delete(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method == 'POST':
#         task.delete()
#         return redirect('tasks:task_list')
#     return render(request, 'tasks/task_confirm_delete.html', {'task': task})




