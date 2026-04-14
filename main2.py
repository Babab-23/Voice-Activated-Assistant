import speech_recognition as sr
import pyttsx3
import datetime
import random

# Initialize
engine = pyttsx3.init()
recognizer = sr.Recognizer()

# User name (you can change this)
user_name = "Kayla"

# Fun facts list
fun_facts = [
    "Octopuses have three hearts.",
    "Bananas are berries, but strawberries are not.",
    "Honey never spoils.",
    "Sharks existed before trees.",
    "A day on Venus is longer than a year on Venus."
]

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You:", command)
            return command.lower()
        except:
            speak("Sorry, I didn't catch that.")
            return ""

# Greeting
speak(f"Hello {user_name}, how can I help you today?")

# Main loop
while True:
    command = listen()

    if "date" in command:
        today = datetime.date.today()
        speak(f"Today's date is {today}")

    elif "hello" in command or "hi" in command:
        speak(f"Hello {user_name}! Nice to hear from you.")

    elif "fun fact" in command:
        fact = random.choice(fun_facts)
        speak(f"Here is a fun fact: {fact}")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        break

    else:
        speak("I don't understand that command yet.")