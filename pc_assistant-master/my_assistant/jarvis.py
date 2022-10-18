import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import sys
from playsound import playsound
import smtplib
import psutil
import pyautogui
from diction import translate
from loc import weather
from youtube import youtube
import psutil
import pyjokes
from sys import platform
import os
import winshell
import getpass
import subprocess
import glob
import random
#from news import short_news
from news import full_news
from datetime import datetime
import datetime
import time


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def screenshot():
    now=datetime.datetime.now()
    date_time=now.strftime("%Y-%m-%d ,%H-%M-%S")
    img=pyautogui.screenshot()
    img.save(r'C:\\Users\\user\\Pictures\\screenshot\\'+str(date_time)+'.png')
    speak('sir do you wanna see this screenshot')
    message=takeCommand().lower()
    if 'yes' in message or 'of course' in message or 'why not' in message:
        os.startfile('C:\\Users\\user\\Pictures\\screenshot\\'+str(date_time)+'.png')
    elif 'no' in message:
        speak('okay! no problem sir')
    else:
        speak("done sir!")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)



def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.0)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print(e)
        print('Say that again please...')
        return 'None'
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning SIR")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon SIR")
    else:
        speak('Good Evening SIR')
    weather()
    time.sleep(0.5)
    speak(' Please command me')



def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])


if __name__ == '__main__':

    if platform == "linux" or platform == "linux2":
        chrome_path = '/usr/bin/google-chrome'

    elif platform == "win32":
        chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    else:
        print('Unsupported OS')
        exit(1)
        
