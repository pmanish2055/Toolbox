import re
from deep_translator import GoogleTranslator


def wordcount_function (text):
    wordcount=len(text.split())
    charactercount=len(text)
    sentencecount=text.count('.')+text.count('!') + text.count('?')

    # Split on any sequence of blank lines (with optional whitespace)
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n+', text.strip()) if p.strip()]
    paragraphcount = len(paragraphs)

    return {
        'word_count':wordcount,
        'character_count':charactercount,
        'sentence_count':sentencecount,
        'paragraph_count':paragraphcount
    }


def texttranslator_function(text, source_lang,target_lang):
    try:
        translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return {
          'translated_text':translated_text
        }
    except Exception as e:
        return {'translated_text': f"Error in translating: {str(e)}"}
