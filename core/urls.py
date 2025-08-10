from django.urls import path
from core.views import home,imagetool,texttool,mathtool,webtool,codeutilitiestool,misctool,login,signup


urlpatterns = [
    path('', home, name='home'),
    path('login',login, name='login'),
    path('signup',signup, name='signup'),
    path('imagetool', imagetool , name='imagetool'),
    path('texttool', texttool , name='texttool'),
    path('mathtool',mathtool , name= 'mathtool'),
    path('webtool',webtool , name= 'webtool'),
    path('codeutilitiestool',codeutilitiestool , name= 'codeutilitiestool'),
    path('misctool',misctool, name='misctool'),


]
