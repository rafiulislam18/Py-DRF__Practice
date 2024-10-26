from django.db import models
from students.models import Student


# Define Grade model
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.student.first_name} - {self.subject} - {self.score}"
