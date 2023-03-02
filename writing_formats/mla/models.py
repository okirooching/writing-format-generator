from django.db import models

# Create your models here.
class title_page(models.Model):
    paper_id: models.IntegerField()
    professor_name: models.CharField(max_length=30)
    course_id: models.CharField(max_length=70)
    date: models.CharField(max_length=20)
    paper_title: models.CharField(max_length=50)