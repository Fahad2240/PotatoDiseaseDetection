from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
def index(request):
    return render(request,'Detection\index.html')
def add_pic(request):
    if request.method=='POST':
        form=Selectpic(request.POST,request.FILES)
        if form.is_valid():
            Image=form.save(commit=True)
    else:
        form=Selectpic()
    return render(request,'Detection\input.html',{'form':form})

