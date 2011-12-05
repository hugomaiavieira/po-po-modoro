from django.shortcuts import render_to_response
from apps.pomodoro.models import Task

def dashboard(request):
	return render_to_response('dashboard.html')

def todo_today(request):
	tasks = Task.objects.filter(worksheet='todo')
	return render_to_response('todo-today.html', {'tasks': tasks})

def inventory(request):
	tasks = Task.objects.filter(worksheet='inventory')
	return render_to_response('inventory.html', {'tasks': tasks})

