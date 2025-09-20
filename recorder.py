import speech_recognition as sr

# --- Option 1: Normal Recording with Longer Pause ---
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 2  # wait 2 seconds before stopping
        r.energy_threshold = 300  # ignore background noise
        print("🎤 Speak now (stop speaking for 2s to finish)...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("✅ Recognized:", text)
        return text
    except Exception as e:
        return f"Error: {str(e)}"

# --- Option 2: Continuous Listening until stopped ---
def continuous_listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1.5
        r.energy_threshold = 300
        print("🎤 Continuous listening... press Ctrl+C to stop.")
        while True:
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio)
                print("You said:", text)
            except Exception as e:
                print("❌ Error:", str(e))

# --- Test (only runs if you run this file directly) ---
if __name__ == "__main__":
    mode = input("Choose mode: [1] Normal Recording [2] Continuous Listening: ")
    if mode == "1":
        print(recognize_speech())
    else:
        continuous_listen()
