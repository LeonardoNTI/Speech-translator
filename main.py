

import googletrans
import playsound
import speech_recognition
import speech_recognition as sr 
import gtts

input_language = ""
target_language = ""

def translate_text(data):
    translator = googletrans.Translator()
    translate = translator.translate(data, dest=input_language)
    return translate.text

def program():
    recognizer = speech_recognition.Recognizer()
    with sr.Microphone() as source:
        print (translate_text("speak now"))
        voice = recognizer.listen(source)
        listen = recognizer.recognize_google(voice, language=input_language)
        print(listen)



    translator = googletrans.Translator()
    translate = translator.translate(listen, dest=target_language)
    print(translate.text)
    converted_audio = gtts.gTTS(translate.text, lang=target_language)
    converted_audio.save("hello.mp3")
    playsound.playsound("hello.mp3")

languages = ['af', "afrikaans", 'sq', 'albanian', 'am', 'amharic', 'ar', 'arabic', 'hy', 'armenian', 'az', 'azerbaijani', 'eu', 'basque', 'be', 'belarusian', 'bn', 'bengali', 'bs', 'bosnian', 'bg', 'bulgarian', 'ca', 'catalan', 'ceb', 'cebuano', 'ny', 'chichewa', 'zh-cn', 'chinese (simplified)', 'zh-tw', 'chinese (traditional)', 'co', 'corsican', 'hr', 'croatian', 'cs', 'czech', 'da', 'danish', 'nl', 'dutch', 'en', 'english', 'eo', 'esperanto', 'et', 'estonian', 'tl', 'filipino', 'fi', 'finnish', 'fr', 'french', 'fy', 'frisian', 'gl', 'galician', 'ka', 'georgian', 'de', 'german', 'el', 'greek', 'gu', 'gujarati', 'ht', 'haitian creole', 'ha', 'hausa', 'haw', 'hawaiian', 'iw', 'hebrew', 'he', 'hebrew', 'hi', 'hindi', 'hmn', 'hmong', 'hu', 'hungarian', 'is', 'icelandic', 'ig', 'igbo', 'id', 'indonesian', 'ga', 'irish', 'it', 'italian', 'ja', 'japanese', 'jw', 'javanese', 'kn', 'kannada', 'kk', 'kazakh', 'km', 'khmer', 'ko', 'korean', 'ku', 'kurdish (kurmanji)', 'ky', 'kyrgyz', 'lo', 'lao', 'la', 'latin', 'lv', 'latvian', 'lt', 'lithuanian', 'lb', 'luxembourgish', 'mk', 'macedonian', 'mg', 'malagasy', 'ms', 'malay', 'ml', 'malayalam', 'mt', 'maltese', 'mi', 'maori', 'mr', 'marathi', 'mn', 'mongolian', 'my', 'myanmar (burmese)', 'ne', 'nepali', 'no', 'norwegian', 'or', 'odia', 'ps', 'pashto', 'fa', 'persian', 'pl', 'polish', 'pt', 'portuguese', 'pa', 'punjabi', 'ro', 'romanian', 'ru', 'russian', 'sm', 'samoan', 'gd', 'scots gaelic', 'sr', 'serbian', 'st', 'sesotho', 'sn', 'shona', 'sd', 'sindhi', 'si', 'sinhala', 'sk', 'slovak', 'sl', 'slovenian', 'so', 'somali', 'es', 'spanish', 'su', 'sundanese', 'sw', 'swahili', 'sv', 'swedish', 'tg', 'tajik', 'ta', 'tamil', 'te', 'telugu', 'th', 'thai', 'tr', 'turkish', 'uk', 'ukrainian', 'ur', 'urdu', 'ug', 'uyghur', 'uz', 'uzbek', 'vi', 'vietnamese', 'cy', 'welsh', 'xh', 'xhosa', 'yi', 'yiddish', 'yo', 'yoruba', 'zu', 'zulu']

def get_input_language(list_of_languages):

    global input_language
    req_input_language = input("Please select the language you want to translate from: ")

    if req_input_language in list_of_languages:
        language_to_index = list_of_languages.index(req_input_language) 
        input_language = (list_of_languages[language_to_index - 1])
        return input_language
    else:
        print(f"We do not support {req_input_language}, please try again")
        get_input_language(languages)
        

def get_target_language(list_of_languages):
    global target_language
    req_target_language = input("Please select the language you want to translate to: ")

    if req_target_language in list_of_languages:
        language_to_index = list_of_languages.index(req_target_language) 
        target_language = (list_of_languages[language_to_index - 1])
        return target_language
    else:
        print(f"We do not support {req_target_language}, please try again")
        get_target_language(languages)


print ("Hello and welcome to the speech translator.")
get_target_language(languages)
get_input_language(languages)
program()
