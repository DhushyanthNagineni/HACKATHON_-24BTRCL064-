import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio)
    print(f"Recognized: {command}")
except sr.UnknownValueError:
    print("Sorry, I couldn't understand.")
except sr.RequestError:
    print("Could not request results, check your internet connection.")