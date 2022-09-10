import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ").lower()
if this == "tangina ka":
    cowsay.cow("tangina ka din")
    engine.say("tangina ka din")
    engine.runAndWait()