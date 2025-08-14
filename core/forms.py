from django import forms

class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'required': True
    })
    )
    password= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'required': True
    }))
