from django.shortcuts import render,redirect
from .forms import EmpForm
from . models import Student
# Create your views here.
#this code make form html
def index(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmpForm()
    return render(request,'index.html',{'forms':form})


# this code show database data

def show(request):
    form = Student.objects.all()
    return render(request,'show.html',{'vijay':form})

# this code used to delete the data
def delete(request,id):
    form = Student.objects.get(id=id)
    form.delete()
    return redirect('/show')

# this code used to update date
'''def update(request,id):
    form = Student.objects.get(pk=id)
    return render(request,"update.html",{'vijay':form})'''
def update(request,id):
    if request.method == 'POST':
        pi=Student.objects.get(pk=id)
        fm= EmpForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/show')
    else:
        pi = Student.objects.get(pk=id)
        fm = EmpForm(instance=pi)
    return render(request,'update.html',{'form':fm})
