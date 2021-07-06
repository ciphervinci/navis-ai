import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

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

def run_nexa():
    command = take_command()
    print(command)
    if 'song' in command:
        song = command.replace('song', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d %B, %Y')
        print(date)
        talk('Today date is ' + date)
    elif 'what is' in command:
        wikiTerm = command.replace('what is', '')
        info = wikipedia.summary(wikiTerm, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk("I can't get it. Try again")

while True:
    run_nexa()