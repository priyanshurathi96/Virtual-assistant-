
import speech_recognition as sr
import pyttsx3
import webbrowser


recognizer = sr.Recognizer()
engine = pyttsx3.init() #speech to text start 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    


if __name__ == "__main__":
    speak("Initializing anshul...")
    
    while True:
        # Listen for the  word "anshul"
        # Obtain audio from the microphone
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout = 50,phrase_time_limit = 50)
            word = r.recognize_google(audio)
            if(word.lower()=="anshul"):
                speak("yes")
                #listen for command 
                with sr.Microphone() as source:
                    print ("anshul active..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        
            

        except Exception as e:
            print("Error; {0}".format(e))
