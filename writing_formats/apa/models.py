from django.db import models

# Create your models here.
class title_page(models.Model):
    student_name = models.CharField(max_length=20, default="key")
    paper_id = models.FloatField(null=False, default=0.01, primary_key=True)
    professor_name= models.CharField(max_length=30)
    faculty_department = models.CharField(max_length=30)
    course_id= models.CharField(max_length=70)
    date= models.CharField(max_length=20)
    paper_title= models.CharField(max_length=50)
