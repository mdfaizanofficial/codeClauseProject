import pyttsx3
import speech_recognition as sr
import datetime
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
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<5):
        speak("Good afternoon")
    else:
        speak("Good evening")
        print("My name is Leena. Please tell me how may I help you.")
        speak("My name is Leena. Please tell me how may I help you.")

def takeCommand():
    # it takes microphone input from the user and returns string output: 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again Please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('alamfaizan173@gmail.com','Faizan@123')
    server.sendmail('alamfaizan173@gmail.com')
    server.close()


if __name__ == "__main__":
    # speak("Helllo, Good morning sir ")
    wishMe()
    while(True):
        query =takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=50)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'exit' in query:
            break
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open what\'s up' in query:
            webbrowser.open_new("whatsapp.com")
        elif 'open stackoverflow' in query:
            webbrowser.open_new("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'E:\\Hollywood\\New folder (2)\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'hello' in query:
            print("Hello, How are you ?")
            speak("Hello, How are you ?")
        elif 'hello how are you' in query:
            print("Hello,i'm good. what about you ?")
            speak("Hello,i'm good. what about you ?")
        elif 'how are you' in query:
            print("i'm good. what about you ?")
            speak("i'm good. what about you ?")
        elif 'i love you' in query:
            print("i love you two meri jaan")
            speak("i love you two meri jaan")
        elif 'time' in query:
            strTime = datetime.timedelta.now().strftime("%H:%M:%S")
            print(strTime)
            speak("sir, the time is ",strTime)
        elif 'vs code' in query:
           codePath = "C:\\Users\Salim Tyagi\\AppData\\Local\\Programs\\Microsoft VS Code"
           os.startfile(codePath)
        elif 'email to mujeeb' in query:
            try:
                speak("What should I say:")
                content = takeCommand()
                to = "mujeebtyagi14@gmail.com"
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                print("Sorry my friend. i'm not able to send this email")
        elif ('ayan aamir' or 'Ayaan Aamir' or 'ayaan aamir' or 'ayaan amir') in query:
            print("Ayan Aamir is a cute boy. His Father name is Aamir. He belongs to tyori 13 biswa(Ghaziabad).")