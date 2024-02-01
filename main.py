

import googletrans
import playsound
import speech_recognition
import speech_recognition as sr 
import gtts

input_language = ""
target_language = ""
languages = ['af', "afrikaans", 'sq', 'albanian', 'am', 'amharic', 'ar', 'arabic', 'hy', 'armenian', 'az', 'azerbaijani', 'eu', 'basque', 'be', 'belarusian', 'bn', 'bengali', 'bs', 'bosnian', 'bg', 'bulgarian', 'ca', 'catalan', 'ceb', 'cebuano', 'ny', 'chichewa', 'zh-cn', 'chinese', 'zh-tw', 'chinese (traditional)', 'co', 'corsican', 'hr', 'croatian', 'cs', 'czech', 'da', 'danish', 'nl', 'dutch', 'en', 'english', 'eo', 'esperanto', 'et', 'estonian', 'tl', 'filipino', 'fi', 'finnish', 'fr', 'french', 'fy', 'frisian', 'gl', 'galician', 'ka', 'georgian', 'de', 'german', 'el', 'greek', 'gu', 'gujarati', 'ht', 'haitian creole', 'ha', 'hausa', 'haw', 'hawaiian', 'iw', 'hebrew', 'he', 'hebrew', 'hi', 'hindi', 'hmn', 'hmong', 'hu', 'hungarian', 'is', 'icelandic', 'ig', 'igbo', 'id', 'indonesian', 'ga', 'irish', 'it', 'italian', 'ja', 'japanese', 'jw', 'javanese', 'kn', 'kannada', 'kk', 'kazakh', 'km', 'khmer', 'ko', 'korean', 'ku', 'kurdish (kurmanji)', 'ky', 'kyrgyz', 'lo', 'lao', 'la', 'latin', 'lv', 'latvian', 'lt', 'lithuanian', 'lb', 'luxembourgish', 'mk', 'macedonian', 'mg', 'malagasy', 'ms', 'malay', 'ml', 'malayalam', 'mt', 'maltese', 'mi', 'maori', 'mr', 'marathi', 'mn', 'mongolian', 'my', 'myanmar (burmese)', 'ne', 'nepali', 'no', 'norwegian', 'or', 'odia', 'ps', 'pashto', 'fa', 'persian', 'pl', 'polish', 'pt', 'portuguese', 'pa', 'punjabi', 'ro', 'romanian', 'ru', 'russian', 'sm', 'samoan', 'gd', 'scots gaelic', 'sr', 'serbian', 'st', 'sesotho', 'sn', 'shona', 'sd', 'sindhi', 'si', 'sinhala', 'sk', 'slovak', 'sl', 'slovenian', 'so', 'somali', 'es', 'spanish', 'su', 'sundanese', 'sw', 'swahili', 'sv', 'swedish', 'tg', 'tajik', 'ta', 'tamil', 'te', 'telugu', 'th', 'thai', 'tr', 'turkish', 'uk', 'ukrainian', 'ur', 'urdu', 'ug', 'uyghur', 'uz', 'uzbek', 'vi', 'vietnamese', 'cy', 'welsh', 'xh', 'xhosa', 'yi', 'yiddish', 'yo', 'yoruba', 'zu', 'zulu']

def choose_program():
    desired_program = input("Are you able to speak? (Yes/No): \n")
    if desired_program == "yes" or desired_program == "Yes" :
        spoken_program()
    elif desired_program == "no" or desired_program == "No":
        return (written_program())


def speech_to_text():
    recognizer = speech_recognition.Recognizer()
    with sr.Microphone() as source:
        voice = recognizer.listen(source)
        listen = recognizer.recognize_google(voice, language= "en")
        print(listen)
        return listen.lower()

def translate_text(data):
    translator = googletrans.Translator()
    translate = translator.translate(data, dest=input_language)
    return translate.text

def written_program():
    get_written_target_language(languages)

    data = input("write now please: \n")
    translator = googletrans.Translator()
    translate = translator.translate(data,dest=target_language)
    return(translate.text)


def get_written_target_language(list_of_languages):

    global target_language
    req_target_language = input("Please write the language you want to translate to: \n")

    if req_target_language in list_of_languages:
        language_to_index = list_of_languages.index(req_target_language) 
        target_language = (list_of_languages[language_to_index - 1])
        return target_language
    else:
        print(f"We do not support {req_target_language}, please try again")
        get_written_target_language(languages)

def spoken_program():
    get_target_language(languages)
    get_input_language(languages)

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

def get_input_language(list_of_languages):

    global input_language
    print("Please say the language you want to translate from: ")

    req_input_language = speech_to_text()

    if req_input_language in list_of_languages:
        language_to_index = list_of_languages.index(req_input_language) 
        input_language = (list_of_languages[language_to_index - 1])
        return input_language
    else:
        print(f"We do not support {req_input_language}, please try again")
        get_input_language(languages)
        

def get_target_language(list_of_languages):
    global target_language
    print("Please say the language you want to translate to: ")

    req_target_language = speech_to_text()

    if req_target_language in list_of_languages:
        language_to_index = list_of_languages.index(req_target_language) 
        target_language = (list_of_languages[language_to_index - 1])
        return target_language
    else:
        print(f"We do not support {req_target_language}, please try again")
        get_target_language(languages)


print ("Hello and welcome to the speech translator.")
print (choose_program())

