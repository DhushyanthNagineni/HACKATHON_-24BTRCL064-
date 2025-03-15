from  functions import *

greetings =['good morning', 'good evening', 'hi', 'hello']
speak("How can I assist you?")


while True:
  
        command = listen()


        if command:
            # Check for date, day, or time requests
            if "date" in command:
                get_date()
            elif "day" in command:
                get_day()
            elif "time" in command:
                get_time()
            
            # Greetings Handling
            elif any(i in command for i in greetings):
                hour = time.localtime().tm_hour
                if hour < 12:
                    speak("Good morning, how can I assist you today?")
                elif hour < 18:
                    speak("Good afternoon, how can I assist you today?")
                else:
                    speak("Good evening, how can I assist you today?")

            # Search Google or Wikipedia
            elif "search google for" in command:
                search_google(command.replace("search google for", "").strip())
            elif "search wikipedia for" in command:
                search_wikipedia(command.replace("search wikipedia for", "").strip())

            # Notes Handling
            elif "take a note" in command:
                take_note()
            elif "read my notes" in command:
                read_notes()

            # Device Control
            elif "turn on" in command or "turn off" in command:
                control_device(command)

            # Alarm Functions
            elif "set alarm" in command:
                set_alarm()
            elif "stop alarm" in command:
                stop_alarm()

            # Exit Command
            elif "exit" in command:
                speak("Goodbye!")
                break
