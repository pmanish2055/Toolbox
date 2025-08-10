from django.shortcuts import render


def home (req):
    return render(req,'home.html')

def login (req):
    return render(req,'components/login.html')


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