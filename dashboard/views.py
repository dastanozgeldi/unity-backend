from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Student, Distraction


def index(request):
    return JsonResponse({"message": "Hello, world. You're at the dashboard index."})


def get_students(request):
    # return all students as jsonresponse
    return JsonResponse({"students": list(Student.objects.values())})


@csrf_exempt
def add_student(request):
    # get name parameter from request, check for post request
    name = request.GET.get("name")
    if request.method == "POST":
        student = Student.objects.create(name=name)
        data = {
            "id": student.id,
            "name": student.name,
            "distractions": [],
        }
        return JsonResponse({"message": data})
    else:
        # wrong request method error
        return JsonResponse({"message": "Wrong request method."})


def get_distractions(request):
    # return name parameter from request as jsonresponse
    name = request.GET.get("name")
    student = Student.objects.get(name=name)
    return JsonResponse({"distractions": list(student.distractions.values())})


@csrf_exempt
def add_distraction(request):
    # get student by name parameter from request, create distraction with student and current datetime, check for post request
    name = request.GET.get("name")
    student = Student.objects.get(name=name)
    if request.method == "POST":
        distraction = Distraction.objects.create(student=student, time=datetime.now())
        data = {
            "id": distraction.id,
            "student": distraction.student.name,
            "time": distraction.time,
        }
        return JsonResponse({"message": data})
    else:
        # wrong request method error
        return JsonResponse({"message": "Wrong request method."})
