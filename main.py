import voice_listener
import activities
import pyttsx3


while(True):
    audio = voice_listener.listen()
    print(audio)
    if audio != False:
        print('is Active? ', voice_listener.isActive(audio))
        if voice_listener.isActive(audio):
            activities.check_activities(audio)
