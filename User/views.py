from django.shortcuts import render, HttpResponse, redirect
from .models import Peoples


# Create your views here.

def loginpage(request):
    return render(request,"login2.html")

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        person = Peoples.objects.get(email=email)
        
        msg = ""
        if not person:
            msg = "Users not registered"
        else:
            if person.password == password:
                request.session['user_id'] = person.user_id
                request.session['name'] = person.name
                request.session['email'] = person.email
                request.session['profile'] = person.profile_pic.url
                # return index(request)
                return redirect("mainhome")
            else:
                msg = "Password is Incorrect"
        return render(request,"login2.html", {'msg' : msg})


def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        profile_pic = request.POST['profile']
        obj = Peoples(name=name, email=email, password=password, profile_pic=profile_pic)
        obj.save()
    return render(request,"login2.html")

def logout(request):
    del request.session['user_id']
    del request.session['name']
    del request.session['email']
    del request.session['profile']
    return redirect("mainhome")