while True:
    command=takeCommand().lower()
    if 'start' in command:
        playsound('E:\\c\\my_assistant\\sound\\generator.mp3')
        time.sleep(1.5)
        speak('sorry sir! ,engine is not starting ')
        time.sleep(0.5)
        speak('please try again to start engine')
    elif 'turn on' in command or 'turn on your ' in command or 'please' in command:
        playsound('E:\\c\\my_assistant\\sound\\generator.mp3')
        speak('engine started ,now command me to set up sir!')
        print('im listening !')
        while True:
            query = takeCommand().lower()
            if 'set up' in query or 'setup' in query or 'please' in query or 'shut up' in query:
                speak("okay sir!")
                exec(open('E:\\c\\my_assistant\\blackwallpaper.py').read())
                time.sleep(2.0)
                os.system('taskkill /im Nexus.exe /f')
                time.sleep(2.0)
                os.startfile('C:\\Program Files\\Rainmeter\\Rainmeter') 
                playsound('E:\\c\\my_assistant\\sound\\welcome.mp3')
                time.sleep(0.5)
                playsound('E:\\c\\my_assistant\\sound\\conected.mp3')
                time.sleep(0.5)
                webbrowser.register(
                    'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                wishMe()
                while True:
                    query = takeCommand().lower()
                    if 'wikipedia' in query:
                        speak('Searching Wikipedia....')
                        query = query.replace('wikipedia', '')
                        results = wikipedia.summary(query, sentences=2)
                        speak('According to wikipedia ')
                        print(results)
                        speak(results)

                    elif 'youtube downloader' in query or 'download youtube' in query:
                        exec(open('E:\c\my_assistant\youtube_downloader.py').read())
                    
                    elif 'who are you' in query:
                        speak("im your assistant sir!")
                    
                    elif 'nice' and 'cool'in query:
                        speak('thank you sir')

                    elif 'are you there' in query:
                        speak("Yes Sir,always at your service")

                    elif 'open youtube' in query:
                        webbrowser.get('chrome').open_new_tab('https://youtube.com')
                    elif 'meeting' in query:
                        speak("opening your meeting ")
                        webbrowser.get('chrome').open_new_tab('https://meet.google.com/')
                        speak('please enter your meeting code sir')
                    
                    elif'test' in query:
                        speak('ok sir')
                        webbrowser.get('chrome').open_new_tab('https://www.iemcrp.com/')
                        speak('please choose your college yourself')
                        speak('im not able to take you forword, sorry sir!')

                    elif'open whatsapp' in query:
                        speak("opening whatsapp")
                        webbrowser.get('chrome').open_new_tab('https://web.whatsapp.com/')

                    elif'open mail' in query:
                        speak("opening your mail")
                        webbrowser.get('chrome').open_new_tab('https://mail.google.com/mail/u/0/#inbox')

                    elif'create mail' in query:
                        speak("creating your mail sir ")
                        webbrowser.get('chrome').open_new_tab('https://mail.google.com/mail/u/0/#inbox?compose=new')
                    elif'classroom' in query:
                        speak("opening your google classroom ")
                        webbrowser.get('chrome').open_new_tab('https://classroom.google.com/h')
                    elif 'cpu' in query:
                        cpu()
                    
                    elif 'hello' in query:
                        speak("yes sir!")

                    elif 'joke' in query:
                        joke()

                    elif 'screenshot' in query:
                        speak("taking screenshot")
                        screenshot()


                    elif 'open google' in query:
                        webbrowser.get('chrome').open_new_tab('https://google.com')

                    elif 'open weather' in query:
                        speak("opening weather")
                        webbrowser.get('chrome').open_new_tab('https://www.google.com/search?q=today+weather&sxsrf=ALeKk01aqodlWN6ZQ_mNE6906_49VnM5Zw%3A1624380711931&ei=JxXSYKmtOIWP4-EPpNOcsAk&oq=today+weather&gs_lcp=Cgdnd3Mtd2l6EAMyCwgAELEDEIMBEJECMgUIABCRAjIFCAAQkQIyBQgAEJECMgsIABCxAxCDARCRAjIICAAQsQMQgwEyAggAMgUIABCxAzICCAAyBQgAELEDOgcIABBHELADUIFYWItxYP2IAWgAcAJ4AYABsCCIAZqCAZIBAzktNZgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=gws-wiz&ved=0ahUKEwjp3MHa2avxAhWFxzgGHaQpB5YQ4dUDCA4&uact=5&dlnr=1&sei=PhXSYKmGG_-C4-EPxoCVkAQ')


                    elif'empty recycle bin' in query or 'clear recycle bin' in query:
                        winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=False)
                        speak("recycle data is cleared now.")

                
                    elif 'play music' in query or 'next' in query:
                        #exec(open('E:\c\my_assistant\mediaplayer.py').read())
                        music_dir='E:\\SONGS\\Arajit singh song'
                        songs=os.listdir(music_dir)
                        #print(songs)
                        n=random.randint(0,50)
                        os.startfile(os.path.join(music_dir,songs[n]))

                    elif 'play video'in query or 'video' in query:
                        speak('okay sir , i am playing video')
                        video_dir='E:\\video songe'
                        video=os.listdir(video_dir)
                        n=random.randint(0,30)
                        os.startfile(os.path.join(video_dir,video[n]))

                    elif 'search youtube' in query:
                        speak('What you want to search on Youtube?')
                        youtube(takeCommand())

                    elif 'time' in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak('Sir, the time is {strTime}')
                        
                    elif 'search' in query:
                        speak('What do you want to search for?')
                        search = takeCommand()
                        url = 'https://google.com/search?q=' + search
                        webbrowser.get('chrome').open_new_tab(url)
                        speak('Here is What I found for' + search)

                    elif 'location' in query:
                        speak('opening location')
                        location = takeCommand()
                        url = 'https://google.nl/maps/place/' + location + '/&amp;'
                        webbrowser.get('chrome').open_new_tab(url)
                        speak('Here is the location ' + location)

                    elif 'function' in query:
                        speak("sir im your assistant the most advance assistant ,i can search location,i can search on google i can open youtube,also i can  send email i can play music take a screenshort and may more. ")

                    elif 'your master' in query:
                        speak('prajanand kumar  is master ')

                    elif 'open photoshop' in query:
                        if platform == "win32":
                            os.startfile("Photoshop.exe")
                        elif platform == "linux" or platform == "linux2" or "darwin":
                            os.system('Photoshop.exe')

                    elif 'shutdown' in query:
                        if platform == "win32":
                            os.system('C:\\Program Files\\Rainmeter\\Rainmeter')
                            os.system('shutdown /p /f')
                        elif platform == "linux" or platform == "linux2" or "darwin":
                            os.system('poweroff')

                    elif 'cpu' in query:
                        cpu()

                    elif 'joke' in query:
                        joke()

                    elif 'screenshot' in query:
                        speak("taking screenshot")
                        screenshot()


                    elif 'remember that' in query:
                        speak("what should i remember sir")
                        rememberMessage = takeCommand()
                        speak("you said me to remember"+rememberMessage)
                        remember = open('data.txt', 'w')
                        remember.write(rememberMessage)
                        remember.close()

                    elif 'do you remember anything' in query:
                        remember = open('data.txt', 'r')
                        speak("you said me to remember that" + remember.read())
                    
                    elif 'calculator'in query:
                        if 'start' in query:
                            os.system('start calc.exe /f')
                    elif 'calculator'in query:
                        if 'stop' in query:
                            os.system('taskkill /im calc.exe /f')
                        
                    elif 'sleep' in query:
                        speak('okay sir,have a good day !')
                        exec(open('E:\c\my_assistant\wallpaper.py').read())
                        os.system('taskkill /im Rainmeter.exe /f')
                        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\Programs\\Winstep\\nexus')
                        sys.exit()

                    elif 'bye' in query:
                        speak('bye sir ! take care')
                        exec(open('E:\c\my_assistant\wallpaper.py').read())
                        os.system('taskkill /im Rainmeter.exe /f')
                        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\Programs\\Winstep\\nexus')
                        sys.exit()
                    elif 'exit' in query:
                        speak('ok bye sir ! take care')
                        exec(open('E:\c\my_assistant\wallpaper.py').read())
                        os.system('taskkill /im Rainmeter.exe /f')
                        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\Programs\\Winstep\\nexus')
                        sys.exit()
                    elif 'thank you' in query:
                        speak("welcome sir!")

                    elif 'how are you' in query:
                        speak(" im fine sir!,all system are working properly")
                        time.sleep(2.0)
                        speak("how are you sir?")
                        
                    elif 'abort' in query or 'mission' in query:
                        speak('okay sir,good bye take care')
                        time.sleep(0.5)
                        speak('mission aborting')
                        exec(open('E:\c\my_assistant\wallpaper.py').read())
                        os.system('taskkill /im Rainmeter.exe /f')
                        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\Programs\\Winstep\\nexus')
                        sys.exit()
                    
                    elif query != ('exit music') and ('exit') in query:
                        queryword=query
                        stopwords=['exit']
                        querywords=queryword.split()
                        resultwords=[word for word in querywords if word.lower() not in stopwords]
                        result=''.join(resultwords)
                        os.system('taskkill /im ' + result + '.exe /f')
                        rand=[('closing' + result)]
                        speak(rand)
                    
                    
                    elif query != ('start music') and ('start') in query:
                        queryword=query
                        stopwords=['start']
                        querywords=queryword.split()
                        resultwords=[word for word in querywords if word.lower() not in stopwords]
                        result=''.join(resultwords)
                        os.system('start ' + result + '.exe')
                        rand=[('starting' + result)]
                        speak(rand)

                    elif 'type' in query or 'write' in query:
                        speak('what you want to type sir?')
                        write=takeCommand()
                        pyautogui.typewrite(write)


                    elif 'dictionary' in query:
                        speak('What you want to search in your intelligent dictionary?')
                        translate(takeCommand())

                    elif 'undo' in query:
                        speak('okay sir!')
                        pyautogui.hotkey("ctrl","z")
                    elif 'copy' in query:
                        speak('data copied')
                        pyautogui.hotkey("ctrl","c")
                    elif 'paste' in query:
                        pyautogui.hotkey("ctrl","v")
                        speak('data pasted')
                    elif 'new folder' in query:
                        pyautogui.hotkey("ctrl","Shift","N")
                    elif 'delete' in query:
                        speak('deleting..')
                        pyautogui.hotkey("shift","Delete")
                        speak('data deleted  sir!')
                    elif'left' in query:
                        pyautogui.press("left")
                    elif'right' in query:
                        pyautogui.press("right")
                    elif'up' in query:
                        pyautogui.press("up")
                    elif'down' in query:
                        pyautogui.press("down")
                    elif'double click' in query or 'double click' in query:
                        pyautogui.doubleClick()
                    elif 'click' in query:
                        pyautogui.click()
                    elif 'close current window' in query or 'close current tab' in query:
                        speak('closing current window')
                        pyautogui.hotkey("Alt","F4")
                        speak('window closed.')
                    elif 'task manager' in query:
                        speak('opening task manger')
                        pyautogui.hotkey("ctrl","Shift","Esc")
                    elif 'search file'in query:
                        speak('what you want to find sir!')
                        pyautogui.hotkey("Win","F")
                    elif 'enter' in query or 'inter' in query:
                        pyautogui.hotkey("ENTER")
                    elif 'switch tab' in query or 'which tab' in query :
                        speak('switching tab sir.')
                        pyautogui.hotkey("Alt","tab")
                    elif 'shift left' in query:
                        pyautogui.hotkey("Win","left")
                    elif 'shift right' in query:
                        pyautogui.hotkey("Win","right")
                    elif 'minimize all' in query or 'minimise all' in query or 'maximize all' in query or 'minimise all' in query:
                        pyautogui.hotkey("Win","d")
                        speak('done sir')
                    elif 'maximize' in query or 'maximise' in query:
                        pyautogui.hotkey("Win","Up")
                        speak('window maximized.')
                    elif 'restore' in query:
                        pyautogui.hotkey("Win","Down")
                    elif 'select all' in query:
                        pyautogui.hotkey("ctrl","A")
                    elif'save' in query:
                        pyautogui.hotkey("ctrl","S")
                    elif 'properties' in query:
                        speak('opening prperties')
                        pyautogui.hotkey("Alt","ENTER")
                    elif 'go back' in query or 'backspace' in query:
                        speak('okay sir.')
                        pyautogui.hotkey("Backspace")
                    elif'play' in query or 'pause' in query:
                        pyautogui.hotkey("playpause")
                    elif 'volumeup' in query or 'volume up' in query:
                        pyautogui.hotkey("volumeup")
                    elif 'volumedown' in query or 'volume down' in query:
                        pyautogui.hotkey("volumedown")
                    elif 'mute' in query:
                        pyautogui.hotkey("volumemute")
                    elif 'space' in query:
                    
                        pyautogui.hotkey("space")
                    elif 'news' in query:
                        speak('Ofcourse sir..')
                        speak('sir Do you want to listen the full news or short news ...')
                        test = takeCommand()
                        if 'full' in test:
                            full_news()
                        elif 'short' in test:
                            short_news()
                        else:
                            speak('No Problem Sir')
                    elif 'voice' in query:
                        if 'female' in query:
                            engine.setProperty('voice', voices[0].id)
                        else:
                            engine.setProperty('voice', voices[1].id)
                        speak("Hello Sir, I have switched my voice. How is it?")

                    elif 'email' in query:
                        speak("who is the sender")
                        sender=takeCommand()
                        if 'laptop' in sender:
                            try:
                                speak('please enter Email address of recipient.')
                                Recipient_user=input("user: ")
                                speak("what should i say ?")
                                content = takeCommand()
                                server = smtplib.SMTP('smtp.gmail.com',587)
                                server.ehlo()
                                server.starttls()
                                server.login("prem609461@gmail.com",'password')
                                server.sendmail('efgh87933@gmail.com' ,Recipient_user,content)
                                server.close()
                                speak('Email has been sent!')

                            except Exception as e:
                                speak('Sorry sir! Not able to send email at the moment')
            elif 'stop' in query:
                sys.exit()
            elif 'sleep' in query:
                sys.exit()
            elif 'dont' in query:
                sys.exit()
            else:
                takeCommand()
    elif 'mission' in command:
        speak('okay sir')
        sys.exit()
    else:
        takeCommand()

