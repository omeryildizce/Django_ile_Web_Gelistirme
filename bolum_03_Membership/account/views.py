from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_request(request):
    if request.user.is_authenticated:
        return redirect("products")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            return redirect("products")
        else:
            return render(request, "account/login.html", {
                "error":"kullanıcı adı veya parola yanlış."
            })
    else:
        return render(request, "account/login.html")

def register_request(request):
    if request.method == "POST":
        #login
        pass
    else:
        return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("products")