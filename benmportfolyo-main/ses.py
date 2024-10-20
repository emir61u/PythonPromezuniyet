import speech_recognition as sr

def turkce():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Say something!")

        audio = r.listen(source)

 

    a = r.recognize_google(audio, language = "tr-TR")

    return a 



