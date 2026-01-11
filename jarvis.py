import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import pyjokes
import ctypes
import subprocess
import sys
import keyboard  # New module to simulate key presses

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

def speak(audio) -> None:
    engine.say(audio)
    engine.runAndWait()

def time() -> None:
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak("The current time is")
    speak(current_time)
    print("The current time is", current_time)

def date() -> None:
    now = datetime.datetime.now()
    speak("The current date is")
    speak(f"{now.day} {now.strftime('%B')} {now.year}")
    print(f"The current date is {now.day}/{now.month}/{now.year}")

def wishme() -> None:
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 16:
        speak("Good afternoon!")
    elif 16 <= hour < 24:
        speak("Good evening!")
    else:
        speak("Good night!")
    
    assistant_name = load_name()
    speak(f"Hello! I am {assistant_name}, your AI assistant. How can I help you today?")

def takecommand() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        try:
            audio = r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            speak("Timeout occurred. Please try again.")
            return None

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
        return query.lower()
    except sr.UnknownValueError:
        speak("I'm sorry, I couldn't understand that. Can you repeat?")
        return None
    except sr.RequestError:
        speak("Speech recognition service is down. Try again later.")
        return None
    except Exception as e:
        speak(f"An error occurred: {e}")
        print(f"Error: {e}")
        return None

def screenshot() -> None:
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\screenshot.png")
    img.save(img_path)
    speak(f"Screenshot saved as {img_path}.")
    print(f"Screenshot saved as {img_path}.")

def play_music(song_name=None) -> None:
    song_dir = os.path.expanduser(r'C:\Users\ingle\Music\KISSIK.mp3')
    songs = os.listdir(song_dir)

    if song_name:
        songs = [song for song in songs if song_name.lower() in song.lower()]

    if songs:
        song = random.choice(songs)
        os.startfile(os.path.join(song_dir, song))
        speak(f"Playing {song}.")
        print(f"Playing {song}.")
    else:
        speak("No song found.")
        print("No song found.")

def write_text() -> None:
    speak("What do you want me to write?")
    text_to_write = takecommand()
    if text_to_write:
        pyautogui.write(text_to_write)
        speak(f"I've written: {text_to_write}")
        print(f"Wrote: {text_to_write}")
    else:
        speak("I couldn't catch that. Please try again.")

def press_key(key: str) -> None:
    keyboard.press(key)  # Simulate pressing a key
    speak(f"Pressed {key}")
    print(f"Pressed {key}")
    keyboard.release(key)  # Release the key

def open_application(application: str) -> None:
    if application == "google":
        wb.open("google.com")
        speak("Opening Google.")
    elif application == "youtube":
        wb.open("youtube.com")
        speak("Opening YouTube.")
    else:
        speak(f"Sorry, I cannot open {application}.")

def set_name() -> None:
    speak("What would you like to name me?")
    name = takecommand()
    if name:
        with open("assistant_name.txt", "w") as file:
            file.write(name)
        speak(f"Alright, I will be called {name} from now on.")
    else:
        speak("I couldn't catch that. Please try again.")

def load_name() -> str:
    try:
        with open("assistant_name.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "Jarvis"

def search_wikipedia(query):
    try:
        speak("Searching Wikipedia...")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
        print(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("Multiple results found. Please be more specific.")
    except Exception:
        speak("I couldn't find anything on Wikipedia.")

def volume_up() -> None:
    for _ in range(5):
        pyautogui.press('volumeup')
    speak("Volume increased.")

def volume_down() -> None:
    for _ in range(5):
        pyautogui.press('volumedown')
    speak("Volume decreased.")

def mute_volume() -> None:
    pyautogui.press('volumemute')
    speak("Volume muted.")

def open_vscode() -> None:
    vscode_path = "C:\\Users\\Public\\Desktop\\Visual Studio Code.lnk"
    os.startfile(vscode_path)
    speak("Opening Visual Studio Code.")

def press_tab() -> None:
    keyboard.press('tab')  # Simulate pressing the Tab key
    speak("Pressed Tab key.")
    print("Pressed Tab key.")
    keyboard.release('tab')  # Release the Tab key

def switch_tabs() -> None:
    keyboard.press('ctrl')
    keyboard.press('tab')  # Simulate Ctrl + Tab to switch tabs
    speak("Switched to the next tab.")
    print("Switched to the next tab.")
    keyboard.release('ctrl')
    keyboard.release('tab')  # Release the keys

def select_item() -> None:
    keyboard.press('enter')  # Simulate pressing Enter to select the highlighted item
    speak("Selected the highlighted item.")
    print("Selected the highlighted item.")
    keyboard.release('enter')

if __name__ == "__main__":
    wishme()

    while True:
        query = takecommand()
        if not query:
            continue

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            query = query.replace("wikipedia", "").strip()
            search_wikipedia(query)
        elif "play music" in query:
            song_name = query.replace("play music", "").strip()
            play_music(song_name)
        elif "open youtube" in query:
            open_application("youtube")
        elif "open google" in query:
            open_application("google")
        elif "write" in query:
            write_text()
        elif "enter" in query:
            press_key('enter')
        elif "up" in query:
            press_key('page up')
        elif "down" in query:
            press_key('page down')
        elif "right" in query:
            press_key('right')
        elif "left" in query:
            press_key('left')
        elif "home" in query:
            press_key('home')
        elif "end" in query:
            press_key('end')
        elif "backspace" in query:
            press_key('backspace')
        elif "tab" in query:
            press_tab()
        elif "switch tab" in query:
            switch_tabs()
        elif "select" in query:
            select_item()
        elif "change your name" in query:
            set_name()
        elif "screenshot" in query:
            screenshot()
        elif "volume up" in query:
            volume_up()
        elif "volume down" in query:
            volume_down()
        elif "mute" in query:
            mute_volume()
        elif "open vs code" in query:
            open_vscode()
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
        elif "shutdown" in query:
            speak("Shutting down the system. Goodbye!")
            os.system("shutdown /s /f /t 1")
            break
        elif "restart" in query:
            speak("Restarting the system.")
            os.system("shutdown /r /f /t 1")
            break
        elif "exit" in query:
            speak("Going offline. Have a great day!")
            break
