import os
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Sifat, I am your personal assistant. How can I help you?")

def takeVoice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Wait a moment...")
        query = r.recognize_google(audio, language='en-US')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Please say again.")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeVoice().lower()

        if 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("From wikipedia,")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'who is tuntuni' in query:
            speak("The lucky girl you love is tuntuni. And I am jealous of her.")

        elif 'jealous of her' in query:
            speak("because you love her. but now i love you.")

        elif 'play music' in query:
            music_dir = 'D:\\Entertainment\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'cute friend' in query:
            speak("her name is, mohanqian. she is a fantastic girl, from guizhou province.")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

