from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_students/", views.get_students, name="get_students"),
    path("add_student/", views.add_student, name="add_student"),
    path("get_distractions/", views.get_distractions, name="get_distractions"),
    path("add_distraction/", views.add_distraction, name="add_distraction"),
]
