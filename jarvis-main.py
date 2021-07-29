# Hello Everyone. This is Vedansh Ruhela and I have created this Jarvis using Python.
# I hope you will enjoy it. :) :] :D 

# These are the all imported modules

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import time
import random
from PIL import Image
import winsound
import datefinder
import wolframalpha
import pyjokes
import requests 
import cv2
import numpy as np 
import smtplib
import logging
import json
import platform
import pyautogui
import subprocess
import pyaudio
import requests
import ctypes
import PyPDF2
import operator
import pyperclip
import pytz
import speedtest
import sounddevice as sd
from scipy.io.wavfile import write  
from googletrans import Translator
from pywikihow import search_wikihow
import qt5_applications
import qt5_tools
import QtDesigner
from bs4 import BeautifulSoup
from plyer import notification
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTimer, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisGUI import Ui_MainWindow

# To get the voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

#To Change the speaking speed of jarvis.
rate = engine.getProperty("rate")
engine.setProperty("rate",172)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#To Wish Me
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}.")
        print(f"good morning, its {tt}.")
        search = 'what is the temperature?'
        url = f'https://www.google.com/search?q={search}'
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        speak(f"The Current Temperature outside is {temp}")
        print(f"The Current Temperature outside is {temp}")
        import psutil
        battery = psutil.sensors_battery()
        percentage = battery.percent
        speak(f"System current battery level is {percentage} percent.")
        print(f"System current battery level is {percentage} percent.")
        if percentage>=75:
            speak("Sir, system have enough battery level to rock and roll.")
            print("Sir, system have enough battery level to rock and roll.")
        elif percentage>=40 and percentage<=75:
            speak("Sir, system have enough battery level but I would suggest you to connect to charger.")
            print("Sir, system have enough battery level but I would suggest you to connect to charger.") 
        elif percentage>=15 and percentage<=30:
            speak("Sir, system have less battery, I would recommend you connecting to the charger.")
            print("Sir, system have less battery, I would recommend you connecting to the charger.")    
        elif percentage<=15:
            speak("Sir, system do not have battery to work. Please connect to the charger or else I will shutdown the system.")
            print("Sir, system do not have battery to work. Please connect to the charger or else I will shutdown the system.")
    elif hour >= 12 and hour <= 17:
        speak(f"good afternoon, its {tt}.")
        print(f"good afternoon, its {tt}.")
        search = 'what is the temperature?'
        url = f'https://www.google.com/search?q={search}'
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        speak(f"The Current Temperature outside is {temp}.")
        print(f"The Current Temperature outside is {temp}.")
        import psutil
        battery = psutil.sensors_battery()
        percentage = battery.percent
        speak(f"System current battery level is {percentage} percent.")
        print(f"System current battery level is {percentage} percent.")
        if percentage>=75:
            speak("Sir, system have enough battery level to rock and roll.")
            print("Sir, system have enough battery level to rock and roll.")
        elif percentage>=40 and percentage<=75:
            speak("Sir, system have enough battery level but I would suggest you to connect to charger.")
            print("Sir, system have enough battery level but I would suggest you to connect to charger.") 
        elif percentage>=15 and percentage<=30:
            speak("Sir, system have less battery, I would recommend you connecting to the charger.")
            print("Sir, system have less battery, I would recommend you connecting to the charger.")    
        elif percentage<=15:
            speak("Sir, system do not have battery to work. Please connect to the charger or else I will shutdown the system.")
            print("Sir, system do not have battery to work. Please connect to the charger or else I will shutdown the system.")
    else:
        speak(f"good evening, its {tt}.")
        print(f"good evening, its {tt}.")
        search = 'what is the temperature?'
        url = f'https://www.google.com/search?q={search}'
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        speak(f"The Current Temperature outside is {temp}.")
        print(f"The Current Temperature outside is {temp}.")
        import psutil
        battery = psutil.sensors_battery()
        percentage = battery.percent
        speak(f"System current battery level is {percentage} percent.")
        print(f"System current battery level is {percentage} percent.")
        if percentage>=75:
            speak("Sir, system have enough battery level to rock and roll.")
            print("Sir, system have enough battery level to rock and roll.")
        elif percentage>=40 and percentage<=75:
            speak("Sir, system have enough battery level but I would suggest you to connect to charger.")
            print("Sir, system have enough battery level but I would suggest you to connect to charger.") 
        elif percentage>=15 and percentage<=30:
            speak("Sir, system have less battery, I would recommend you connecting to the charger.")
            print("Sir, system have less battery, I would recommend you connecting to the charger.")    
        elif percentage<=15:
            speak("Sir, system do not have battery to work. Please connect to the charger or else I will shutdown the system.")
            print("Sir, system do not have battery to work. Please connect to the charger or else I will shutdown the system.")
         
    speak("This is Jarvis Sir. How may I help you?.") 
    print("This is Jarvis Sir. How may I help you?.")    

