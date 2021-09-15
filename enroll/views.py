from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import User
from .forms import UserRegistration

# def index(request):
#     stud=User.objects.all()
#     return render(request,'enroll/addandshow.html',{'stu':stud})


def show_data(request):

    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            # return index(request)
            # return redirect('/data')
            # stud = User.objects.all()
            # fm = UserRegistration()
            # return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

    else:
        fm = UserRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud })


def delete(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=UserRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = UserRegistration(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})
