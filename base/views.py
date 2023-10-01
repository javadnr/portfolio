from django.shortcuts import render
from .models import Resume

def home(request):
    files = Resume.objects.all()
    return render(request,'home.html',{'files':files})


