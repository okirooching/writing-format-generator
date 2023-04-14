from django.urls import path
from . import views

urlpatterns = [
    path('', views.edit_document, name='edit_document'),
    path('save_paper', views.save_paper, name='save_paper')
]