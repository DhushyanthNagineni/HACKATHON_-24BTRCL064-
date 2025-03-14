import spacy

nlp = spacy.load("en_core_web_sm")
command = "Turn on the lights"
doc = nlp(command)

if "light" in command and "on" in command:
    action = "Turning on the lights"
elif "temperature" in command:
    action = "Adjusting temperature"
else:
    action = "Command not recognized"

print(action)

def execute_command(command):
    if "light" in command and "on" in command:
        print("Turning on the lights...")
        # Call smart home API
    elif "temperature" in command:
        print("Adjusting temperature...")
    else:
        print("Command not recognized.")

execute_command("Turn on the lights")