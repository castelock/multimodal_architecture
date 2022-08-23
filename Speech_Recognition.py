import speech_recognition as sr

class SpeechRecognition:

    def __init__(self):
        self.rec = sr.Recognizer()
        #self.mic = sr.Microphone(device_index = 7)
        self.mic = sr.Microphone()

    def list_mics(self):
        print("The list of microphones are:")
        print(sr.Microphone.list_microphone_names())

    def speechRecognition(self):
        with self.mic as source:
            self.rec.adjust_for_ambient_noise(source)
            audio = self.rec.listen(source)
        
        try:
            text = self.rec.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            print("API unavailable")
        except sr.UnknownValueError:
            # speech was unintelligible
            print("Unable to recognize speech")
                
        
        print(text)