import os
import sys
import pyautogui
import webbrowser
import smtplib
import time
from datetime import datetime
import wikipedia
import pygame
import pyttsx3
import requests
import subprocess
import math

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    # Greet the user
    hour = int(datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("How can I assist you today?")

def takecommand():
    # Simulate listening and return the command (you can integrate speech-to-text here)
    query = input("You: ")
    return query.lower()

def time():
    curr_time = datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {curr_time}")

def date():
    curr_date = datetime.now().strftime("%Y-%m-%d")
    speak(f"Today's date is {curr_date}")

def search_wikipedia(query):
    result = wikipedia.summary(query, sentences=2)
    speak(result)

def play_music():
    pygame.mixer.init()  # Initialize the mixer module
    pygame.mixer.music.load(r'C:\Users\ingle\Music\KISSIK.mp3')  # Load the sound file
    pygame.mixer.music.play()  # Play the sound

def open_application(app_name):
    apps = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "twitter": "https://www.twitter.com",
        "facebook": "https://www.facebook.com"
    }
    url = apps.get(app_name)
    if url:
        webbrowser.open(url)
        speak(f"Opening {app_name}")

def write_text() -> None:
    speak("What do you want me to write?")
    text_to_write = takecommand()
    if text_to_write:
        pyautogui.write(text_to_write)
        speak(f"I've written: {text_to_write}")
        print(f"Wrote: {text_to_write}")
    else:
        speak("I couldn't catch that. Please try again.")

def press_key(key):
    pyautogui.press(key)

def press_tab():
    pyautogui.press('tab')

def switch_tabs():
    pyautogui.hotkey('ctrl', 'tab')

def select_item():
    pyautogui.click()

def set_name():
    speak("What would you like to set your name to?")
    name = takecommand()
    speak(f"Your name is now set to {name}")

def screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speak("Screenshot taken and saved.")

def volume_up():
    os.system("nircmd.exe changesysvolume 5000")

def volume_down():
    os.system("nircmd.exe changesysvolume -5000")

def mute_volume():
    os.system("nircmd.exe mutesysvolume 1")

def open_vscode():
    os.system("code")

def tell_joke():
    jokes = ["Why don't scientists trust atoms? Because they make up everything!",
            "Why did the computer go to the doctor? Because it had a virus!"]
    speak(jokes[0])

def get_weather(city):
    # You can use an API like OpenWeatherMap
    api_key = "your_openweathermap_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()
    if data['cod'] == 200:
        weather = data['main']
        temp = weather['temp'] - 273.15  # Convert from Kelvin to Celsius
        description = data['weather'][0]['description']
        speak(f"The temperature in {city} is {temp:.2f}°C with {description}.")
    else:
        speak("Sorry, I couldn't fetch the weather for that city.")

def send_email(to, subject, body):
    # Sending email logic
    email = "your_email@example.com"
    password = "your_email_password"
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(email, to, message)
        server.quit()
        speak(f"Email sent to {to}")
    except Exception as e:
        speak(f"Failed to send email. Error: {str(e)}")

def calculator(query):
    query = query.replace("calculate", "").strip()
    try:
        # Safe evaluation using eval
        result = eval(query)
        speak(f"The result is {result}")
    except Exception as e:
        speak("Sorry, I couldn't perform the calculation. Please try again.")

def search_youtube(query):
    query = query.replace("search youtube", "").strip()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    speak(f"Here are the results for {query} on YouTube.")

def web_search(query):
    query = query.replace("search the web", "").strip()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query} on the web.")

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
        elif "open twitter" in query:
            open_application("twitter")
        elif "open facebook" in query:
            open_application("facebook")
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
            tell_joke()
        elif "weather" in query:
            city = query.replace("weather", "").strip()
            get_weather(city)
        elif "send email" in query:
            speak("Please tell me the recipient's email address.")
            to = takecommand()
            speak("What is the subject?")
            subject = takecommand()
            speak("What should be the body?")
            body = takecommand()
            send_email(to, subject, body)
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
        elif "calculate" in query:
            calculator(query)
        elif "search youtube" in query:
            search_youtube(query)
        elif "search the web" in query:
            web_search(query)
