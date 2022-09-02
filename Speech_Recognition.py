import speech_recognition as sr
import cv2
import asyncio
from modality_component import ModalityComponent

class SpeechRecognition(ModalityComponent):

    def __init__(self):
        self.rec = sr.Recognizer()
        self.mic = sr.Microphone()
        self.command = "unkown"
        self.responseIM = " "
        self.waitSignal = False

    def list_mics(self):
        print("La lista de micrófonos son:")
        print(sr.Microphone.list_microphone_names())

    def input_mc(self):
        self.rec = sr.Recognizer()
        self.mic = sr.Microphone()        
         

    def output(self):
        return super().output()

    async def speechRecognition(self):

        self.input_mc()

        while True:
            with self.mic as source:
                self.rec.adjust_for_ambient_noise(source)
                audio = self.rec.listen(source)
            
            try:
                self.command = self.rec.recognize_google(audio)
            except sr.RequestError:
                # API inalcanzable o no respondía
                print("API no disponible")
            except sr.UnknownValueError:
                # Speech ininteligible
                print("Unable to recognize speech")
            
            # Enviar evento si el comando es reconocido correctamente
            if(self.command=="nombre" or self.command=="apellidos" or self.command=="edad" or self.command=="enviar" or self.command=="salir"):
                self.send_messageIM()
                response = await self.wait_response()
                print("El mensaje del Interaction Manager es {}",response)

            if cv2.waitKey(1) == ord('q'):                
                break
        
        self.output()
    
    def send_messageIM(self):
        InteractionManager.phase = "speech_recognised"

    async def wait_response(self):
        while(self.waitSignal == False):
            print("Esperando la respuesta del Interaction Manager")
        
        self.waitSignal = False
        return self.responseIM

    def set_response(self, response):
        self.waitSignal = True
        self.responseIM = response

    def getCommand(self):
        return self.command