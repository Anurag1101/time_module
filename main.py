import time

def get_greeting():
    current_time = time.strftime('%H:%M:%S')  # Current time in HH:MM:SS format
    current_hour = int(time.strftime('%H'))  # Extracting the hour part
    print(f"Current time: {current_time}")  # Display the current time

    # Determine the greeting based on the hour of the day
    if current_hour < 12:
        return "Good Morning"
    elif current_hour < 16:
        return "Good Afternoon"
    elif current_hour < 20:
        return "Good Evening"
    else:
        return "Good Night"

# Call the function to display the greeting
greeting = get_greeting()
print(greeting)
