import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import time
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    # Function to send email, you can implement this based on your requirements
    pass

def fetch_circuit_info():
    url = "https://en.wikipedia.org/wiki/Electronic_circuit"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Assuming the information is in paragraphs under a specific class
        circuit_info_paragraphs = soup.find_all('p', class_='circuit-info')
        if circuit_info_paragraphs:
            circuit_info = ' '.join([p.get_text() for p in circuit_info_paragraphs])
            return circuit_info
    return None

def open_telegram():
    # Assuming Telegram is installed in the default location on Windows
    os.system("start telegram")

def make_telegram_call(contact_name):
    # Assuming you have a contact saved in Telegram with the given name
    os.system(f"telegram -call {contact_name}")

def search_on_internet(query):
    browser_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"  # Path to Microsoft Edge executable
    search_url = f"https://www.youtube.com/results?search_query={query}"  # YouTube search URL with query

    # Open Microsoft Edge with the search URL
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(browser_path))
    webbrowser.get('edge').open(search_url)

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'your songs Path'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = " Your VS Code.exe Path"
            os.startfile(codePath)

        elif 'email to ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "YourfriendEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif 'open paint' in query:
            os.system("start mspaint")

        elif 'draw electric circuit' in query:
            speak('Fetching electric circuit information...')
            circuit_info = fetch_circuit_info()
            if circuit_info:
                print(circuit_info)
                speak(circuit_info)
            else:
                speak('Sorry, I couldn\'t fetch electric circuit information at the moment.')

        elif 'open telegram' in query:
            open_telegram()

        elif 'make telegram call' in query:
            speak("Whom do you want to call?")
            contact_name = takeCommand()
            make_telegram_call(contact_name)

        elif 'search on internet' in query:
            speak("What do you want to search?")
            search_query = takeCommand()
            search_on_internet(search_query)

        elif 'open' in query:  
            app_name = query.split('open ')[-1]  
            os.system(f"start {app_name}.exe")

        # You can add more conditions based on your requirement to open specific applications or perform tasks.