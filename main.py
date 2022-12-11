import random
import os
import sys
from sys import path
import speech_recognition as sr
import pyttsx3
import webbrowser as web
import speedtest 
import datetime
import pywhatkit as kt
from selenium import webdriver


speed=speedtest.Speedtest()

engine = pyttsx3.init()

                
voices = engine.getProperty('voices')     
engine.setProperty('voice', voices[1].id) 

engine.say("Hi, I'm Bruno the bot. Please tell me how I can help you.")
engine.runAndWait()


r = sr.Recognizer()
while True:




 with sr.Microphone() as source:
        print('What can I do for you?')
        text = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=1)
            
        try:
            recognizedtext = r.recognize_google(text)
            
        except sr.UnknownValueError:
            print("Sorry, I couldn't get that. Please check your microphone.")
        except sr.RequestError:
            print("Sorry, I'm facing technical issues. Please try again later.")
            
        # Task1: Searching Google via Voice Commands
        if "search google" in recognizedtext.lower(): 
            print("What can I search for you?")
            user_query = input("Please enter your search query here: ")
            kt.search(user_query)
            print("Voice command: "+ recognizedtext)
        
        
            # Task2: Exiting from a Try block via Voice Commands
        elif "exit" in recognizedtext.lower():
            print("Voice command: "+recognizedtext)
            sys.exit()
        
        
            # Task3: Checking Internet Speeds via Voice Commands
            
        elif "internet speed" in recognizedtext.lower():
            print("Voice command: "+ recognizedtext)
            print("Upload Speed: ",speed.upload())             #upload speed 
            print("Download Speed: ",speed.download())         #download speed
                
                
            # Task 4: Date 
        elif "time" in recognizedtext.lower():
            date=datetime.datetime.now()
            print("Voice command: "+ recognizedtext)
            print("The time is: "+date.strftime("%c"))     # Date
            
            # Task 5: Time
        elif "date" in recognizedtext.lower():
            date=datetime.datetime.now()
            print("Voice command: "+ recognizedtext)
            print("The date is: "+date.strftime("%c"))
        
            # Task 5: Jokes
        elif "joke" or "jokes" in recognizedtext.lower():
            print("Voice command: "+ recognizedtext)
            engine.say("I'm talking to one")
            engine.runAndWait()
           
            # Task 6: Conversation
        elif "What's your name" in recognizedtext.lower():
            print("Voice command: "+ recognizedtext)
            engine.say("My name is Harley")
            engine.runAndWait()
        elif "What's on my schedule" in recognizedtext.lower():
            print("Voice command: "+ recognizedtext)
            engine.say("You don't have a schedule")
            engine.runAndWait()
        elif "Hi" or "Hiya" or "Hello" or "Yo" in recognizedtext.lower():
            engine.say("Howdy?") 
            
        else:
            print("Can't answer your question, sorry")