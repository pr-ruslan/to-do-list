from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, get_object_or_404


from .models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect(reverse("tasks:index"))


class TagListView(ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = "tags"


class TaskCreateView(CreateView):
    model = Task
    fields = ["content", "deadline", "is_completed", "tags"]
    success_url = "/"

class TagCreateView(CreateView):
    model = Tag
    fields = ["name"]
    success_url = "/tags/"


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["content", "deadline", "is_completed", "tags"]
    success_url = "/"

class TagUpdateView(UpdateView):
    model = Tag
    fields = ["name"]
    success_url = "/tags/"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/confirm_delete.html"
    success_url = reverse_lazy("tasks:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["name"] = self.object.content
        return context

class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tasks/confirm_delete.html"
    success_url = reverse_lazy("tasks:tag-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["name"] = self.object.name
        return context


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"

class TagDetailView(DetailView):
    model = Tag
    template_name = "tasks/tag_detail.html"
    context_object_name = "tag"
