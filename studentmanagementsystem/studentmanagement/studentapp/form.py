from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['roll_number','first_name','last_name','email','field_of_study','gpa']

        
        widgets={
            'roll_number':forms.NumberInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'field_of_study':forms.TextInput(attrs={'class':'form-control'}),
            'gpa':forms.NumberInput(attrs={'class':'form-control'})
        }