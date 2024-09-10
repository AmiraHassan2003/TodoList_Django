from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name='home'),
    path("addTask", views.add_task, name='add_task'),
    path("mark_as_completed/<int:task_id>/", views.mark_as_completed, name="mark_as_completed"),
    path("delete_task/<int:task_id>/", views.delete_task, name = "delete_task"),
    path("delete_all_tasks/", views.delete_all_tasks, name = "delete_all_tasks"),
    path("incomplete_task/", views.incomplete_task, name = "incomplete_task"),
    path("complete_task/", views.complete_task, name = "complete_task"),
    path("see_all_tasks/", views.see_all_tasks, name = "see_all_tasks"),

]