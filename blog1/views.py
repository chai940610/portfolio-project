from django.shortcuts import render, get_object_or_404
from .models import blog2
def house(request):
    supermax=blog2.objects
    return render(request,'blog1/niceblog.html',{'supermaxs':supermax})
def detail(request, mom_id):
    detailblog=get_object_or_404(blog2,pk=mom_id)
    return render(request,'blog1/detail.html',{'blog':detailblog})
# Create your views here.
