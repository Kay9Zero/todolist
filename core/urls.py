from django.urls import path

from core.views import task_detail, task_delete, task_form, task_update, taskset

urlpatterns = [
    path('htmx/task-form/', task_form, name='task-form'),
    # TODO! Reduce these routes into a single url path and utilize HTTP methods
    #       and then resolve each of these to a function that routes to their respective function (route_task_actions)
    #       (or switch to Django REST Framework)
    path('htmx/task/<pk>/', task_detail, name="task-detail"),
    path('htmx/task/<pk>/update/', task_update, name="task-update"),
    path('htmx/task/<pk>/delete/', task_delete, name="task-delete"),
    path('', taskset, name='tasks'),
]