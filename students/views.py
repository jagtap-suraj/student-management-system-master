from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm
from django.db.models import Q

# Create your views here.
def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })

def view_student(request, id):
  student = Student.objects.get(pk=id)
  return HttpResponseRedirect(reverse('index'))

def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_branch = form.cleaned_data['branch']
      new_sem = form.cleaned_data['sem']
      new_division = form.cleaned_data['division']
      new_gpa = form.cleaned_data['gpa']
      new_kt = form.cleaned_data['kt']

      new_student = Student(
        student_number = new_student_number,
        first_name = new_first_name,
        last_name = new_last_name,
        email = new_email,
        branch = new_branch,
        sem = new_sem,
        division = new_division,
        gpa = new_gpa,
        kt = new_kt
      )
      new_student.save()
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })

def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })

def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))

def search(request):
    query = request.GET.get('search_query')
    students = Student.objects.filter(
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query) |
        Q(student_number__icontains=query)
    )
    return render(request, 'students/index.html', {'students': students})

def index(request):
  sort_by = request.GET.get('sort_by')
  if sort_by:
    students = Student.objects.order_by(sort_by)
  else:
    students = Student.objects.all()
  return render(request, 'students/index.html', {
    'students': students
  })
