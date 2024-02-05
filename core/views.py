from django.http import HttpResponse, HttpResponseNotAllowed, Http404
from django.shortcuts import redirect, render, get_object_or_404

from core.forms import TaskForm
from core.models import Task


def task_detail(request, pk):
    task = get_object_or_404(Task, id=pk)
    context = {
        "task": task,
    }
    return render(request, "partials/task_detail.html", context)


def task_form(request):
    context = {
        "form": TaskForm()
    }
    return render(request, "partials/task_form.html", context)


def task_update(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("task-detail", pk=task.id)

    context = {
        "form": form,
        "task": task,
    }

    return render(request, "partials/task_form.html", context)

def taskset(request):
    # TODO! Break up this task!!
    # This function handles both creating and listing tasks, split it in two by those behaviors
    form = TaskForm(request.POST or None)
    context = {
        "form": form,
    }

    if request.method == "POST":
        if form.is_valid():
            task = form.save()
            return redirect("task-detail", pk=task.id)
        else:
            return render(request, "partials/task_form.html", context)

    context["tasks"] = Task.objects.all()  # TODO! Paginate in the future please
    return render(request, "tasks.html", context)


def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "POST":
        task.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def route_task_actions(request, *args, **kwargs):
    # TODO! WIP that still needs to be tested
    if request.method == "POST":
        pass

    pk = kwargs.get("pk")
    if request.method == "GET":
        return task_detail(request, pk)
    elif request.method == "PATCH":
        return task_update(request, pk)
    elif request.method == "DELETE":
        return task_delete(request, pk)
    else:
        raise Http404("Method Not Allowed")
