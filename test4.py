import datetime
import time
import threading
import playsound  # Ensure playsound is installed

alarms = []

def set_alarm():
    """Sets an alarm using voice command."""
    print("At what time should I set the alarm? (Use HH:MM AM/PM format)")
    alarm_time = input("Enter time: ").strip()

    formatted_time = convert_to_24_hour(alarm_time)
    if formatted_time:
        alarms.append(formatted_time)
        print(f"✅ Alarm set for {alarm_time} ({formatted_time}).")
        start_alarm_thread(formatted_time)
    else:
        print("❌ Invalid time format. Please use HH:MM AM/PM.")

def stop_alarm():
    """Stops an ongoing alarm."""
    print("Do you want to stop the alarm?")
    response = input("Enter response: ").strip().lower()
    if "yes" in response:
        print("🔕 Alarm stopped.")

def convert_to_24_hour(time_str):
    """Converts spoken time (12-hour) to 24-hour format for comparison."""
    try:
        time_obj = datetime.datetime.strptime(time_str, "%I:%M %p")
        return time_obj.strftime("%H:%M")  # Convert to 24-hour format
    except ValueError:
        return None

def start_alarm_thread(alarm_time):
    """Starts a background thread to check the alarm time."""
    def alarm_checker():
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time == alarm_time:
                print("Alarm ringing! ")
                playsound.playsound("alarm.mp3")  # Ensure this file exists
                break
            time.sleep(10)  # Check every 10 seconds

    threading.Thread(target=alarm_checker, daemon=True).start()

# Run the assistant
command = input("Enter command: ").strip().lower()

if "set alarm" in command:
    set_alarm()
elif "stop alarm" in command:
    stop_alarm()