from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'branch', 'sem', 'division', 'kt', 'gpa']
        labels = {
            'student_number': 'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'branch': 'Branch',
            'sem': 'Sem',
            'division': 'Division',
            'kt': 'KT',
            'gpa': 'GPA',
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'sem': forms.Select(attrs={'class': 'form-control'}),
            'division': forms.Select(attrs={'class': 'form-control'}),
            'kt': forms.NumberInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        kt = cleaned_data.get('kt')
        gpa = cleaned_data.get('gpa')
        if kt and kt > 0 and gpa:
            raise forms.ValidationError('CGPA cannot be entered when number of KT is greater than 0')
        elif kt and kt > 0:
            cleaned_data['gpa'] = 0
        return cleaned_data
