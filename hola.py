import speech_recognition as sr
import keyboard
import unicodedata
import time

def normalizar_texto(texto):
    return unicodedata.normalize("NFKD", texto.lower())

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Habla ahora...")

        try:
            audio = recognizer.listen(source, timeout=3)  # Reducción del tiempo de espera
            print("Audio capturado. Reconociendo...")

            texto_reconocido_es = recognizer.recognize_google(audio, language="es-ES")
            texto_reconocido_en = recognizer.recognize_google(audio, language="en-US")
            print("Texto en español:", texto_reconocido_es)
            print("Texto en inglés:", texto_reconocido_en)

            palabras_es = normalizar_texto(texto_reconocido_es).split()
            palabras_en = normalizar_texto(texto_reconocido_en).split()

            if any(palabra in palabras_es for palabra in ["flash"]) or any(palabra in palabras_en for palabra in ["flash"]):
                time.sleep(10)
                keyboard.press_and_release("w")
                print("Pulsando la tecla w")

            if any(palabra in palabras_es for palabra in ["curar"]) or any(palabra in palabras_en for palabra in ["cure"]):
                time.sleep(40)
                keyboard.press_and_release("a")
                print("Pulsando la tecla a")
            if any(palabra in palabras_es for palabra in ["definitivo"]) or any(palabra in palabras_en for palabra in ["definitivo"]):
                time.sleep(30)
                keyboard.press_and_release("d")
                print("Pulsando la tecla d")
             
            
        except sr.WaitTimeoutError:
            print("Tiempo de espera agotado. Intenta nuevamente.")
        except sr.UnknownValueError:
            print("No se pudo reconocer el audio. Intenta nuevamente.")
        except sr.RequestError as e:
            print("Error al solicitar el reconocimiento; {0}".format(e))
