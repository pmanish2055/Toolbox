from django.urls import path

from alltools.views import wordcount,texttranslation,texttospeech

urlpatterns = [
    path('wordcount', wordcount, name='wordcount'),
    path('texttranslation', texttranslation, name='texttranslation'),
    path('texttospeech', texttospeech, name='texttospeech'),


  
]
 