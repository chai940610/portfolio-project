from django.shortcuts import render
from .models import Job1
def home(request):
    job3 =Job1.objects
    return render(request,'job2/home.html',{'job3':job3})
# Create your views here.
