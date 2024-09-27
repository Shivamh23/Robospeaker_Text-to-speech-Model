import pyttsx3


def speak(text):
    # Initializing the TTS engine
    engine = pyttsx3.init()

    # Setting properties before adding things to say
    #engine.setProperty('rate', 150)  # Speed percent (can go over 100)
   # engine.setProperty('volume', 0.9)  # Volume 0-1

    # Say the given text
    engine.say(text)

    # Blocking while processing all the currently queued commands
    engine.runAndWait()


if __name__ == "__main__":
    print("Welcome to RoboSpeaker!")
    print("Type 'exit' to quit.")

    while True:
        text = input("Enter text to speak: ")

        if text.lower() == "exit":
            print("Exiting RoboSpeaker...")
            break

        speak(text)