#To know the news
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bac4de1e43164a2c9f701633f09fa284'
    main_page = requests.get(main_url).json()
    articles = main_page['articles']
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eigth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")    

#To Read pdf   
def pdffiles():
    book = open('oop.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(pages)
    speaker = pyttsx3.init()
    page = pdfReader.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

# To read the selected text
def read():
    pyautogui.hotkey("ctrl",'c')
    tobespoken=pyperclip.paste()
    speak(tobespoken)

# To make a note and save it. 
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])   

# To repeat my speech
def repeatmyspeech():
    speak("Okay starting to listen.")
    speak(" start speaking.")
    print("Okay starting to listen.")
    print(" start speaking.")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" I am Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:   
        query = r.recognize_google(audio, language='en-in')
        speak(f"User said: {query}\n")
        print(f" here is your text repetition by me {query}.\n")
    except Exception as e:
        return "None"
    return query

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print('Recognising...')  
            query = r.recognize_google(audio, language='en-in')
            print(f'User said: {query}\n')

        except Exception as e:
            print('Please say that again Sir...')    
            return "none"
        query = query.lower()
        return query 

        

    def run(self):
        while True:
            self.query = self.takeCommand()
            if "wake up jarvis" in self.query or "wake up" in self.query or "jarvis" in self.query:
                self.TaskExecution()
            
    # To execute all the commands
    def TaskExecution(self):
        wish()
        while True:
            self.query = self.takeCommand()
            if 'wikipedia' in self.query or "wiki" in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)       

    # Saying hello to jarvis   
            elif "how are you" in self.query:
                rep=['I am fine.','I am full of energy.','I am always good.']
                speak(random.choice(rep))
                speak("And what about you sir?")
                print("And what about you sir?")
            
    # Saying Thank you to jarvis
            elif "Thank You" in self.query or "thank you" in self.query or "thanks" in self.query:
                rep=['Welcome Sir.','Your Welcome Sir.','Well you know Sir im cool.','No Need of that.','By the way I should thank you for creating me.','I am always ready to help you.']
                speak(random.choice(rep))

    # jarvis replying to hello
            elif "I am also fine " in self.query or "fine" in self.query or "good" in self.query or "full of energy" in self.query:
                speak("That's really nice Sir. So what to do now? I am ready for your command Sir!!.") 
                print("That's really nice Sir. So what to do now? I am ready for your command Sir!!.") 

            elif "Hello Jarvis" in self.query or "hello jarvis" in self.query or "Hey Jarvis" in self.query or "hey jarvis" in self.query:
                rep=['Hello Sir.','hello sir.','hey sir.','Hey Sir.','Ya Hi sir.','ya hi sir.','Hi Sir','hi sir']
                speak(random.choice(rep))

    # To know the name of jarvis
            elif "what is your name" in self.query or "tell me your name" in self.query:
                speak("Sir, My name is Jarvis.")
                print("Sir, My name is Jarvis.")

    # To know about jarvis
            elif "tell me about yourself jarvis" in self.query or "give your introduction" in self.query or "give your intro" in self.query or "tell me about yourself" in self.query:
                speak("My name is Jarvis and I am a personal assistance of Vedansh Ruhela.")
                speak("Ok, so now let me start by the time when I was developed.")
                speak("Vedansh, my developer was thinking to make a perfect personal assistant and then he made me and gave me a name JARVIS.")
                speak("And then slowly I started learning and doing various tasks like opening websites, apps, playing music and many more.")
                speak("And now I am capable of doing each and every tasks that you want me to do.")
                print("My name is Jarvis and I am a personal assistance of Vedansh Ruhela.")
                print("Ok, so now let me start by the time when I was developed.")
                print("Vedansh, my developer was thinking to make a perfect personal assistant and then he made me and gave me a name JARVIS.")
                print("And then slowly I started learning and doing various tasks like opening websites, apps, playing music and many more.")
                print("And now I am capable of doing each and every tasks that you want me to do.")

    # To know about the developer of jarvis
            elif "tell me about your developer" in self.query or "who made you" in self.query or "who developed you" in self.query or "tell me about vedansh" in self.query:
                speak("Vedansh is my developer my teacher the one who taught me how be a good, wise and smart personal assistant.")
                print("Vedansh is my developer my teacher the one who taught me how be a good, wise and smart personal assistant.")  

    # To know that how jarvis was developed
            elif "how were you developed" in self.query or "how were you made" in self.query:
                speak("Sorry sir, This is highly confidential and I am not allowed to tell you that.")
                print("Sorry sir, This is highly confidential and I am not allowed to tell you that.")

    # To open youtube.com
            elif 'open youtube' in self.query:
                url = 'youtube.com'
                chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)

    # To open google.com
            elif 'open google' in self.query:
                url = 'google.com'
                chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)

    # To open stackoverflow.com
            elif 'open stack overflow' in self.query or "open stackoveflow" in self.query:
                url = 'stackoverflow.com'
                chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url) 

    # To open github.com            
            elif 'open github' in self.query:
                url = 'github.com'
                chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)           

    # To play music    
            elif 'play music' in self.query:
                webbrowser.open("https://www.youtube.com/watch?v=G0Hx6uN2AJE&list=PLHuHXHyLu7BEnMJNeVvkXpxapvDSp5UdI")

    # To know the time
            elif 'the time' in self.query or "time" in self.query:
                strTime = datetime.datetime.now().strftime("%I:%M:%S")
                speak(f"Sir, the time is {strTime}.")
                print(strTime)

    # To open vs code 
            elif 'open vs code' in self.query:
                codePath = "C:\\Users\\Vedansh Ruhela\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                speak('vs code opened.')
                print('vs code opened.')
 
    # To close vs code
            elif 'close vs code' in self.query:
                codePath = "C:\\Users\\Vedansh Ruhela\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.system("TASKKILL /F /IM code.exe")  
                speak('vs code closed.')
                print('vs code closed.')

    # To open ms teams
            elif 'open teams' in self.query:
                codePath = "C:\\Users\\Vedansh Ruhela\\AppData\\Local\\Microsoft\\Teams\\previous\\Teams.exe"
                os.startfile(codePath)
                speak('teams opened.')
                print('teams opened.')

    # To close teams
            elif 'close teams' in self.query:
                codePath = "C:\\Users\\Vedansh Ruhela\\AppData\\Local\\Microsoft\\Teams\\previous\\Teams.exe"
                os.system("TASKKILL /F /IM Teams.exe")  
                speak('teams closed.')  
                print('teams closed.')

    # To open filmora 9 
            elif "open filmora 9" in self.query:
                codePath = "C:\\Program Files\\Wondershare\\Filmora9\\Wondershare Filmora9.exe"
                os.startfile(codePath)
                speak('filmora 9 opened.')
                print('filmora 9 opened.')

    # To close filmora 9 
            elif "close filmora 9" in self.query:
                codePath = "C:\\Program Files\\Wondershare\\Filmora9\\Wondershare Filmora9.exe"
                os.system("TASKKILL /F /IM Teams.exe") 
                speak('filmora 9 closed.')
                print('filmora 9 closed.')
                
    # To open chrome
            elif 'open chrome' in self.query:
                codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codePath)
                speak('chrome opened.')
                print('chrome opened.')

    # To close chrome
            elif 'close chrome' in self.query:
                codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.system("TASKKILL /F /IM chrome.exe") 
                speak('chrome closed.')   
                print('chrome closed.')

    # To open epic games 
            elif 'epic games' in self.query:
                codePath = "D:\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
                os.startfile(codePath) 
                speak('epic games opened.')
                print('epic games opened.')

    # To close epic games
            elif 'close epic games' in self.query:
                codePath = "D:\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
                os.system("TASKKILL /F /IM EpicGamesLauncher.exe") 
                speak('epic games closed.')      
                print('epic games closed.') 

    # To open cmd
            elif 'open cmd' in self.query:
                codePath = "C:\\Users\\Vedansh Ruhela\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
                os.startfile(codePath)
                speak('cmd opened.')
                print('cmd opened.')

    # To close cmd
            elif 'close cmd' in self.query:
                codePath = "C:\\Users\\Vedansh Ruhela\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
                os.system("TASKKILL /F /IM cmd.exe") 
                speak('cmd closed.') 
                print('cmd closed.') 

    # To open notepad
            elif 'open notepad' in self.query:
                codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
                os.startfile(codePath)
                speak('notepad opened.')
                print('notepad opened.')

    # To close notepad
            elif 'close notepad' in self.query:
                codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
                os.system("TASKKILL /F /IM notepad.exe")
                speak('notepad closed.')
                print('notepad closed.')

    # To know a joke
            elif 'tell me a joke' in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
                print(joke)

    # To know the news
            elif 'tell me the news' in self.query or "news" in self.query:
                speak('Please wait sir. I am fetching the latest news.')
                news()
                print(news())

    # To check the internet speed
            elif "check the speed" in self.query or "check the internet speed" in self.query or "internet speed" in self.query or "speed" in self.query:
                speak("Ok sir, Please wait I am checking the internet speed.")
                print("Ok sir, Please wait I am checking the internet speed.")
                import speedtest
                test = speedtest.Speedtest()
                down_speed=test.download()/10**6
                up_speed=test.upload()/10**6
                speak(f"Sir, Download speed is {down_speed:.2f} Mbps. \nUpload speed is {up_speed:.2f} Mbps.")
                print(f"Sir, Download speed is {down_speed:.2f} Mbps. \nUpload speed is {up_speed:.2f} Mbps.")

    # To know my current location
            elif "where am i" in self.query or "where we are" in self.query or "where i am" in self.query:
                speak("Wait a minute sir, Let me check.")
                try:
                    ipAdd = requests.get("https://api.ipify.org").text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f'Sir, I think we are in {city} city of {country} country.')
                    print(f'Sir, I think we are in {city} city of {country} country.')
                except Exception as e:
                    speak("Sorry Sir, due to unavailability of internet I am unable to find where we our.")
                    pass  

    # To set an alarm
            elif 'set an alarm' in self.query or "set alarm" in self.query or "alarm" in self.query:
                speak("For what time should I set the alarm?")
                tt = self.takeCommand()
                # tt = tt.replace("set alarm to ", "")
                tt = tt.replace(".","")
                tt = tt.upper()
                import MyAlarm
                MyAlarm.alarm(tt) 

    # To set the volume
            elif "volume down" in self.query:
                pyautogui.press("volumedown")

            elif "volume up" in self.query:
                pyautogui.press("volumeup") 

            elif "volume mute" in self.query or "mute" in self.query: 
                pyautogui.press("volumemute")

            elif "volume unmute" in self.query or "unmute" in self.query:
                pyautogui.press("volumeunmute")   

    # To take a screenshot            
            elif 'take a screenshot' in self.query or 'take screenshot' in self.query or "screenshot" in self.query:
                speak("Sir, Please tell me a name for this file to be saved.")
                name = self.takeCommand()
                speak("Ok sir I am taking the screenshot. Please Do not do any other action.")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak(f"I have taken the screenshot sir and saved it with the name {name} in our main directory.")
                try:
                    speak("should i show it to you")
                    print("should i show it to you")
                    self.reply=self.takeCommand()
                    if "yes" in self.reply:
                        im = Image.open(f"{name}.png")
                        im.show()
                    elif "no" in self.reply:
                        ans=["No Problem","Never Mind","Ok, next command sir."]
                        speak(random.choice(ans))
                except Exception as e:
                    speak("Sir, I am facing problem listening.")
                    print("Sir, I am facing problem listening.")   

    # To open camera
            elif "open camera" in self.query:
                speak("Ok sir, opening camera.")
                print("Ok sir, opening camera.")
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

    # To read a pdf
            elif 'read the pdf' in self.query:
                pdffiles()

    # To switch the current windows            
            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

    # To hide/unhide files 
            elif 'hide the files' in self.query or 'hide all the files in this folder' in self.query or "hide all the files of this folder" in self.query or "hide the file" in self.query or "hide" in self.query:
                condition = self.takeCommand()
                os.system("attrib +h /s /d")
                speak("Sir, all the files in this folder are hidden now.")

            elif 'unhide all the files of this folder' in self.query or 'unhide files' in self.query or "unhide" in self.query or "unhide the files" in self.query or "unhide file" in self.query or "unhide all the files in this folder" in self.query:
                condition = self.takeCommand()
                os.system("attrib -h /s /d")
                speak("Sir, all the files in this folder are unhidden now.")

    # To search anything on google
            elif "search google" in self.query or "google" in self.query:
                speak("Search activated. Sir, What do you want to search on google?.")
                how = self.takeCommand()
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)    

    # To know the current temperature
            elif "temperature" in self.query:
                search = "what is the temperature?"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"The Current Temperature outside is {temp}.")
                print(f"The Current Temperature outside is {temp}.")

    # To check the battery level
            elif "what is the battery level" in self.query or "battery" in self.query:
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"System current battery level is {percentage} percent.")
                print(f"System current battery level is {percentage} percent.")
                if percentage>=75:
                    speak("Sir, system have enough battery level to rock and roll.")
                    print("Sir, system have enough battery level to rock and roll.")
                elif percentage>=40 and percentage<=75:
                    speak("Sir, system have enough battery level but I would suggest you to connect to charger.")
                    print("Sir, system have enough battery level but I would suggest you to connect to charger.") 
                elif percentage>=15 and percentage<=30:
                    speak("Sir, system have less battery, I would recommend you connecting to the charger.")
                    print("Sir, system have less battery, I would recommend you connecting to the charger.")    
                elif percentage<=15:
                    speak("Sir, system do not have battery to work. Please connect to the charger or else I will shutdown the system.")
                    print("Sir, system do not have battery to work. Please connect to the charger or else I will shutdown the system.") 

    # To do calculations
            elif "calculations" in self.query or "do some maths" in self.query or "maths" in self.query or "calculate" in self.query or "maths" in self.query:
                try:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        speak("Sir, tell me what to calculate, example 2 plus 2.")
                        print("listening...")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    my_string=r.recognize_google(audio)
                    print(my_string)
                    def get_operator_fn(op):
                        return {
                            '+' : operator.add,
                            '-' : operator.sub,
                            'x' : operator.mul,
                            'divided' :operator.__truediv__,
                            }[op]
                    def eval_binary_expr(op1, oper, op2):
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)
                    speak("Sir,The answer is ")   
                    speak(eval_binary_expr(*(my_string.split())))
                    print("Sir,The answer is ") 
                    print(eval_binary_expr(*(my_string.split()))) 
                except Exception as e:
                    speak('Sir, I am having error while calculating')
                    print('Sir, I am having error while calculating')    
                    return "none"    

    # To type my words
            elif "type" in self.query:
                speak("okay i am listening sir. Please start speaking.")
                pyautogui.typewrite(self.takeCommand())       

    # To select everything
            elif "select all" in self.query:
                pyautogui.hotkey('ctrl','a')

    # To close a window
            elif "close this window" in self.query:
                pyautogui.hotkey('alt','f4')

    # To open a new tab
            elif "open a new window" in self.query:
                pyautogui.hotkey('ctrl','n')

    # To open a new incognitive window
            elif "open a new incognitive window" in self.query or "open a new incognito window" in self.query or "new icognito window" in self.query:
                pyautogui.hotkey('ctrl','shift','n')

    # To copy anything
            elif "copy" in self.query:
                pyautogui.hotkey('ctrl','c')
                speak("text copied to clipboard.")
                print("text copied to clipboard.")

    # To paste anything
            elif "paste" in self.query:
                pyautogui.hotkey('ctrl','v')

    # To undo anything
            elif "undo" in self.query:
                pyautogui.hotkey('ctrl','z')

    # To redo anything
            elif "redo" in self.query:
                pyautogui.hotkey('ctrl',)

    # To save anything
            elif "save" in self.query:
                pyautogui.hotkey('ctrl','s')

    # To go back
            elif "back" in self.query:
                pyautogui.hotkey('browserback')

    # To go up
            elif "go up" in self.query:
                pyautogui.hotkey('pageup') 

    # To go to top
            elif "go to top" in self.query:
                pyautogui.hotkey('home')

    # To open a new chrome tab
            elif "open a new tab" in self.query or "new tab" in self.query:
                pyautogui.hotkey('ctrl','t') 

    # To close chrome tab
            elif "close this tab" in self.query:
                pyautogui.hotkey('ctrl','w') 

    # To switch between chrome tabs
            elif "switch the tab" in self.query:
                pyautogui.hotkey('ctrl','shift','tab') 

    # To reopen closed chrome tab
            elif "open that tab again" in self.query or "open my recent tab" in self.query:
                pyautogui.hotkey('ctrl','shift','t')

    # To open this pc
            elif "open this pc" in self.query or "open file explorer" in self.query:
                pyautogui.hotkey('win','e') 

    # To open settings
            elif "open settings" in self.query:
                pyautogui.hotkey('win','i') 

    # To quickly close all windows
            elif "quickly close all windows" in self.query or "close all windows" in self.query or "minimize all windows" in self.query:
                pyautogui.hotkey('win','d')            

    # To open run
            elif "open run" in self.query:
                pyautogui.hotkey('win','r')

    # To delete something
            elif "delete" in self.query:
                final=self.query.split("delete")
                os.system("del "+final[1])

    # To repeat my speech
            elif "repeat me" in self.query or "repeat" in self.query:
                repeatmyspeech()          

    # To make a note of something
            elif "make a note" in self.query or "write this down"  in self.query or "remember this" in self.query:
                NOTE_STRS = ["make a note", "write this down", "remember this"]
                for phrase in NOTE_STRS:
                    if phrase in self.query:
                        speak("What would you like me to write down?. ")
                        print("What would you like me to write down?. ")
                        write_down = self.takeCommand()
                        note(write_down)
                        speak("I've made a note of that.")
                        print("I've made a note of that.") 
                break             

    # To lock the pc
            elif "lock the pc" in self.query or "lock" in self.query:
                ctypes.windll.user32.LockWorkStation()

    # To shutdown the pc
            elif 'shutdown the pc' in self.query:
                os.system("shutdown /s /t 5")
                
    # To restart the pc
            elif 'restart the pc' in self.query: 
                os.system("shutdown /r /t 5")    

    # To sleep the pc
            elif 'sleep the pc' in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                    
    # To close the program
            elif 'go to sleep' in self.query:
                speak('Thank you for using me Sir. Now I am going to sleep but you can wake me up anytime.')
                print('Thank you for using me Sir. Now I am going to sleep but you can wake me up anytime.')
                break   
            
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.runbutton.clicked.connect(self.startTask)
        self.ui.exitbutton.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("7LP8.gif")
        self.ui.background.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Jarvis_Loading_Screen.gif")
        self.ui.loadinggif.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(300)
        startExecution.start()

    def showTime(self):
        QApplication.processEvents()
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)  
        self.ui.time.setText(label_date)
        self.ui.date.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_()) 

