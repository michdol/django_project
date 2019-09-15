from django import forms


class CreateUserForm(forms.Form):
    username = forms.CharField(
        min_length=8,
        max_length=150,
    )
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8,
        max_length=128,
        widget=forms.PasswordInput()
    )
