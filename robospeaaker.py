import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1")
    
    # Initialize the pyttsx3 engine once outside the loop
    engine = pyttsx3.init()
    
    while True:
        x = input("Enter what you want me to speak (or 'q' to quit): ")
        if x.lower() == "q":  # Added .lower() to handle 'Q' as well
            print("Exiting RoboSpeaker. Goodbye!")
            break
        engine.say(x)
        engine.runAndWait()
