from django.shortcuts import render,redirect
from .models import Student
from .form import StudentForm
def index(request):
    return render(request,"students/index.html",{
        "students":Student.objects.all()
        })

def viewstudent(request,id):
    student=Student.objects.get(pk=id)
    return redirect("index")

def add(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        print(form)
        if form.is_valid():
            new_student_roll=form.cleaned_data['roll_number']
            new_student_first_name=form.cleaned_data['first_name']
            new_student_last_name=form.cleaned_data['last_name']
            new_student_email=form.cleaned_data['email']
            new_student_field=form.cleaned_data['field_of_study']
            new_gpa=form.cleaned_data['gpa']

            new_student=Student(
                roll_number=new_student_roll,
                first_name=new_student_first_name,
                last_name=new_student_last_name,
                email=new_student_email,
                field_of_study=new_student_field,
                gpa=new_gpa
            )
            new_student.save()
            return render(request,'students/add.html',{'form':StudentForm(),"success":True})
    else:
        form=StudentForm()
    return render(request,'students/add.html',{'form':StudentForm()})

def edit(request,id):
    if request.method=='POST':
        student=Student.objects.get(pk=id)
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return render(request,'students/edit.html',{'form':form,'success':True})
    else:
        student=Student.objects.get(pk=id)
        form=StudentForm(instance=student)
    return render(request,'students/edit.html',{"form":form})

def delete(request,id):
    if request.method=='POST':
        student=Student.objects.get(pk=id)
        student.delete()
    return redirect('index')




# Create your views here.
