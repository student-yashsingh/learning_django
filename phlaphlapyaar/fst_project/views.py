from django.shortcuts import render
from .models import ChaiVarity

# Create your views here.
def fst(request): 
    chais=ChaiVarity.objects.all()
    return render(request,'fst_project/fst.html',{'chais':chais})
