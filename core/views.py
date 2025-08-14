from django.shortcuts import render ,redirect
from .forms import LoginForm

def home (req):
    return render(req,'home.html')


def login(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            print(email, password)
            return redirect(home)
    else:
        form = LoginForm()
    
    return render(req, 'components/login.html', {'form': form})



def signup (req):
    return render(req,'components/signup.html')

def imagetool (req):
    return render(req,'components/imagetool.html')

def texttool (req):
    return render(req,'components/texttool.html') 

def mathtool (req):
    return render(req,'components/mathtool.html') 

def webtool (req):
    return render(req,'components/webtool.html') 

def codeutilitiestool (req):
    return render(req,'components/codeutilitiestool.html') 

def misctool (req):
    return render(req,'components/misctool.html') 