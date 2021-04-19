import voice_listener
import webbrowser
from gtts import gTTS
from pynput.keyboard import Key, Controller
import time
import os


VI_NAME = ["Google", "google"]

def check_activities(audio):
    response = ""
    if "pesquise por" in audio or "pesquisar" in audio or "pesquise sobre" in audio or "pesquisa sobre" in audio or "pesquise" in audio:
        response = search_for(audio)

    #elif "Oi" in audio or "oi" in audio or "olá" in audio or "Olá" in audio or "Eae" in audio or "eae" in audio:
    #    response = greetings()

    elif audio in VI_NAME:
        call_name()

    elif "digite" in audio.lower():
        type(audio)

    elif "youtube" in audio.lower():
        search_youtube(audio)

    elif "fechar janela" in audio.lower():
        close_tab()

    elif "fechar aplicativo" in audio.lower():
        close_app()

    elif "desligar computador" in audio.lower():
        shutdown()


    if response != "":
        tts = gTTS(text=response, lang='pt-br')
        tts.save("good.mp3")
        voice_listener.speak()


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

    url = "https://www.google.com.tr/search?q={}".format(terms)
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(
                            'C:\Program Files\Google\Chrome\Application\chrome.exe'))
    webbrowser.get('chrome').open(url)

    return "Estes foram os resultados encontrados"


def greetings():
    return "Olá"


def call_name():
    tts = gTTS(text="o que deseja?", lang='pt-br')
    tts.save("good.mp3")
    voice_listener.speak()
    audio = voice_listener.listen()
    if audio != False:
        check_activities(audio)
    else:
        tts = gTTS(text="Não entendi", lang='pt-br')
        tts.save("good.mp3")
        voice_listener.speak()


def type(text):
    if "digite" in text:
        text = text.split("digite", 1)[1]

    keyboard = Controller()

    for char in text:
        keyboard.press(char)
        keyboard.release(char)


def search_youtube(audio):
    terms = ""
    if "youtube" in audio.lower():
        terms = audio.lower().split("youtube", 1)[1]
    url = "https://www.youtube.com/results?search_query={}".format(terms)
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(
                            'C:\Program Files\Google\Chrome\Application\chrome.exe'))
    webbrowser.get('chrome').open(url)


def close_tab():
    keyboard = Controller()

    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release(Key.ctrl)
    keyboard.release('w')


def close_app():
    keyboard = Controller()

    keyboard.press(Key.alt)
    keyboard.press(Key.f4)
    keyboard.release(Key.alt)
    keyboard.release(Key.f4)


def shutdown():
    os.system("shutdown /s /t 1")