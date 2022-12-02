from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def login_request(request):
    if request.user.is_authenticated:
        return redirect("products")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next',None)
            if next_url is None:
                messages.success(request, "Login başarılı")
                return redirect("products")
            else:
                return redirect(next_url)
        else:
            messages.error(request, "Kullanıcı adı veya parola yanlış." )
            return render(request, "account/login.html" )
    else:
        return render(request, "account/login.html")


def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", {"error": "Username kullanılıyor."})
            else:
                if User.objects.filter(email = email).exists():
                    return render(request, "account/register.html", {"error": "Email kullanılıyor."})
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect("login")
        else:
            return render(request, "account/register.html", {"error": "Parola eşleşmiyor."})
    else:
        return render(request, "account/register.html")


def logout_request(request):
    logout(request)
    return redirect("products")
