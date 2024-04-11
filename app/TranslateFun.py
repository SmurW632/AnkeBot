from googletrans import Translator

async def Translation(text, language):

    translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])
    
    translated  = await translator.translate(text,dest = language)

    return translated.text