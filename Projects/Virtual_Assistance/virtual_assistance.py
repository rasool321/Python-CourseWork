#pip install pyttsx3 SpeechRecognition pyaudio
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1

        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio,language='en-in')
            print("🗣️ You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Sorry, I didn't understand.")
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("❌ Speech service error.")
            speak("Sorry, my speech service is down.")
            return ""

# Function to respond to voice commands
speak("Hello! I'm your virtual assistant. How can I help you?")
while True:
    command = listen()
    if 'time' in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif 'play music' in command:
        speak('Okay, Music is playing...')

    elif 'politics' in command:
        speak('Geopolitics usually refers to countries and relations between them; '
                  'it may also focus on two other kinds of states: de facto independent '
                  'states with limited international recognition and relations between '
                  'sub-national geopolitical entities.')

    elif 'remainder' in command:
        speak('Push your code to GitHub')

    elif 'alarm' in command:
        speak('Set alarm feature is not available yet.')

    elif 'date' in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today\'s date is {today}")

    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'open codegnan' in command:
        speak("Opening Codegnan website")
        webbrowser.open("https://codegnan.com/")

    elif 'your name' in command:
        speak("I am your Python assistant!")

    elif any(word in command for word in ['stop', 'exit', 'bye']):
        speak("Okay bye bye! Have a good day")
        break

    elif command.strip() == "":  # ignore empty input
        continue

    else:
        speak("Sorry, I can't do that yet.")

# Run the assistant
