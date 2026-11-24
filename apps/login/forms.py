from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class EmailAuthenticationForm(forms.Form):
    email = forms.CharField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "operator@ascend.os",
                "autocomplete": "email",
                "autofocus": True,
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "••••••••••••",
                "autocomplete": "current-password",
            }
        ),
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email_or_user = self.cleaned_data.get("email", "").strip()
        password = self.cleaned_data.get("password")

        if email_or_user and password:
            # Lookup user by email (case-insensitive)
            user_obj = User.objects.filter(email__iexact=email_or_user).first()
            if not user_obj:
                # Fallback to username for flexibility
                user_obj = User.objects.filter(username__iexact=email_or_user).first()

            if user_obj:
                self.user_cache = authenticate(
                    self.request, username=user_obj.username, password=password
                )

            if self.user_cache is None:
                raise forms.ValidationError(
                    "Invalid email or security passkey. Clearance denied."
                )
            elif not self.user_cache.is_active:
                raise forms.ValidationError("Clearance revoked: Account inactive.")

        return self.cleaned_data

    def get_user(self):
        return self.user_cache
