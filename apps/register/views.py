from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django import forms


class ExtendedRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True, help_text="Legal or preferred first name."
    )
    last_name = forms.CharField(
        max_length=30, required=True, help_text="Legal or preferred surname."
    )
    email = forms.EmailField(
        max_length=254, required=True, help_text="Secure comms channel."
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email")


def register_view(request):
    if request.method == "POST":
        form = ExtendedRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home:home")
    else:
        form = ExtendedRegistrationForm()
    return render(request, "register/register.html", {"form": form})
