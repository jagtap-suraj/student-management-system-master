from django.db import models

# Create your models here.
class Student(models.Model):

  Branch_Choices = (
    ('Computer Engineering', 'Computer Engineering'),
    ('Information Technology', 'Information Technology'),
    ('ExTC', 'ExTC'),
    ('ECS', 'ECS'),
    ('Cyber Security', 'Cyber Security'),
    ('AI-DS', 'AI-DS'),
  )

  Sem_Choices = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
  )

  Division_Choices = (
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11),
    (12, 12),
  )

  student_number = models.PositiveIntegerField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  branch = models.CharField(max_length=50, choices=Branch_Choices, default='Computer Engineering')
  sem = models.PositiveIntegerField(choices=Sem_Choices, default=1)
  division = models.PositiveIntegerField(choices=Division_Choices, default=3)
  gpa = models.FloatField()
  kt = models.PositiveIntegerField(default=0)

  def __str__(self):
    return f'Student: {self.first_name} {self.last_name}'
