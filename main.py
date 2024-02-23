import googletrans  # Importera bibliotek för översättning
import playsound    # Importera bibliotek för att spela ljud
import speech_recognition  # Importera bibliotek för taligenkänning
import speech_recognition as sr  # För att använda sr.Microphone
import gtts # Importera gtts-bibliotek för att konvertera text till tal


input_language = ""   # Variabel för indatatspråk
target_language = ""  # Variabel för målspråk

# Lista över tillgängliga språkkoder för översättning
languages = ['af', "afrikaans", 'sq', 'albanian', 'am', 'amharic', 'ar', 'arabic', 'hy', 'armenian', 'az', 'azerbaijani', 'eu', 'basque', 'be', 'belarusian', 'bn', 'bengali', 'bs', 'bosnian', 'bg', 'bulgarian', 'ca', 'catalan', 'ceb', 'cebuano', 'ny', 'chichewa', 'zh-cn', 'chinese', 'zh-tw', 'chinese (traditional)', 'co', 'corsican', 'hr', 'croatian', 'cs', 'czech', 'da', 'danish', 'nl', 'dutch', 'en', 'english', 'eo', 'esperanto', 'et', 'estonian', 'tl', 'filipino', 'fi', 'finnish', 'fr', 'french', 'fy', 'frisian', 'gl', 'galician', 'ka', 'georgian', 'de', 'german', 'el', 'greek', 'gu', 'gujarati', 'ht', 'haitian creole', 'ha', 'hausa', 'haw', 'hawaiian', 'iw', 'hebrew', 'he', 'hebrew', 'hi', 'hindi', 'hmn', 'hmong', 'hu', 'hungarian', 'is', 'icelandic', 'ig', 'igbo', 'id', 'indonesian', 'ga', 'irish', 'it', 'italian', 'ja', 'japanese', 'jw', 'javanese', 'kn', 'kannada', 'kk', 'kazakh', 'km', 'khmer', 'ko', 'korean', 'ku', 'kurdish (kurmanji)', 'ky', 'kyrgyz', 'lo', 'lao', 'la', 'latin', 'lv', 'latvian', 'lt', 'lithuanian', 'lb', 'luxembourgish', 'mk', 'macedonian', 'mg', 'malagasy', 'ms', 'malay', 'ml', 'malayalam', 'mt', 'maltese', 'mi', 'maori', 'mr', 'marathi', 'mn', 'mongolian', 'my', 'myanmar (burmese)', 'ne', 'nepali', 'no', 'norwegian', 'or', 'odia', 'ps', 'pashto', 'fa', 'persian', 'pl', 'polish', 'pt', 'portuguese', 'pa', 'punjabi', 'ro', 'romanian', 'ru', 'russian', 'sm', 'samoan', 'gd', 'scots gaelic', 'sr', 'serbian', 'st', 'sesotho', 'sn', 'shona', 'sd', 'sindhi', 'si', 'sinhala', 'sk', 'slovak', 'sl', 'slovenian', 'so', 'somali', 'es', 'spanish', 'su', 'sundanese', 'sw', 'swahili', 'sv', 'swedish', 'tg', 'tajik', 'ta', 'tamil', 'te', 'telugu', 'th', 'thai', 'tr', 'turkish', 'uk', 'ukrainian', 'ur', 'urdu', 'ug', 'uyghur', 'uz', 'uzbek', 'vi', 'vietnamese', 'cy', 'welsh', 'xh', 'xhosa', 'yi', 'yiddish', 'yo', 'yoruba', 'zu', 'zulu']

# Funktion för att välja program beroende på användarens förmåga att tala
def choose_program():
    desired_program = input("Are you able to speak? (Yes/No): \n")  # Fråga användaren om deras förmåga att tala
    
    if desired_program.lower() == "yes":  # Om användaren kan tala, kör talprogrammet
        spoken_program()  
    
    elif desired_program.lower() == "no":  # Om användaren inte kan tala, kör det skrivna programmet
        return written_program()  
    
    else:  # Om användaren anger ett ogiltigt svar, be om en korrekt input
        print("Invalid input. Please enter 'Yes' or 'No'.")
        return choose_program()  # Anropa funktionen igen för att få ett giltigt svar


