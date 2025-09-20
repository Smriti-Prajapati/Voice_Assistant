# Amigo Voice Assistant 🎙️🤖

Amigo is a **Python-based personal voice assistant** that can listen, recognize, and respond to your commands in real-time. It leverages **Vosk Speech Recognition**, **pyttsx3 for text-to-speech**, and various APIs to provide a wide range of features like Wikipedia search, Google search, weather updates, jokes, time/date announcements, and more.

---

## 🚀 Features

* **Speech Recognition**: Uses [Vosk](https://alphacephei.com/vosk/) for offline speech-to-text.
* **Text-to-Speech**: Converts responses into natural speech using `pyttsx3`.
* **Wikipedia Search**: Fetches quick summaries from Wikipedia.
* **Google Search**: Performs web searches and reads out top results.
* **Open Websites**: Quickly open YouTube, Google, or GitHub via voice commands.
* **Weather Updates**: Get live weather information for Indian cities using **OpenWeatherMap API**.
* **News Headlines**: Reads random latest news headlines (can be extended with News API).
* **Jokes**: Lightens the mood with random jokes.
* **Time & Date**: Tells the current time and date.
* **Exit Command**: Gracefully shuts down the assistant.

---

## 🛠️ Technologies Used

* **Python 3.x**
* [Vosk](https://pypi.org/project/vosk/) – Offline speech recognition
* [Sounddevice](https://pypi.org/project/sounddevice/) – Audio input stream
* [pyttsx3](https://pypi.org/project/pyttsx3/) – Text-to-speech engine
* [Wikipedia API](https://pypi.org/project/wikipedia/) – Fetches summaries
* [Requests](https://docs.python-requests.org/en/master/) – API calls
* [Google Search](https://pypi.org/project/googlesearch-python/) – Web search integration
* **OpenWeatherMap API** – Weather updates
* **Python Standard Libraries**: `os`, `json`, `datetime`, `queue`, `random`, `webbrowser`

---

## 📂 Project Structure

```
Amigo-Voice-Assistant/
│── assistant.py         # Main Python script
│── requirements.txt     # List of dependencies
│── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Smriti-Prajaapati/Voice_Assistant.git
cd amigo-voice-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Vosk Model

* Download the [Vosk English Model](https://alphacephei.com/vosk/models).
* Extract it and update the `model_path` in the script:

```python
model_path = r"C:\path\to\vosk-model-small-en-us-0.15"
```

### 4. Add API Keys

Replace placeholders with your own keys:

```python
WEATHER_API_KEY = "your_openweathermap_api_key"
NEWS_API_KEY = "your_newsapi_key"  # Optional if you extend news feature
```

---

## ▶️ Usage

Run the assistant:

```bash
python assistant.py
```

Amigo will greet you:

```
Amigo assistant activated. How can I assist you?
```

Now, speak any supported command like:

* "Wikipedia Albert Einstein"
* "Open YouTube"
* "Search for Python programming"
* "What's the weather?"
* "Tell me a joke"
* "What's the time?"
* "What's today's date?"
* "Exit"

---

## 📋 Example Commands

| Command                | Action                          |
| ---------------------- | ------------------------------- |
| "Wikipedia Python"     | Reads a Wikipedia summary       |
| "Open Google"          | Opens google.com in browser     |
| "Search for AI trends" | Reads Google search results     |
| "Weather"              | Asks for city and gives weather |
| "News"                 | Reads a random news headline    |
| "Tell me a joke"       | Speaks a random joke            |
| "Time"                 | Tells the current time          |
| "Date"                 | Tells today’s date              |
| "Exit"                 | Exits the assistant             |

---

## 🔮 Future Enhancements

* Integration with **real-time News API** for live headlines.
* Adding **music playback** via Spotify or YouTube API.
* Implementing **reminders and alarms**.
* Extending **multi-language support**.
* Adding **chatbot capabilities** for casual conversation.

---

## 👩‍💻 Author

Developed by **Smriti Prajapati**
*Personal Voice Assistant Project — "Amigo"*

---
