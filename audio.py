import speech_recognition as sr
import os
import sys
import webbrowser


# def talk(word):
#     print(word)
#     os.system("say " + word)
#
#
# talk('Привет')

def command():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Говорите: ")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(src, duration=1)
        audio = r.listen(src)
    try:
        comm = r.recognize_google(audio, language="ru-RU")
        print("Вы сказали: "+comm)
    except sr.UnknownValueError:
        print("Не понял!!!")
        comm = command()
    return comm


chto = command()
url1 = 'https://www.youtube.com/watch?v=L83ye4x71lw'
url2 = 'https://www.youtube.com/watch?v=VNcHYr5zL3g'
if 'Невзоров' in chto:
    url = url1
elif 'Базилио' in chto:
    url = url2
else:
    print(chto + " послышалось")
webbrowser.open(url)

