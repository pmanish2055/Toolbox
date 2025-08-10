from django.shortcuts import render
from .utils.textttols import wordcount_function ,texttranslator_function

def wordcount (req):
    if req.method == 'POST':
        context={}
        # Get the text from the textarea
        text = req.POST.get('text_to_count', '')
        count= wordcount_function(text)
        context.update(count)
        context['original_text']=text
        return render(req, 'components/texttools/wordcount.html', context)
    
    # If it's a GET req, just show the empty form
    return render(req, 'components/texttools/wordcount.html')

def texttranslation(req):
    if req.method=='POST':
        context={}
         # Get the text from the textarea
        languagefrom = req.POST.get('from_language', '')
        languageto = req.POST.get('to_language', '')

        fromtxt = req.POST.get('text_input', '')

        translate=texttranslator_function(fromtxt ,languagefrom,languageto)
        context.update(translate)
        context['original_text']=fromtxt
   
        return render(req, 'components/texttools/texttranslation.html', context)
    
    # If it's a GET req, just show the empty form
    return render(req, 'components/texttools/texttranslation.html')

def texttospeech(req):
    return render(req,'components/texttools/texttospeech.html')