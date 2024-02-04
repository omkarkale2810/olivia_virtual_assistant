import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice' , voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# this function check time from datetime and wish according to it 
def wishme():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour < 12:
        speak("good morning omkar")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon omkar")
    else:
        speak("Good evening omkar")  
    speak("Myself Olivia , how can i help you")    

def introduce():
    speak("now me to introduce myself . i am olivia a virtual artificial intelegence , and i am here to assist you variety of tasks i can , 24 hours a day , 7 days a week .   ")

def fine():
    speak("i am good what about you ")

# this function listen audio and google recognize the audio and convert it into string
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)  # Adjust the timeout as needed (5 seconds in this example)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except sr.WaitTimeoutError:
            print("Listening timeout. No speech detected.")
            return "None"
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio.")
            return "None"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "None"

if __name__ == "__main__":
    wishme()
    while True :
        # khalchi line speak kelel la lower case string madhe convert kart 
        query = takecommand().lower()
        # ata logic lihaycha jar apan bollo tyanusar reply bhetayla
        
        if 'wikipedia' in query :
            speak("searching in wikipedia...")
            # jar apan bollo tyamadhe wikipedai asa shabd asel tr ya if madhe jael 
            query =query.replace("wikipedia","")
            # query ya string madhun wikipedia shabd kadhun takle replace by "" 
            results = wikipedia.summary(query, sentences=3)
            print("Accordinng to wikipedia")
            speak(results)

        elif 'bye' in query :
            speak("bye bye . have a good day.")
            break    
        
        elif 'who are you' or 'about yourself' in query:
            introduce()

        elif 'how are you' in query:
            fine()    

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            break
        elif 'open chatgpt' in query:
            webbrowser.open('chat.openai.com')
            break
        elif 'open google' in query:
            webbrowser.open('google.com')   
            break 
        elif 'open gfg' in query:
            webbrowser.open('geeksforgeeks.com')
            break
        elif 'open codeforces' in query:
            webbrowser.open('codeforces.com')
            break
        elif 'open leetcode' in query:
            webbrowser.open('leetcode.com')
            break
        elif 'open hackerrank' in query:
            webbrowser.open('hackerrank.com')
            break


