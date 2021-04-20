# -*- coding: utf-8 -*-
import speech_recognition as sr
import pygame
import pathlib
import os
from time import sleep
import pyglet
from gtts import gTTS

VI_NAME = "google"

def listen():
    #creates object listening for microphone
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    sr.Microphone.list_microphone_names()
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
    if VI_NAME.lower() in audio.lower():
        return True
    else:
        return False


def speak(text):
    tts = gTTS(text=text, lang='pt-br')
    tts.save("good.mp3")

    music = pyglet.media.load("good.mp3", streaming=False)
    music.play()

    sleep(music.duration)  # prevent from killing
    os.remove("good.mp3")  # remove temperory file