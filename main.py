import webbrowser
import speech_recognition as sr
import pyttsx3
import subprocess
import wolframalpha
import requests
import pywhatkit
import datetime
import time as tm
import wikipedia
import pyjokes
import ctypes
from ecapture import ecapture as ec



engine = pyttsx3.init()
engine.setProperty('rate', 170)

#for female voice
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

#for random talk
def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        talk("Good Afternoon Sir !")

    else:
        talk("Good Evening Sir !")

    talk("I am your personal Assistant, BOB")

wishMe()

#taking the command through microphone
def take_command():
    listner = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listenng..........')
        listner.pause_threshold = 1
        voice = listner.listen(source)
    try:
        # Recognizing the voice
        print("Recognizing..........")
        command = listner.recognize_google(voice, language='en-us')
        command = command.lower()
        print(f"User said: {command}\n")

        if 'bob' in command:
            command = command.replace('bob', '')
            print(command)

    except Exception as e:
        print(e)

    return command

def run_bob():
    command = take_command()
    print(command)

    if 'how are you' in command:
        talk('i am fine, thank you,sir.')
        talk('how are you? sir')

    elif 'good' in command or 'fine' in command:
         talk('it is good to know that, you are fine')
    elif "very bad" in command:
        talk("Sorry to hear that sir")

    elif 'who are you' in command:
        talk('I am your virtual assistant, bob')

        # for openning youtube
    elif 'open youtube' in command:
        talk('Here you go to youtube')
        webbrowser.open("youtube.com")

    # for openning google
    elif 'open google' in command:
        talk("Here you go to Google\n")
        webbrowser.open("google.com")

    #play youtube video
    elif 'play' in command:
        song = command.replace('play', ' ')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    #to capture photo
    elif 'camera' in command or 'take photo' in command:
        talk("openning camera")
        ec.capture(0, "frame", "photo.jpg")

    elif 'are you single' in command:
        talk('Yes i am single. Girls does not love me')

    # using subprocsses
    elif 'restart' in command:
        talk('restarting')
        subprocess.call(['shutdown', '/r'])
    elif 'hibernate' in command:
        talk("Hibernating")
        subprocess.call("shutdown / h")
    elif 'shutdown system' in command:
        talk("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')
    elif 'lock window' in command:
        talk("locking the device")
        ctypes.windll.user32.LockWorkStation()

    # calculation some quick math
    elif 'calculate' in command:
        app_id = "RTJP3Q-8PR4L5LWLW"
        client = wolframalpha.Client(app_id)
        indx = command.lower().split().index('calculate')
        command = command.split()[indx + 1:]
        res = client.query(' '.join(command))
        answer = next(res.results).text
        print("The answer is " + answer)
        talk("The answer is " + answer)

    # answer some quick question
    elif 'what is' in command:
        client = wolframalpha.Client('RTJP3Q-8PR4L5LWLW')
        res = client.query(command)
        try:
            print(next(res.results,).text)
            talk(next(res.results).text)
        except StopIteration:
            print("No result")

    #date and time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif "where is" in command:
        query = command.replace("where is", "")
        location = query
        talk("User asked to Locate")
        talk(location)
        webbrowser.open("http://www.google.com/maps/place/" + location + "")

    #wikipedia info
    elif 'who is' in command:
        talk('Searching in Wikipedia...')
        query = command.replace("wikipedia", "")
        results = wikipedia.summary(query, 3)
        talk("According to Wikipedia")
        print(results)
        talk(results)

    elif "who made you" in command or "who created you" in command:
        talk("I have been created by team Praggo.")

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    elif "write a note" in command:
        talk("What should i write, sir")
        note = take_command()
        file = open('note.txt', 'w')
        file.write(note)
        talk("writing done,sir")

    #writing notes
    elif "show the note" in command:
        talk("Showing Notes")
        file = open("note.txt", "r")
        print(file.read())
        talk(file.read(6))

    elif "don't listen" in command or "stop listening" in command:
        talk("for how much time you want to stop bob from listening commands")
        a = int(take_command())
        tm.gmtime(a)
        print(a)

    elif "stalin alex" in command:
        talk("Doctore D stalin alex completed his Doctorate in Computer Science and Engineering, Anna University, Chennai, India Published 10 Research Articles in SCOPUS Indexed Journal,now he is workin as a professor in sate university of banglaesh")
        print('Doctore D stalin alex completed his Doctorate in Computer Science and Engineering, Anna University, Chennai, India Published 10 Research Articles in SCOPUS Indexed Journal,now he is workin as a professor in sate university of banglaesh')

    elif "are you there" in command:
        talk("Yes, i am here")

    elif "thank you" in command:
        talk("it is my pleasure sir.")

    elif 'stop for now' in command:
        talk('Thanks for giving me your time')
        exit()

    else:
        talk('please say the command again.')


while True:
    run_bob()

