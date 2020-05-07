from django.shortcuts import render , redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User , auth
from home.models import Blog



# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST["f-name"]
        last_name = request.POST["l-name"]
        email = request.POST["email"]
        username = request.POST["u-name"]
        password1 = request.POST["p1"]
        password2 = request.POST["p2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse('<h1>user exisits</h1>') 
            elif User.objects.filter(email=email).exists():
                return HttpResponse('<h1>user exisits</h1>')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user saved")
                return redirect('/accounts/login')
        else:
            return HttpResponse('<h1>password not matching</h1>')
       
    else:
        return render(request,"register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            
            return HttpResponse("<h1>INvalid</h1>")
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    
    d = Blog.objects.all()
    dicti = {'dests':d}
    return render(request,"profile.html",dicti)

    