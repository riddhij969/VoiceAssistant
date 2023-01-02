import pyttsx3 
import datetime
import speech_recognition as sr 
import wikipedia 
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >=12 and hour <18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
   

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say now")
        speak("Say now")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Getting")
        speak("Getting")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        
        print("Say that again please...")
        return "None"
    return query

def sendemail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("riddhij969@gmail.com",'#password')
    
    server.sendmail("riddhij969@gmail.com",to, content)
    server.close()

if __name__ == '__main__':
    
    wishme()
    
    while True:
   
        query =  takecommand().lower()


        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")
       

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'music play' in query:
            music_dir = 'E:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif'time' in query:
            instr = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"mam, the time is {instr}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Riddhi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email' in query:
            try:
                speak("what should i say?")

                to = 'riddhijain969@gmail.com'
                content = takecommand()
                sendemail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry my friend riddhi. i am not able to send this email.")

        else:
            print("Not getting")
            
