import pyttsx3  #A python library that will help us to convert text to speech.It works offline.

import speech_recognition as sr #before takecommand install this.

import datetime #To provide current or live time to A.I., we need to import a module called datetime
import wikipedia
import webbrowser#To open any website, we need to import a module called webbrowser.inbuilt no need to
import os
import smtplib#simple mail transfer protocol.
#An instance method called sendmail is present in the SMTP module. This instance method allows us to send an email.  

import subprocess as sp




engine=pyttsx3.init('sapi5')#sapi5=ms developed speech API.helps in synthesis &recognition of voice.
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)#..voice[0].id=male voice,voice[1].id=female voice.





def speak(audio):     #this function take the audio as a argument and then pronounce it.
    engine.say(audio)
    engine.runAndWait()#without this command ,speech will not be audible to us.

def wishMe():
    hour=int (datetime.datetime.now().hour)#tored the current hour or time integer value into a variable named hour. 
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    
    speak(" Hello I am Jarvis    Please tell me how may i help you")
    
def takeCommand():
    #take the command with the help of microphone of the system.return output in string.
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')#using google for voice recognition.
        print(f"User said: {query}\n")#user query will be printed.
        
    except Exception as e:
        print(e) #if you don't want to show error on the terminal then remove this line
        
        print("Say that again please...")#this line printed in case of improper voice
        return "None" #none string will be returned.
    return query

# def new_func(r):
#     r.pouse_threshold=1
def sendEmail(do,content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.strttls()
    server.login('sakshinavalkar1@gmail.com','your-password')
    server.sendemail('sakshinavalkar1@gmail.com', to, content)
    server.close()
    
if __name__=="__main__":
   # speak("sakshi is good girl")
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower() #convert user query into lowercase.
        
        #logic for executing task based query.
        if 'wikipedia' in query: #if wikipedia found in the query then this block will be executed.
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
    
        # # elif 'play music' in query:
        # #     music_dir=
        # #     songs=os.listdir(music_dir)
        # #     print(songs)
        # #     os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")
            
        # elif 'open code' in query:
        #     codePath="C:\\Users\\saksh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)
        elif 'email to sakshi' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                
                to="sakshinavalkar1@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sakshi my friend.i am not able to send this email")
        elif 'open camera' in query:
            def open_camera():
                sp.run('start microsoft.windows.camera:',shell=True)
            
    

