import os
import vosk
import sounddevice as sd
import numpy as np
import json
import pyttsx3
import wikipedia
import webbrowser
from datetime import datetime
import requests
from googlesearch import search
import queue
import random\

# Initialize pyttsx3 engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # 1 for female, 0 for male voice

# API Keys
WEATHER_API_KEY = "e60c15d6aa5bae46a76dfed0ab48332f"
NEWS_API_KEY = "f040fc6d2fa048ed9c760da1a5f6af85"
WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Path to the Vosk model folder C:\Users\smrit\Downloads\vosk-model-en-us-0.22
model_path = r"C:\Users\smrit\Downloads\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15"


# Initialize the Vosk model 
try:
    if os.path.exists(model_path):
        print("Path exists!")
        model = vosk.Model(model_path)
        print("Model loaded successfully!")
    else:
        print("Path does not exist. Please verify the model path.")
        exit(1)
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# Initialize the recognizer
recognizer = vosk.KaldiRecognizer(model, 16000)  # 16 kHz sample rate

# Queue for storing audio data
audio_queue = queue.Queue()

def speak(audio):
    """Speak the given text using pyttsx3."""
    engine.say(audio)
    engine.runAndWait()

def callback(indata, frames, time, status):
    """Callback function for the sounddevice InputStream."""
    if status:
        print(status)
    # Convert NumPy array to byte array
    audio_queue.put(bytes(indata))

def listen_and_recognize():
    """Continuous listening and recognition."""
    with sd.InputStream(callback=callback, channels=1, samplerate=16000, dtype='int16'):
        print("Listening... Please speak now.")
        while True:
            try:
                data = audio_queue.get()
                if recognizer.AcceptWaveform(data):
                    result = recognizer.Result()
                    print(f"Recognized: {result}")
                    handle_command(result)
                else:
                    partial_result = recognizer.PartialResult()
                    print(f"Partial: {partial_result}")
            except KeyboardInterrupt:
                print("Stopping the assistant...")
                break

def handle_command(command):
    """Process the recognized command and perform the appropriate action."""
    command_text = json.loads(command).get("text", "").lower()
    if not command_text:
        return

    if 'wikipedia' in command_text:
        search_wikipedia(command_text)
    elif 'who are you' in command_text or 'introduce yourself' in command_text:
        speak("I am Amigo, your personal voice assistant, developed by Smriti Prajapati.")
    elif 'open youtube' in command_text:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")
    elif 'open google' in command_text:
        speak("Opening Google.")
        webbrowser.open("https://google.com")
    elif 'open github' in command_text:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com")
    elif 'search for' in command_text:
        query = command_text.replace("search for", "")
        google_search(query)
    elif 'weather' in command_text:
        speak("Which city's weather would you like to know?")
        city = get_speech_input()
        if city:
            get_weather(city)
    elif 'news' in command_text:
        get_news()
    elif 'joke' in command_text:
        tell_joke()
    elif 'time' in command_text:
        tell_time()
    elif 'date' in command_text:
        tell_date()
    elif 'exit' in command_text:
        speak("Goodbye!")
        exit()

def google_search(query):
    """Perform a Google search for the given query and speak the results."""
    try:
        speak(f"Searching Google for {query}")
        results = search(query, num_results=3)
        for result in results:
            speak(f"Here is a result: {result}")
    except Exception as e:
        print(f"Google Search Error: {e}")
        speak("Sorry, I couldn't complete the search.")

def search_wikipedia(query):
    """Search Wikipedia for the given query and speak the summary."""
    try:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=5)
        speak(f"According to Wikipedia: {result}")
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"Multiple results found. Here are some options: {e.options[:5]}")
    except Exception as e:
        print(f"Wikipedia Error: {e}")
        speak("Sorry, I couldn't fetch the details. Please try again later.")

def get_weather(city):
    """Fetch and speak the weather details for a given city in India."""
    try:
        # Add the country code for India (in) to the URL
        complete_url = WEATHER_BASE_URL + "q=" + city + ",in" + "&appid=" + WEATHER_API_KEY
        response = requests.get(complete_url)
        data = response.json()

        print(data)  

        if data["cod"] == 200:  # Check if the response code is 200
            main_data = data["main"]
            weather_data = data["weather"][0]
            temperature = main_data["temp"] - 273.15  # Convert temperature to Celsius
            weather_desc = weather_data["description"]
            speak(f"The temperature in {city} is {temperature:.2f}°C with {weather_desc}.")
        else:
            speak("City not found. Please try again.")
    except Exception as e:
        print(f"Weather API Error: {e}")
        speak("Sorry, I couldn't fetch the weather details. Please try again later.")

def get_news():
    """Fetch and speak a random news headline from a predefined list."""
    try:
        speak("Fetching the latest news headlines.")
        
        # List of dummy news headlines
        news_headlines = [
            "Breaking: New technology breakthrough promises faster internet speeds.",
            "Local elections results are in, with unexpected outcomes in several regions.",
            "Experts predict significant changes in the global economy in the coming months.",
            "Government announces new healthcare reforms aimed at improving accessibility.",
            "Scientists discover a new species of fish in the deep ocean."
        ]
        
        # Pick a random news headline
        news = random.choice(news_headlines)
        
        # Speak the selected headline
        speak(f"Here's a news headline: {news}")
        
    except Exception as e:
        print(f"News Error: {e}")
        speak("Sorry, I couldn't fetch the news. Please try again later.")

def tell_joke():
    """Tell a random joke."""
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don’t programmers like nature? It has too many bugs.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the computer go to the doctor? Because it had a virus!"
    ]
    speak(random.choice(jokes))

def tell_time():
    """Speak the current time."""
    time = datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {time}")

def tell_date():
    """Speak the current date."""
    date = datetime.now().strftime("%A, %d %B %Y")
    speak(f"Today's date is {date}")

def get_speech_input():
    """Capture and return speech input as text."""
    try:
        speak("I'm listening. Please speak now.")
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                command_text = json.loads(result).get("text", "").strip()
                return command_text
    except Exception as e:
        print(f"Speech Input Error: {e}")
        speak("Sorry, I couldn't understand. Please try again.")
        return ""

if __name__ == "__main__":
    speak("Amigo assistant activated. How can I assist you?")
    listen_and_recognize()
