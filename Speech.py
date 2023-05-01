import speech_recognition as sr

import pyaudio

r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print("Sorry, could not request results from Google Speech Recognition service; {0}".format(e))
