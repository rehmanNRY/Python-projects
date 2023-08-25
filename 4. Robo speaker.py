import os
from gtts import gTTS
from playsound import playsound
def myFun(my_text):
    voice = gTTS(text=my_text)
    voice.save("my_audio.mp3")
    playsound("my_audio.mp3")
    os.remove("my_audio.mp3")
print("========== Welcome o Robo-Speaker ==========")
print("* Press q to exit")
while(True):
    text = input("==> Enter text: ")
    if text=="q" or text=="Q":
        print("==> Thanks for using, return soon!")
        break
    else:
        myFun(text)