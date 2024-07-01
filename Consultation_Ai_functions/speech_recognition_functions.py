from PyQt5.QtWidgets import QApplication
from windows_functions.loading_windows import D2D, D2Z
import speech_recognition as sr
import pyttsx3
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def recognize_speechZ():
    global  D2Z
    with sr.Microphone() as source:
        D2Z.listen.setText("Listening...")
        QApplication.processEvents()
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        D2Z.listen.setText("")
        D2Z.user.setText(text)
        QApplication.processEvents()
        return text
    except sr.UnknownValueError:
        D2D.listen.setText("")
        QApplication.processEvents()
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError as e:
        D2D.listen.setText("")
        QApplication.processEvents()
        return "Could not request results"

def respondZ(text):
    global  D2Z
    D2Z.AI.setText(text)
    D2Z.listen.setText("")
    QApplication.processEvents()
    engine.say(text)
    engine.runAndWait()

def recognize_speechD():
    global  D2D
    with sr.Microphone() as source:
        D2D.listen.setText("Listening...")
        QApplication.processEvents()
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        D2D.listen.setText("")
        D2D.user.setText(text)
        QApplication.processEvents()
        return text
    except sr.UnknownValueError:
        D2D.listen.setText("")
        QApplication.processEvents()
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError as e:
        D2D.listen.setText("")
        QApplication.processEvents()
        return "Could not request results"

def respondD(text):
    global  D2D
    D2D.AI.setText(text)
    D2D.listen.setText("")
    QApplication.processEvents()
    engine.say(text)
    engine.runAndWait()
    
def talk(text):
    engine.say(text)
    engine.runAndWait()
    