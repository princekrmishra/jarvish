import pyttsx3
import speech_recognition as sr
import datetime 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voice[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!, Prince")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!, Prince")
    else:
        speak("Good Evening!, Prince")
    speak("I am Jarvis your assistant, how can I help you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print("user said: {query}\n")
        
    except Exception as e:
     #   print(e)
        speak("Sorry, I didn't get that. Please try again")
        return "None"
    return query
    
if __name__ == "__main__":
    wishMe()
    takeCommand()
    