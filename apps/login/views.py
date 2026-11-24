from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import EmailAuthenticationForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home:home")

    if request.method == "POST":
        form = EmailAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home:home")
    else:
        form = EmailAuthenticationForm()
    return render(request, "login/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login:login")
