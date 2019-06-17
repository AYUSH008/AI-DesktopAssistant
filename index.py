import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning Mr.Ayush!")

    elif hour>=12 and hour<18:
        speak("Good afternoon Sir Mr.Ayush")

    else:
        speak("Good evening Sir")

    speak("I am Jarvis !Please tell me How may i help you sir?")

def takeCommand():
    
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening ......")
         r.pause_threshold = 1
         audio = r.listen(source)

     try:
         print("Recognizing.....")
         query = r.recognize_google(audio , language='en-in')
         print(f"user said :{query} \n")

     except Exception as e:
         print(e)

         print("say that again please")
         speak("sorry sir i think i have a problem in my ears would you please say that again")
         return "None"
     return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senders_email_id' , 'sender_password')
    server.sendmail('reciverId' , to , content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
    
        #logic
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'open geeksforgeeks' in query:
            webbrowser.open('geeksforgeeks.com')
        
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif ' play music ' in query:
            music_dir = 'C:\\Users\\AYUSH\\Desktop\\ct3 19\\Bharat songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" sir the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\AYUSH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to ayush' in query:
            try:
                speak("what should i say ")
                content  = takeCommand()
                to = "desintaion_email_id"
                sendEmail(to,content)
                speak("email has been sent sir!")
            except Exception as e:
                print(e)
                speak("sorry Mr. Ayush . i am not able to send your email sir")
        elif 'in google' in query:
            webbrowser.open("https://google.com/search?q=%s" % query)
        elif 'in youtube' in query:
            webbrowser.open("https://www.youtube.com/watch?v=%s" % query)