# Import Module
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from tkinter import *
import sys
import time

# Create Object
root = Tk()

# Add Title
root.title('Alfred')

 #Add Geometry
root.geometry("800x500")

# Keep track of the button state on/off
global is_on
is_on = False

 #Create Label
my_label = Label(root, text="Press to Start", fg="red", font=("Helvetica", 32))

root.configure(background="blue")

my_label.pack(pady=20)


# Define our switch function
def switch():
    global is_on

    # Determin is on or off
    if is_on:

        # time.sleep(5)
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        rate = engine.getProperty('rate')  # getting details of current speaking rate
        engine.setProperty('rate', 172)

        def speak(audio):
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

            assname = ("Alfred")
            speak("I am " + assname)

        def usrname():

            columns = shutil.get_terminal_size().columns

            print("#####################".center(columns))
            #    print("Welcome Mr.", uname.center(columns))
            print("#####################".center(columns))

            speak("How can i Help you ")

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

        def sendemail(to, content):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()

            # Enable low security in gmail
            server.login('dhrubfcr@gmail.com', 'radhe@123')
            server.sendmail('dhrubfcr@gmail.com', to, content)
            server.close()

        if __name__ == '__main__':
            clear = lambda: os.system('cls')

            # This Function will clean any
            # command before execution of this python file
            clear()
            wishMe()
            usrname()

            while True:
                global time

                query = takeCommand().lower()

                # All the commands said by user will be
                # stored here in 'query' and will be
                # converted to lower case for easily
                # recognition of command
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in query:
                    speak("Here you go to Youtube\n")
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    speak("Here you go to Google\n")
                    webbrowser.open("google.com")

                elif 'open outlook' in query:
                    speak("Here you go to outlook\n")
                    subprocess.call(r'C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE')

                elif 'open chrome' in query:
                    speak("here you got to chrome\n")
                    subprocess.call(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

                elif 'open discord' in query:
                    speak("sure")
                    subprocess.call(r"C:\Users\Dhruv\AppData\Local\Discord\app-0.0.309\Discord.exe")

                elif 'open firefox' in query:
                    speak("Here you go\n")
                    subprocess.call(r"C:\Program Files\Mozilla Firefox\firefox.exe")

                elif 'open word' in query:
                    speak("opening word\n")
                    subprocess.call(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.exe")

                elif 'open powerpoint' in query:
                    speak("opening power point\n")
                    subprocess.call(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.exe")

                #

                elif 'play some music' in query or "play a song" in query or "song" in query:
                    speak("Sure . Here is a random song")

                    musicpath = "C:\\Users\\Dhruv\\Music"
                    songs = os.listdir(musicpath)
                    print(songs)
                    random = os.startfile(os.path.join(musicpath, songs[2]))

                elif 'the time' in query:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    speak('Current time is ' + time)

                elif 'the date' in query:
                    date = datetime.datetime.now().strftime("%B,%d,%A,%Y")
                    print(date)
                    speak('Today is ' + date)

                elif 'email to Innoveight' in query:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = "dhrubfcr@gmail.com"
                        sendemail(to, content)
                        speak("Email has been sent !")
                    except Exception as e:
                        print(e)
                        speak("I am not able to send this email")

                elif 'send a mail' in query:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        speak("whom should i send")
                        to = input()
                        sendemail(to, content)
                        speak("Email has been sent !")
                    except Exception as e:
                        print(e)
                        speak("I am not able to send this email")

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
                    speak("Thanks for naming me again")

                elif "what's your name" in query or "What is your name" in query:
                    assname = ('Alfred')
                    speak("My friends call me")
                    speak(assname)
                    print("My friends call me", assname)

                elif 'exit' in query:

                    speak("Thanks for giving me your time")
                    root.configure(background="red")
                    # on_button.config(image=off)

                    my_label.config(text="The Switch is Off", fg="red")

                    time.sleep(1)

                    exit()
                    is_on = True

                elif "who made you" in query or "who created you" in query:
                    speak("I have been created by Innoveight.")

                elif 'joke' in query:
                    speak(pyjokes.get_joke())

                elif "solve" in query:

                    app_id = "5347RR-HTXX5KVRG6"
                    client = wolframalpha.Client(app_id)
                    indx = query.lower().split().index('solve')
                    query = query.split()[indx + 1:]
                    res = client.query(' '.join(query))
                    answer = next(res.results).text
                    print("The answer is " + answer)
                    speak("The answer is " + answer)

                elif 'search' in query or 'play' in query:
                    query = query.replace("search", "")
                    results = wikipedia.summary(query, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                #  query = query.replace("search", "")
                #  query = query.replace("play", "")
                #  print("query")
                #  webbrowser.open(query)

                elif "who i am" in query:
                    speak("If you talk then definately your human.")

                elif "why you came to world" in query:
                    speak("Thanks to Innoveight. Furthermore It's a secret")

                elif 'is love' in query:
                    speak("It is 7th sense that destroys all other senses")

                elif "who are you" in query:
                    speak("I am your virtual assistant created by Innoveight")

                elif 'reason for you' in query:
                    speak("I was created as a Minor project by Team Innoveight ")

                elif 'news' in query:

                    try:
                        jsonObj = urlopen(
                            '''https://newsapi.org/v2/top-headlines?country=in&apiKey=531a64ee3326465e9de01d0b84e4d968''')

                        data = json.load(jsonObj)
                        i = 1
                        x = 0

                        speak('here are some top news from the times of india')
                        print('''=============== TIMES OF INDIA ============''' + '\n')

                        for item in data['articles']:
                            print(str(i) + '. ' + item['title'] + '\n')
                            print(item['description'] + '\n')
                            speak(str(i) + '. ' + item['title'] + '\n')
                            i += 3


                    except Exception as e:

                        print(str(e))

                elif 'lock my pc' in query:
                    speak("locking the device")
                    ctypes.windll.user32.LockWorkStation()

                elif 'shutdown system' in query:
                    speak("Hold On a Sec ! Your system is on its way to shut down")
                    subprocess.call('shutdown / p /f')

                elif 'empty recycle bin' in query:
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                    speak("Recycle Bin Recycled")

                elif "don't listen" in query or "stop listening" in query:
                    speak("for how much time you want to stop jarvis from listening commands")
                    a = int(takeCommand())
                    time.sleep(a)
                    print(a)

                elif "where is" in query:
                    query = query.replace("where is", "")
                    location = query
                    speak("User asked to Locate")
                    speak(location)
                    webbrowser.open("https://www.google.nl/maps/place/" + location + "")

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
                    file = open('Alfred.txt', 'w')
                    file.write(note)


                elif "show note" in query:
                    speak("Showing Notes")
                    file = open("jarvis.txt", "r")
                    print(file.read())
                    speak(file.read(6))

                elif "Alfred" in query:

                    wishMe()
                    speak("Alfred in your service Mister")
                    speak(assname)

                elif "weather" in query:

                    # Google Open weather website
                    # to get API of Open weather
                    api_key = "51c47081a02f45bb088ea9ca05026e2f"
                    base_url = "http://api.openweathermap.org/data/2.5/weather?"
                    speak("Please state the City name ")
                    print("City name : ")
                    city_name = takeCommand()
                    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                    response = requests.get(complete_url)
                    x = response.json()

                    if x["cod"] != "404":
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
                        speak("Current temprature is" + str(current_temperature) + "degree kelvin")
                        speak("Current pressure is" + str(current_pressure) + "hecto pascals")
                        speak("Current humidity is" + str(current_humidiy) + "percent")
                        speak("There is")
                        speak(str(weather_description))

                    else:
                        speak(" City Not Found ")

                elif "open wikipedia" in query:
                    webbrowser.open("wikipedia.com")

                elif "Good Morning" in query:
                    speak("A warm" + query)
                    speak("How are you Mister")
                    speak(assname)

                # most asked question from google Assistant
                elif "will you be my gf" in query or "will you be my bf" in query:
                    speak("I'm not sure about, may be you should give me some more time")

                elif "how are you" in query:
                    speak("I'm fine, glad you asked that")

                elif "i love you" in query:
                    speak("It's hard to understand for me")

                elif "what is" in query or "who is" in query:

                    # Use the same API key
                    # that we have generated earlier
                    client = wolframalpha.Client("5347RR-HTXX5KVRG6")
                    res = client.query(query)

                    try:
                        print(next(res.results).text)
                        speak(next(res.results).text)
                    except StopIteration:
                        print("No results")

                elif "stock" in query:
                    print(json.dumps(getQuotes('AAPL'), indent=2))

                else:
                    speak("Sorry i was not able to understand your command")


        is_on = False
    else:
        root.configure(background="green")
        on_button.config(image=on)
        my_label.config(text="I am Listening\n Please speak", fg="green")
        is_on=True




# Define Our Images
on = PhotoImage(file="on.png")
off = PhotoImage(file="off.png")

 #Create A Button
on_button = Button(root, image=off, bd=0, command=switch)
on_button.pack(pady=50)

exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.pack(side="right")

# Execute Tkinter
root.mainloop()