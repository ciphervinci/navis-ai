import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random
import os
import subprocess

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'nexa' in command:
                command = command.replace('nexa ', '')
    except:
        print('Microphone error or no response!')
        pass
    return command

def play_music(music):
    talk('playing' + music)
    pywhatkit.playonyt(music)

def talk_greetings():
    greetings = ['Hi Whats up?',
                 'Hello! How are you?',
                 'Welcome',
                 'Lets have some fun',
                 'Ask me anything']
    talk(random.choice(greetings))

def open_application(app_name):
    talk('opening ' + app_name)
    if 'spotify' in app_name:
        spotify_location = r'"C:\Users\Da Vinci\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Spotify.lnk"'
        os.system(spotify_location)

def run_nexa():
    command = take_command()
    print(command)
    if 'what is' in command:
        wikiterm = command.replace('what is', '')
        info = wikipedia.summary(wikiterm, 1)
        print(info)
        talk(info)

    elif 'open' in command:
        open_application(command.replace('open', ''))

    elif 'song' in command:
        song1 = command.replace('song', '')
        play_music(song1)

    elif 'music' in command:
        song2 = command.replace('music', '')
        play_music(song2)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d %B, %Y')
        print(date)
        talk('Today date is ' + date)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'Hi' or 'Hello' in command:
        talk_greetings()

    else:
        talk("I can't get it. Try again")

while True:
    run_nexa()