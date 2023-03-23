from django.shortcuts import render

# Create your views here.
def edit_document(request):
    return render(request, 'editdocument.html')