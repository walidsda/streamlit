import streamlit as st
import speech_recognition as sr

r = sr.Recognizer()

audio_file = st.file_uploader("Upload an audio file or record audio", type=["wav", "mp3"])
if audio_file is not None:
    with open("user_audio.wav", "wb") as f:
        f.write(audio_file.getbuffer())
    audio = sr.AudioFile("user_audio.wav")
else:
    with sr.Microphone() as source:
        audio = r.record(source, duration=5)

try:
    text = r.recognize_google(audio)
    st.write("You said:", text)
except sr.UnknownValueError:
    st.write("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    st.write("Sorry, could not request results from Google Speech Recognition service; {0}".format(e))