import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import time
import threading
import requests
from playsound import playsound

engine = pyttsx3.init()

def speak(text):
    # Convert text to speech.
    engine.say(text)
    engine.runAndWait()

def listen():
    # Capture voice input.
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand.")
        return None
    except sr.RequestError:
        speak("Check your internet connection.")
        return None

# Commands 

def get_date():
    # Speak the current date.
    today = datetime.datetime.today().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")
    print(f"📅 Date: {today}")

def get_day():
    # Speak the current day.
    day = datetime.datetime.today().strftime("%A")
    speak(f"Today is {day}")
    print(f"📅 Day: {day}")

def get_time():
    # Speak the current time.
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")
    print(f"🕒 Time: {now}")

def search_google(query):
    # Perform a Google search.
    speak(f"Searching Google for {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def search_wikipedia(query):
    # Fetch summary from Wikipedia.
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)
        print(f"Wikipedia: {summary}")
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results, please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find anything on Wikipedia.")

# To-Do List & Notes 

notes = []

def take_note():
    # Save a note from voice input
    speak("What should I note down?")
    note = listen()
    if note:
        notes.append(note)
        speak("Note saved.")
        print(f"Note saved: {note}")

def read_notes():
    # Read out saved notes.
    if notes:
        speak("Here are your notes:")
        for note in notes:
            speak(note)
            print(f" {note}")
    else:
        speak("You have no notes.")

# Smart Home Controls (Simulated) 

def control_device(command):
    # Simulate smart home control.
    if "light" in command:
        if "on" in command:
            speak("Turning the lights on.")
            print(" Lights turned ON.")
        elif "off" in command:
            speak("Turning the lights off.")
            print(" Lights turned OFF.")
    elif "fan" in command:
        if "on" in command:
            speak("Turning the fan on.")
            print(" Fan turned ON.")
        elif "off" in command:
            speak("Turning the fan off.")
            print("Fan turned OFF.")
    else:
        speak("I didn't understand the command.")

#   alarm system (From Previous Implementation) 

alarms = []

def play_alarm_sound():
    #play alarm ringtone.
    playsound("alarm.mp3")  

def check_alarms():
    #continuously check if an alarm time is reached
    while True:
        now = datetime.datetime.now().strftime("%I:%M %p")
        for alarm in alarms:
            if now in alarm:
                speak("Wake up! Your alarm is ringing.")
                print(f"Alarm ringing at {now}!")
                play_alarm_sound()
                alarms.remove(now)
            time.sleep(10)

alarm_thread = threading.Thread(target=check_alarms, daemon=True)
alarm_thread.start()

def set_alarm():
    # sets an alarm using voice command.
    speak("At what time should I set the alarm? (Use HH:MM AM/PM format)")
    alarm_times = listen()
    alarm_time = str(alarm_times)
    if "a.m" or "p.m" in alarm_time:
        alarm_time = alarm_time.replace("a.m.", "AM").replace("p.m.", "PM")
    formatted_time = convert_to_24_hour(alarm_time)
    if formatted_time:
        alarms.append(formatted_time)
        speak(f" Alarm set for {alarm_time} ({formatted_time}).")
        start_alarm_thread(formatted_time)
    else:
        speak("Invalid time format. Please use HH:MM AM/PM.")

def stop_alarm():
    """Stops an ongoing alarm."""
    speak("Do you want to stop the alarm?")
    response = input("Enter response: ").strip().lower()
    if "yes" in response:
        speak(" Alarm stopped.")

def convert_to_24_hour(time_str):
    # Converts spoken time (12-hour) to 24-hour format for comparison.
    try:
        time_obj = datetime.datetime.strptime(time_str, "%I:%M %p")
        return time_obj.strftime("%H:%M")  # Convert to 24-hour format
    except ValueError:
        return None

def start_alarm_thread(alarm_time):
    # Starts a background thread to check the alarm time.
    def alarm_checker():
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time == alarm_time:
                speak("Alarm ringing! ")
                playsound("alarm.mp3")  # Ensure this file exists
                break
            time.sleep(10)  # Check every 10 seconds

    threading.Thread(target=alarm_checker, daemon=True).start()

# Run the assistant
