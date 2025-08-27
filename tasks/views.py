from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Task, Tag

def index(request):
    return render(request, 'tasks/index.html')


class TaskListView(ListView):
    model = Task


class TagListView(ListView):
    model = Tag


class TaskDetailView(DetailView):
    model = Task


class TagDetailView(DetailView):
    model = Tag

class TaskCreateView(CreateView):
    model = Task


class TagCreateView(CreateView):
    model = Tag


class TaskUpdateView(UpdateView):
    model = Task


class TagUpdateView(UpdateView):
    model = Tag


class TaskDeleteView(DeleteView):
    model = Task


class TagDeleteView(DeleteView):
    model = Tag