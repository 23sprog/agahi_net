from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class CreationUserForm(forms.ModelForm):

    password1= forms.CharField(label="گذرواژه", widget=forms.PasswordInput)
    password2= forms.CharField(label="تایید گذرواژه", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "email",
            "username"
        ]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] and cd["password2"] and cd["password1"] == cd["password2"]:
            return cd["password2"]
        raise ValidationError("گذرواژه ها مطابقت ندارند")

    def clean_email(self):
        cd = self.cleaned_data
        email_exists = User.object.filter(email=cd["email"]).exists()
        if email_exists:
            raise ValidationError("این ایمیل قبلا در سایت ثبت نام شده است")
        return cd["email"]
    
    def clean_username(self):
        cd = self.cleaned_data
        username_exists = User.object.filter(username=cd["username"]).exists()
        if username_exists:
            raise ValidationError("این نام کاربری قبلا در سایت ثبت نام شده است")
        return cd["username"]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ChangeUserForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(help_text="you can change password using <a href=\"../password/\">this form</a>.")
    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name", "is_active", "is_admin", "courses")




class RegisterUserForm(forms.Form):
    email = forms.EmailField(max_length=255, label="ایمیل", widget=forms.TextInput({"class": "form-control"}))
    username = forms.CharField(max_length=255, label="نام کاربری", widget=forms.TextInput({"class": "form-control"}))
    password1 = forms.CharField(label="گذرواژه", widget=forms.PasswordInput({"class": "form-control"}))
    password2 = forms.CharField(label="تایید گذرواژه", widget=forms.PasswordInput({"class": "form-control"}))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] and cd["password2"] and cd["password1"] == cd["password2"]:
            return cd["password2"]
        raise ValidationError("گذرواژه ها مطابقت ندارند")

    def clean_email(self):
        cd = self.cleaned_data
        email_exists = User.object.filter(email=cd["email"]).exists()
        if email_exists:
            raise ValidationError("این ایمیل قبلا در سایت ثبت نام شده است")
        return cd["email"]

    def clean_username(self):
        cd = self.cleaned_data
        username_exists = User.object.filter(username=cd["username"]).exists()
        if username_exists:
            raise ValidationError("این نام کاربری قبلا در سایت ثبت نام شده است")
        return cd["username"]

class LoginUserForm(forms.Form):
    email = forms.EmailField(max_length=255, label="ایمیل", widget=forms.TextInput({"class": "form-control"}))
    password = forms.CharField(label="گذرواژه", widget=forms.PasswordInput({"class": "form-control"}))

class ProfileUserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(ProfileUserForm, self).__init__(*args, **kwargs)
        # if not user.is_admin:
        #     self.fields["is_company_admin"].disabled=True
    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name", )
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }
