from input_assistant import voice_listener
import webbrowser
from pynput.keyboard import Key, Controller
import os
from nlu.classifier import classify
import datetime
from auxiliar import improve_model


VI_NAME = "google"


def check_activities(audio):

    response = ""

    improve_model.write_nem_commands(audio.lower().split(VI_NAME)[1])

    if "pesquise por" in audio or "pesquisar" in audio or "pesquise sobre" in audio or "pesquisa sobre" in audio or "pesquise" in audio:
        response = search_for(audio)
        confirmation(response)
        return

    elif audio in VI_NAME:
        call_name()
        confirmation(response)
        return

    elif "digite" in audio.lower() or "escreva" in audio.lower() or "digita" in audio.lower():
        type(audio)
        confirmation(response)
        return

    elif "youtube" in audio.lower():
        response = search_youtube(audio)
        confirmation(response)
        return

    elif "fechar janela" in audio.lower() or "fechar aba" in audio.lower():
        response = close_tab()
        confirmation(response)
        return

    elif "fechar aplicativo" in audio.lower() or "fechar programa" in audio.lower() or "fechar app" in audio.lower():
        response = close_app()
        confirmation(response)
        return

    elif "desligar computador" in audio.lower() or "desligar pc" in audio.lower():
        shutdown()
        confirmation(response)
        return

    elif "abrir chrome" in audio.lower():
        response = open_chrome()
        confirmation(response)
        return

    elif "abrir spotify" in audio.lower():
        response = open_spotify()
        confirmation(response)
        return

    entity = classify(audio.lower().split(VI_NAME)[1])

    print('entity: ', entity)

    response = ""
    if entity == 'search|search_for':
        response = search_for(audio)

    elif entity == 'time|get_time':
        response = get_time()

    elif entity == 'date|get_date':
        response = get_date()

    if response != "":
        voice_listener.speak(response)


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
    else:
        terms = audio.lower().split(VI_NAME)[1]

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
    voice_listener.speak("o que deseja?")
    audio = voice_listener.listen()
    if audio != False:
        check_activities(audio)
    else:
        voice_listener.speak("Não entendi")


def type(text):
    if "digite" in text.lower():
        text = text.lower().split("digite", 1)[1]

    keyboard = Controller()

    for char in text:
        keyboard.press(char)
        keyboard.release(char)

    return "ok"


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
    return "ok"


def close_tab():
    keyboard = Controller()

    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release(Key.ctrl)
    keyboard.release('w')
    return "ok"


def close_app():
    keyboard = Controller()

    keyboard.press(Key.alt)
    keyboard.press(Key.f4)
    keyboard.release(Key.alt)
    keyboard.release(Key.f4)
    return "ok"


def shutdown():
    audio = False
    voice_listener.speak("Tem certeza que deseja desligar o computador?")
    while not audio:
        audio = voice_listener.listen()


    print(audio)
    if 'sim' in audio.lower():
        voice_listener.speak("Ok, desligando")
        os.system("shutdown /s /t 1")
    else:
        voice_listener.speak("Ok, cancelando")
        pass


def get_time():
    now = datetime.datetime.now()
    answer = 'São {} horas e {} minutos.'.format(now.hour, now.minute)
    return answer


def get_date():
    now = datetime.datetime.now()
    answer = 'Hoje é dia {} de {} de {}'.format(now.day, now.strftime("%B"), now.year)
    return answer


def open_chrome():
    os.system('C:\Program Files\Google\Chrome\Application\chrome.exe')
    return 'abrindo chrome'


def open_spotify():
    os.system('C:/Users/Gustavo/AppData/Roaming/Spotify/Spotify.exe')
    return 'abrindo spotify'


def open_notion():
    os.system('C:/Users/Gustavo/AppData/Local/Programs/Notion/Notion.exe')
    return 'abrindo notion'


def confirmation(response):
    if response != "":
        voice_listener.speak(response)