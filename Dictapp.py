import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)  
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
dictapp = {"command prompt" : "cmd" , "paint" : "paint" , "word" : "winword" , "excel" : "Excel" , "chrome" : "chrome" , "vscode" : "code" , "power point" : "powerpnt"}

def openappweb(query):
    speak("Launging...")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace( "open", "")
        query = query.replace( "jarvis", "")
        query = query.replace( "launch", "")
        query = query.replace( " ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")
                
def closeappweb(query):
    speak("Closing...")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed.")
    elif "2 tab" or "to tab" or "two tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed.")
    elif "3 tab" or "three tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed.")
    elif "4 tab" or "four tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed.")
    elif "5 tab"or "five tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed.")
    
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
        
