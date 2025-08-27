from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Task, Tag

def index(request):
    return render(request, 'tasks/index.html')


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"


class TagListView(ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = "tags"


class TaskCreateView(CreateView):
    model = Task
    fields = ["content", "deadline", "is_completed", "tags"]
    success_url = "/tasks/"

class TagCreateView(CreateView):
    model = Tag
    fields = ["name"]
    success_url = "/tags/"


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["content", "deadline", "is_completed", "tags"]
    success_url = "/tasks/"

class TagUpdateView(UpdateView):
    model = Tag
    fields = ["name"]
    success_url = "/tags/"


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tag-list")


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"

class TagDetailView(DetailView):
    model = Tag
    template_name = "tasks/tag_detail.html"
    context_object_name = "tag"
