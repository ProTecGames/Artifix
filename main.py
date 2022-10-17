from tkinter import *
from email.message import EmailMessage
import psutil
import ctypes
import datetime
import json
import speedtest
import os
import shutil
import smtplib
import subprocess
import time
import webbrowser
from urllib.request import urlopen
import pywhatkit
from AppOpener import run
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import winshell
import wolframalpha
from datetime import date
from clint.textui import progress
from ecapture import ecapture as ec


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio: object) -> object:
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("Artifix")
    speak("I am your Assistant")
    speak(assname)
    speak("tell me how can i help you")





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
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query




if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    wishMe()


    while True:

        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'play' in query:
                song = query.replace('play', '')
                speak('playing ' + song)
                pywhatkit.playonyt(song)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif "google" in query or "search google" in query:
            speak("Here you go to Google\n")
            webbrowser.open_new("google.com")

        elif 'stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open_new("stackoverflow.com")




        elif 'search app' in query:

                speak("enter app name")
                # taking input
                inp = input("ENTER APPLICATION TO OPEN: ").strip()
                # check if there is input
                if input:
                    run(inp)
                    speak("Opening please wait")
        elif 'the date' in query:
            today = date.today()
            speak(today)
            print(today)
        elif 'battery' in query:
            def convertTime(seconds):
                minutes, seconds = divmod(seconds, 60)
                hours, minutes = divmod(minutes, 60)
                return "%d:%02d:%02d" % (hours, minutes, seconds)
            battery = psutil.sensors_battery()
            speak("present left battery is")
            speak(battery.percent)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")



        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif "who are developers" in query:
            speak("developers are the people who are capable of changing this world")
            print("Developers are the people who are capable of changing this world")

        elif "is god" in query:
            speak("i don't know where or who is god for me the person who has given me life because of whome i can talk understand others is god")
            print("I don't know where or who is god for me the person who has given me life because of whome i can talk understand others is god :-)")


        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "tell me about yourself" in query:
            speak("Artifix is a python based artificial assistant made by ProTec Games in the year 2022. I am a part of project that is to be submitted to I.I.T mumbai e cell")
            print("Artifix is a python based artificial assistant made by ProTec Games in the year 2022. I am a part of project that is to be submitted to I.I.T mumbai e-cell")

        elif "unique in you" in query or "unique about you" in query:
            speak("I can calculate your internet speed, i can make tweet, i can chat, i can do almost evrything as that of a high tech robot")
            print("I can calculate your internet speed, I can make tweet, I can chat, I can do almost everything as that of a high tech robot")

        elif "like coding" in query:
            speak("I like coding becuase coding is a art that can make dreams come to reality")
            print("I like coding because Coding is a art that can make dreams come to reality")

        elif "something about developer" in query:
            speak("My developer is prakhar doneria.he has made me to make this world a better in I.t. sector. my developers keep working hard to give me new features everyday so that i can be more productive to our users")
            print("My developer is prakhar doneria. He has made me to make this world a better in I.T. sector. My developers keep working hard to give me new features everyday so that I can be more productive to our users")

        elif "kill humans" in query or "kill us" in query or "kill me" in query:
            speak("i don't think so technology is been made for helping humans not destroying them. it's the human who stars using it in negative way like the nuclear power.for me asking such questions is useless because our control is in under humans only we can't even work without humans then how can we kill you. after all a chaild can't go againt the parents")
            print("I don't think so technology is been made for helping humans not destroying them. It's the human who stars using it in negative way like the nuclear power.For me asking such questions is useless because our control is in under humans only we can't even work without humans then how can we kill you. After all a chaild can't go againt the parents")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by ProTec Games.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:

            app_id = "QGTETJ-2GGPV6AJU4"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to ProTec Games. further It's a secret")

        elif 'wi-fi connected list' in query:
            speak("please wait collecting data")
            # getting meta data of the wifi network
            meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

            # decoding meta data from byte to string
            data = meta_data.decode('utf-8', errors="backslashreplace")

            # splitting data by line by line
            # string to list
            data = data.split('\n')

            # creating a list of wifi names
            names = []

            # traverse the list
            for i in data:

                # find "All User Profile" in each item
                # as this item will have the wifi name
                if "All User Profile" in i:
                    # if found split the item
                    # in order to get only the name
                    i = i.split(":")

                    # item at index 1 will be the wifi name
                    i = i[1]

                    # formatting the name
                    # first and last chracter is use less
                    i = i[1:-1]

                    # appending the wifi name in the list
                    names.append(i)

            # printing the wifi names
            print("All wifi that system has connected to are ")
            print("-----------------------------------------")
            for name in names:
                print(name)

        elif 'is love' in query:
            speak("A feeling that can not be expressed but can be felt")

        elif "who are you" in query:
            speak("I am your virtual assistant created by ProTec Games")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister ProTec Games ")

        elif 'open text editor' in query:
            speak("opening text editor")
            root = Tk()
            root.geometry("350x250")
            root.title("Artifix Notes")
            root.minsize(height=250, width=350)
            root.maxsize(height=250, width=350)

            scrollbar = Scrollbar(root)

            scrollbar.pack(side=RIGHT,
                           fill=Y)

            text_info = Text(root,
                             yscrollcommand=scrollbar.set)
            text_info.pack(fill=BOTH)

            scrollbar.config(command=text_info.yview)

            root.mainloop()

        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)

        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))


        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Secound ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop Artifix from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Artifix Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('artifix.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("artifix.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

        elif "artifix" in query:

            wishMe()
            speak("Artifix in your service sir")
            speak(assname)

        elif "weather" in query:

            api_key = "enter api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" City Not Found ")

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(assname)
#question asked from google assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:

            speak("I'm fine, glad you me that")

        elif "internet speed" in query:
            wifi = speedtest.Speedtest()
            speak("checking your internet speed please wait it can take some time")
            print("Wifi Download Speed is ", wifi.download())
            print("Wifi Upload Speed is ", wifi.upload())


        elif "what is" in query or "who is" in query:

            client = wolframalpha.Client("QGTETJ-2GGPV6AJU4")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")
            else:
                speak("")
