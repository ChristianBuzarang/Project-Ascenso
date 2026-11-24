from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Patient, Professional, ProfessionalAssignment



@login_required(login_url="login:login")
def profile_view(request):
    # Fetch or create the profile for the logged-in user
    profile, created = Profile.objects.get_or_create(user=request.user)
    if not request.user.role:
        request.user.role = "Patient"
        request.user.save(update_fields=["role"])

    if request.method == "POST":
        # Save Role directly on the User (auth_user table in Supabase)
        designation = request.POST.get("designation", "").strip()
        if designation in ("Patient", "Professional"):
            request.user.role = designation
            request.user.save(update_fields=["role"])

            # Sync related role records in Supabase
            if designation == "Patient":
                Patient.objects.get_or_create(user=request.user)
                Professional.objects.filter(user=request.user).delete()
            elif designation == "Professional":
                specialty_input = request.POST.get("specialty", "").strip()
                license_input = request.POST.get("license_number", "").strip()
                prof, _ = Professional.objects.get_or_create(
                    user=request.user,
                    defaults={
                        "specialty": specialty_input or "Doctor / Psychiatrist",
                        "license_number": license_input or f"PRO-{request.user.id:04d}",
                    },
                )
                if specialty_input:
                    prof.specialty = specialty_input
                if license_input:
                    prof.license_number = license_input
                prof.save()
                Patient.objects.filter(user=request.user).delete()



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

    professional = Professional.objects.filter(user=request.user).first()
    return render(
        request,
        "user_profile/profile.html",
        {"profile": profile, "professional": professional},
    )



@login_required(login_url="login:login")
def connect_view(request):
    """
    Patient-to-Professional Connection View:
    - Resolves the current user's Patient record.
    - Loads verified Professional records (Doctors / Therapists).
    - Handles POST requests to connect or update ProfessionalAssignment without duplicates.
    - Passes existing assignments, available professionals, and status context to the template.
    """
    profile, _ = Profile.objects.get_or_create(user=request.user)

    # If the user is a Professional, redirect to the professional assignment roster
    if request.user.is_professional:
        return redirect("user_profile:assignment")


    # Resolve or create Patient record for the current user
    patient, _ = Patient.objects.get_or_create(user=request.user)

    if request.method == "POST":
        action = request.POST.get("action", "connect").strip()

        if action in ("disconnect", "terminate"):
            assignment_id = request.POST.get("assignment_id")
            assignment = get_object_or_404(
                ProfessionalAssignment, id=assignment_id, patient=patient
            )
            assignment.status = "Inactive"
            assignment.save()
            messages.info(
                request,
                f"Neural connection link with {assignment.professional} has been deactivated.",
            )
            return redirect("user_profile:connect")

        elif action == "reconnect":
            assignment_id = request.POST.get("assignment_id")
            assignment = get_object_or_404(
                ProfessionalAssignment, id=assignment_id, patient=patient
            )
            assignment.status = "Active"
            assignment.save()
            messages.success(
                request,
                f"Connection link with {assignment.professional} re-established.",
            )
            return redirect("user_profile:connect")

        else:
            # Default connect action
            professional_id = request.POST.get("professional_id")
            if not professional_id:
                messages.error(request, "Please select a valid professional specialist.")
                return redirect("user_profile:connect")

            professional = get_object_or_404(Professional, id=professional_id)

            # Prevent self-assignment if the account holds both records
            if professional.user == request.user:
                messages.error(request, "Self-assignment is not permitted.")
                return redirect("user_profile:connect")

            # Check if assignment already exists
            assignment = ProfessionalAssignment.objects.filter(
                patient=patient, professional=professional
            ).first()

            if assignment:
                if assignment.status == "Active":
                    messages.info(
                        request,
                        f"Active neural link with {professional} is already in place.",
                    )
                else:
                    assignment.status = "Active"
                    assignment.save()
                    messages.success(
                        request,
                        f"Connection link with {professional} reactivated.",
                    )
            else:
                ProfessionalAssignment.objects.create(
                    patient=patient,
                    professional=professional,
                    status="Active",
                )
                messages.success(
                    request,
                    f"Successfully established neural link with {professional}.",
                )

            return redirect("user_profile:connect")

    # Fetch available professionals
    available_professionals = (
        Professional.objects.exclude(user=request.user)
        .select_related("user", "user__profile")
        .order_by("user__last_name", "user__first_name")
    )

    # Fetch existing assignments for this patient
    existing_assignments = (
        ProfessionalAssignment.objects.filter(patient=patient)
        .select_related("professional", "professional__user", "professional__user__profile")
        .order_by("-assigned_date")
    )

    # Collect set of active professional IDs for badge highlighting
    active_professional_ids = set(
        existing_assignments.filter(status="Active").values_list("professional_id", flat=True)
    )

    context = {
        "profile": profile,
        "patient": patient,
        "available_professionals": available_professionals,
        "existing_assignments": existing_assignments,
        "active_professional_ids": active_professional_ids,
    }
    return render(request, "user_profile/connect.html", context)


@login_required(login_url="login:login")
def assignment_view(request):
    """
    Professional Patient Roster View:
    - Visible to Doctors and Therapists.
    - Shows all assigned patients and their status.
    - Allows professionals to update assignment status.
    """
    profile, _ = Profile.objects.get_or_create(user=request.user)

    # If the user is a patient, redirect them to the connect view
    if not request.user.is_professional:
        return redirect("user_profile:connect")

    # Resolve or create professional record
    professional, _ = Professional.objects.get_or_create(
        user=request.user,
        defaults={
            "specialty": "Doctor / Psychiatrist",
            "license_number": f"PRO-{request.user.id:04d}",
        },
    )


    if request.method == "POST":
        action = request.POST.get("action", "").strip()
        assignment_id = request.POST.get("assignment_id")
        new_status = request.POST.get("status", "").strip()

        assignment = get_object_or_404(
            ProfessionalAssignment, id=assignment_id, professional=professional
        )

        if action == "update_status" and new_status in ("Active", "Completed", "Inactive", "Pending"):
            assignment.status = new_status
            assignment.save()
            messages.success(
                request,
                f"Status for patient {assignment.patient.user.get_full_name() or assignment.patient.user.username} updated to {new_status}.",
            )
        elif action == "remove":
            assignment.status = "Inactive"
            assignment.save()
            messages.info(
                request,
                f"Patient {assignment.patient.user.get_full_name() or assignment.patient.user.username} marked as Inactive.",
            )

        return redirect("user_profile:assignment")

    assigned_patients = (
        ProfessionalAssignment.objects.filter(professional=professional)
        .select_related("patient", "patient__user", "patient__user__profile")
        .order_by("-assigned_date")
    )

    context = {
        "profile": profile,
        "professional": professional,
        "assigned_patients": assigned_patients,
    }
    return render(request, "user_profile/assignment.html", context)

