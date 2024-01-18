

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


def get_input_language():
    global input_language
    req_input_language = input("Please select the language you want to translate from: ")


    if req_input_language == "italian" or req_input_language == "Italian" or req_input_language == "it":
         input_language = "it"
    elif req_input_language == "swedish" or req_input_language == "Swedish" or req_input_language == "sv":
         input_language = "sv"
    elif req_input_language == "english" or req_input_language == "English" or req_input_language == "en":
         input_language = "en"
    else:
        print(f"We do not support {req_input_language}, please try again")
        get_input_language()

    return input_language

def get_target_language():
    global target_language
    req_target_language = input("please select the language you want to translate to: ")

    if req_target_language == "italian" or req_target_language == "Italian" or req_target_language == "it":
         target_language = "it"
    elif req_target_language == "swedish" or req_target_language == "Swedish" or req_target_language == "sv":
         target_language = "sv"
    elif req_target_language == "english" or req_target_language == "English" or req_target_language == "en":
         target_language = "en"
    else:
        print(f"We do not support {req_target_language}, please try again)")
        get_target_language()

    return target_language


print ("Hello and welcome to the speech translator.")
get_target_language()
get_input_language()
program()