'''
from googletrans import Translator

def translate_to_korean(sentence):
    translator = Translator()
    detected = translator.detect(sentence)
    print(f"Detected language: {detected.lang}")
    
    result = translator.translate(sentence, dest='ko')
    return result.text

# 예시 사용
sentence = "음성변환텍스트파일"
translated_sentence = translate_to_korean(sentence)
print(translated_sentence)
'''
from deep_translator import GoogleTranslator

def translate_to_korean(sentence):
    translator = GoogleTranslator(source='auto', target='ko')
    translated_sentence = translator.translate(sentence)
    return translated_sentence