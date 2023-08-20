import subprocess

librerias = ["speechrecognition", "keyboard", "pyaudio"]

for libreria in librerias:
    subprocess.call(["pip", "install", libreria])
