from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile


@login_required(login_url="login:login")
def profile_view(request):
    # Fetch or create the profile for the logged-in user
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile.full_name = request.POST.get("full_name", "")
        profile.bio = request.POST.get("bio", "")

        # Handle Profile Picture Uploads
        if "profile_image" in request.FILES:
            profile.profile_image = request.FILES["profile_image"]

        profile.save()
        messages.success(request, "Agent Identity Successfully Updated")
        return redirect("user_profile:profile")

    return render(request, "user_profile/profile.html", {"profile": profile})
