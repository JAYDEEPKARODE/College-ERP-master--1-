from django.shortcuts import render,get_object_or_404
from info.models import Student

# Create your views here.
def fees(request,student_usn):
    student_data = get_object_or_404(Student, USN = student_usn)
    return render(request, 'fees.html',{'student_data': student_data})