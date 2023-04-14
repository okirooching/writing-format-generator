from django.shortcuts import render
from .models import title_page

import random

# Create your views here.
def edit_document(request):
    return render(request, 'editdocument.html')


def save_paper(request):
    if request.method == "POST":
        print("keynes")
        paper_id = random.uniform(0,1)
        student_name = request.POST["std_name"]
        professor_name= request.POST["prof_name"]
        faculty_department = request.POST["faculty"]
        course_id= request.POST["cos_id"]
        date=request.POST["date"]
        paper_title= request.POST["title"]
        print(student_name)
        a = title_page(
            student_name = student_name,
            paper_id = paper_id,
            professor_name = professor_name,
            faculty_department = faculty_department,
            course_id = course_id,
            date = date,
            paper_title = paper_title
        )
        a.save()
    return render(request, 'editdocument.html')