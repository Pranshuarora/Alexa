import speech_recognition as sr   
import pyttsx3    #speach #talk #text to speech
import pywhatkit  #for youtube music
import datetime   #time
import wikipedia  #Wiki 
import pyjokes    #jokes
import sys

# Install packages from PIP install in terminal and then can import here
  
listener=sr.Recognizer()
engine=pyttsx3.init()
#engine.say("I am your alexa")
#engine.say("What can I do for you")   
voices=engine.getProperty("voices")   
engine.setProperty("voice", voices[1].id) #declaring alexa voice boy/girl by index

 
def talk(text):
    engine.say(text)
    engine.runAndWait() #alexa run and wait to respond
    
def alexa_Command():
    try:
        with sr.Microphone() as source:     #microphone as source of listening
            print("Listening...")           #microphone started listening
            voice=listener.listen(source)
            Command=listener.recognize_google(voice) # send voice to google
            Command=Command.lower() 
            if "alexa" in Command:
                Command=Command.replace("alexa", "")    #alexa ommited from Command to print
                print(Command)
    except:
        pass
    return Command

def run_alexa():
    Command=alexa_Command()
    print(Command)
    if "play" in Command:
        song=Command.replace("play", "")
        talk("Playing" +song)
        pywhatkit.playonyt(song)    #play song from youtube
    elif "time" in Command:
        time=datetime.datetime.now().strftime("%H:%M")    #current time        
        print(time)        
        talk("Current time is"+time)            
    elif "superstar" in Command:
        person=Command.replace("superstar", "")
        info=wikipedia.summary(person, 2)  #inforamtion from wiki
        print(info)
        talk(info)
    elif "joke" in Command:
        person=Command.replace("joke", "")    
        talk(pyjokes.get_joke())     #joke from online
    elif "stop" in Command:
        sys.exit()
    
run_alexa()