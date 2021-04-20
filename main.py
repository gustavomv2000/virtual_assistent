from input_assistant import voice_listener
from system import activities
from nlu.classifier import classify


while(True):
    audio = voice_listener.listen()
    print(audio)
    if audio != False:
        print('is Active? ', voice_listener.isActive(audio))
        if voice_listener.isActive(audio):
            #print(classify(audio.lower()))
            activities.check_activities(audio)
