from  functions import *


while True:
    speak("How can I assist you?, Dhushyanth")
    command = listen()

    if command:
        if "date" in command:
            get_date()
        elif "day" in command:
            get_day()
        elif "time" in command:
            get_time()
        elif "search google for" in command:
            search_google(command.replace("search google for", "").strip())
        elif "search wikipedia for" in command:
            search_wikipedia(command.replace("search wikipedia for", "").strip())
       
        elif "take a note" in command:
            take_note()
        elif "read my notes" in command:
            read_notes()
        elif "turn on" in command or "turn off" in command:
            control_device(command)
        elif "set alarm" in command:
            set_alarm()
        elif "stop alarm" in command:
            stop_alarm()
        elif "exit"   in command:
            speak("Goodbye!")
            break
       