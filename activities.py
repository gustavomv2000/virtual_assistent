import voice_listener
import webbrowser
from gtts import gTTS
import os

VI_NAME = ["João", "joão"]

def check_activities(audio):
    response = ""
    if "pesquise por" in audio or "pesquisar" in audio or "pesquise sobre" in audio or "pesquisa sobre" in audio or "pesquise" in audio:
        response = search_for(audio)

    elif "Oi" in audio or "oi" in audio or "olá" in audio or "Olá" in audio or "Eae" in audio or "eae" in audio:
        response = greetings()

    elif audio in VI_NAME:
        call_name()

    if response != "":
        tts = gTTS(text=response, lang='pt-br')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")


def search_for(audio):
    terms = ""
    if "pesquise por" in audio:
        terms = audio.split("pesquise por", 1)[1]
    elif "pesquisar" in audio:
        terms = audio.split("pesquisar", 1)[1]
    elif "pesquise sobre" in audio:
        terms = audio.split("pesquise sobre", 1)[1]
    elif "pesquisa sobre" in audio:
        terms = audio.split("pesquisa sobre", 1)[1]
    elif "pesquise" in audio:
        terms = audio.split("pesquise", 1)[1]

    print("audio: ", audio)
    print("search terms was: ", terms)

    url = "https://www.google.com.tr/search?q={}".format(terms)
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(
                            '/usr/bin/google-chrome'))
    webbrowser.get('chrome').open(url)

    return "Estes foram os resultados encontrados"


def greetings():
    return "Olá"


def call_name():
    tts = gTTS(text="o que deseja?", lang='pt-br')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")
    audio = voice_listener.listen()
    if audio != False:
        check_activities(audio)
    else:
        tts = gTTS(text="Não entendi", lang='pt-br')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")