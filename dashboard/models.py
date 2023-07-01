from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Distraction(models.Model):
    time = models.DateTimeField(auto_now_add=False)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="distractions"
    )

    def __str__(self):
        return f"{self.student} at {self.time}"