# Funktion för tal till text
def speech_to_text():
    recognizer = speech_recognition.Recognizer()  # Skapa en taligenkänningsinstans
    with sr.Microphone() as source:
        voice = recognizer.listen(source)  # Lyssna på mikrofonen för tal
        listen = recognizer.recognize_google(voice, language= "en")  # Kör taligenkänningen och spara resultatet
        print(listen)
        return listen.lower()

# Funktion för att översätta text
def translate_text(data):
    translator = googletrans.Translator()  # Skapa en översättningsinstans
    translate = translator.translate(data, dest=input_language)  # Översätt texten till önskat språk
    return translate.text

# Funktion för det skrivna programmet
def written_program():
    get_written_target_language(languages)  # Hämta det valda målspråket från användaren

    data = input("write now please: \n")  # Be användaren skriva in text
    translator = googletrans.Translator()  # Skapa en översättningsinstans
    translate = translator.translate(data,dest=target_language)  # Översätt texten till det valda målspråket
    return(translate.text)

# Funktion för att hämta det skrivna målspråket från användaren
def get_written_target_language(list_of_languages):
    global target_language  # Global variabel för målspråk
    req_target_language = input("Please write the language you want to translate to: \n")  # Fråga användaren om önskat språk för översättning

    if req_target_language in list_of_languages:  # Om det valda språket finns i listan över tillgängliga språk
        language_to_index = list_of_languages.index(req_target_language) 
        target_language = (list_of_languages[language_to_index - 1])  # Sätt målspråket till det valda språket från listan
        return target_language  # Returnera det valda målspråket
    else:
        print(f"We do not support {req_target_language}, please try again")  # Meddelande om det valda språket inte stöds
        get_written_target_language(languages)  # Be användaren välja igen om det valda språket inte stöds

# Funktion för det talade programmet
def spoken_program():
    get_target_language(languages)  # Hämta det valda målspråket från användaren
    get_input_language(languages)  # Hämta det valda indatatspråket från användaren

    recognizer = speech_recognition.Recognizer()  # Skapa en taligenkänningsinstans
    with sr.Microphone() as source:
        print (translate_text("speak now"))  # Meddelande för att be användaren tala
        voice = recognizer.listen(source)  # Lyssna på mikrofonen för tal
        listen = recognizer.recognize_google(voice, language=input_language)  # Kör taligenkänningen och spara resultatet
        print(listen)

    translator = googletrans.Translator()  # Skapa en översättningsinstans
    translate = translator.translate(listen, dest=target_language)  # Översätt det tagna talet till målspråket
    print(translate.text)
    converted_audio = gtts.gTTS(translate.text, lang=target_language)  # Konvertera översatt text till ljudfil
    converted_audio.save("hello.mp3")  # Spara ljudfilen
    playsound.playsound("hello.mp3")  # Spela upp ljudfilen

# Funktion för att hämta det valda indatatspråket från användaren
def get_input_language(list_of_languages):
    global input_language  # Global variabel för indatatspråk
    print("Please say the language you want to translate from: ")  # Fråga användaren om indatatspråk

    req_input_language = speech_to_text()  # Anropa funktionen för tal till text för att ta emot användarens svar

    if req_input_language in list_of_languages:  # Om det valda språket finns i listan över tillgängliga språk
        language_to_index = list_of_languages.index(req_input_language) 
        input_language = (list_of_languages[language_to_index - 1])  # Sätt indatatspråket till det valda språket från listan
        return input_language  # Returnera det valda indatatspråket
    else:
        print(f"We do not support {req_input_language}, please try again")  # Meddelande om det valda språket inte stöds
        get_input_language(languages)  # Be användaren välja igen om det valda språket inte stöds

# Funktion för att hämta det valda målspråket
def get_target_language(list_of_languages):
    global target_language  # Global variabel för målspråk
    print("Please say the language you want to translate to: ")

    req_target_language = speech_to_text()  # Anropa funktionen för tal till text för att ta emot användarens svar

    if req_target_language in list_of_languages:  # Kontrollera om det valda språket finns i listan över tillgängliga språk
        language_to_index = list_of_languages.index(req_target_language)  # Hitta index för det valda språket
        target_language = (list_of_languages[language_to_index - 1])  # Sätt målspråket till det valda språket från listan
        return target_language  # Returnera det valda målspråket
    else:
        print(f"We do not support {req_target_language}, please try again")  # Meddelande om det valda språket inte stöds
        get_target_language(languages)  # Be användaren välja igen om det valda språket inte stöds

print ("Hello and welcome to the speech translator.")
print (choose_program())
