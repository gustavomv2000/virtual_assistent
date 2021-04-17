import speech_recognition as sr

VI_NAME = ["João", "joão"]

def listen():
    #creates object listening for microphone
    print("diga")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 0.5
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    #tries to understand what you said
    try:
        return recognizer.recognize_google(audio, language='pt')
    except sr.UnknownValueError:
        return False
    except sr.RequestError as e:
        return "google error; {0}".format(e)


def isActive(audio):
    for name in VI_NAME:
        if name in audio:
            return True
        else:
            return False
