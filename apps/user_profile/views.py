from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Patient, Professional


@login_required(login_url="login:login")
def profile_view(request):
    # Fetch or create the profile for the logged-in user
    profile, created = Profile.objects.get_or_create(user=request.user)
    if not profile.designation:
        profile.designation = "Patient"
        profile.role = "Patient"
        profile.save()

    if request.method == "POST":
        # Save Designation / Role
        designation = request.POST.get("designation", "").strip()
        if designation in ("Patient", "Doctor", "Therapist"):
            profile.designation = designation
            profile.role = designation

            # Sync related role records in Supabase
            if designation == "Patient":
                Patient.objects.get_or_create(user=request.user)
            elif designation in ("Doctor", "Therapist"):
                Professional.objects.get_or_create(
                    user=request.user,
                    defaults={
                        "specialty": designation,
                        "license_number": f"{designation[:3].upper()}-{request.user.id:04d}",
                    },
                )

        # Save Name if supplied
        full_name = request.POST.get("full_name", "").strip()
        if full_name:
            parts = full_name.split(None, 1)
            request.user.first_name = parts[0]
            request.user.last_name = parts[1] if len(parts) > 1 else ""
            request.user.save()

        profile.bio = request.POST.get("bio", "")

        # Handle Profile Picture Uploads
        if "profile_image" in request.FILES:
            profile.image = request.FILES["profile_image"]

        profile.save()
        messages.success(request, "Agent Identity Successfully Updated")
        return redirect("user_profile:profile")

    return render(request, "user_profile/profile.html", {"profile": profile})
