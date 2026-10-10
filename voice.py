"""Speech input/output helpers (offline via Sphinx + pyttsx3)."""

import speech_recognition as sr
import pyttsx3

from config import TTS_RATE

_engine = pyttsx3.init()
_engine.setProperty("rate", TTS_RATE)


def speak(text):
    _engine.say(text)
    _engine.runAndWait()


def listen():
    """Capture one utterance from the microphone; return "" on failure."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_sphinx(audio)  # OFFLINE
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

    print("You:", text)
    return text
