import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    print("I am Jarvis Sir. Please tell me how may I help you")
    speak("I am Jarvis Sir. Please tell me how may I help you")
    print(
        "System Info: system-started\nConnection to Internet: Connection Succeeded\nConnecting to Stelite No. 74: Done\n"
    )
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("Status: time = ", strTime)
    print("System Speed: 1Tb/s")
    print("Internet Speed: 1Gbps")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def closecmd():
    os.system('TASKKILL /F /IM chrome.exe')


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for command Input...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Identifying Command Input...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Voice Input : {query}\n")

    except Exception as e:
        # print(e)
        print("Sir please say that again I couldnt get It")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email_addreess@gmail.com', 'password')
    server.sendmail(dhangarjayashree51 @ gmail.com, to, content)
    server.close()


def multiplication():
    speak("PLease Enter the first Number")
    print("PLease Enter the first Number")
    a = takeCommand()
    a = int(a)
    speak("PLease Enter the second Number")
    print("PLease Enter the Second Number")
    b = takeCommand()
    b = int(b)
    product = a * b
    print("The prduct is ", product)
    speak(f"The answer is {product}")


def add():
    speak("PLease Enter the first Number")
    print("PLease Enter the first Number")
    a = takeCommand()
    a = int(a)
    speak("PLease Enter the second Number")
    print("PLease Enter the Second Number")
    b = takeCommand()
    b = int(b)
    sum = a + b
    print("The prduct is ", sum)
    speak(f"The answer is {sum}")


def minus():
    speak("Please Enter first number")
    print("Please Enter first number")
    a = takeCommand()
    a = int(a)
    speak("Please Enter second number")
    print("Please Enter second number")
    diff = a - b
    print("The difference of the numbers is ", diff)
    speak(f"The differnce is {diff}")


def devide():
    speak("Please Enter first number")
    print("Please Enter first number")
    a = takeCommand()
    a = int(a)
    speak("Please Enter second number")
    print("Please Enter second number")
    que = a / b
    print("The difference of the numbers is ", que)
    speak(f"The differnce is {que}")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #Logic for executing commands
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open my website' in query:
            webbrowser.open("https://codewithdhruva.github.io/MyWebsite/")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Prakash Dhangar\\Desktop\\My Projects\\Jarvis AI\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'close' in query:
            speak("What should I close")
            print("Waiting for the answer")
            if 'command prompt' in query:
                os.system('TASKKILL /F /IM cmd.exe')
            elif 'browser' in query:
                os.system('TASKKILL /F /IM chrome.exe')
            elif 'Browser' in query:
                os.system('TASKKILL /F /IM chrome.exe')
            elif 'code' in query:
                os.systen('TASKKILL /F /IM code.exe')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'open code' in query:
            print("Opening Code")
            speak("Opening Code")
            codePath = "C:\\Users\\Prakash Dhangar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open idea' in query:
            print("Opening IntelliJ Idea")
            speak("Opening IntelliJ Idea")
            ideaPath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.1.2\\bin\\idea64.exe"
            os.startfile(ideaPath)
        elif 'open studio' in query:
            print("Opening Android Studio")
            speak("Opening Android Studio")
            studioPath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(studioPath)
        elif 'play upgrade' in query:
            upgradePath = "C:\\Users\\Prakash Dhangar\\Desktop\\Programms\\Upgrade.mkv"
            speak("Playing Upgrade")
            os.startfile(upgradePath)
        elif 'send mail to prakash' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "itworldcs@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I couldnt send this Email")
        elif 'thank you' in query:
            speak(
                "At your service I am always there. I am glad that I could help you."
            )
        elif 'open teams' in query:
            teamsPath = "C:\\Users\\Prakash Dhangar\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams.ink"
            speak("Starting Teams")
            os.startfile(teamsPath)
        elif 'play old music' in query:
            webbrowser.open("https://youtu.be/kJIidWqWjUs?t=115")
        elif 'multiply' in query:
            multiplication()
        elif 'sum of' in query:
            add()
        elif 'devide' in query:
            devide()
        elif 'minus' in query:
            minus()
        elif 'sleep' in query:
            break
