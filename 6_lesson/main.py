import pyttsx3
import datetime
import webbrowser

tts = pyttsx3.init()

voices = tts.getProperty('voices')

tts.setProperty('voice', 'ru')
tts.say('Hello every one')
tts.runAndWait()

# speakrecognition
# pyaudio
import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

record = sr.Recognizer()


def sayToMe(talk):
    tts.say(talk)
    tts.runAndWait()

sayToMe("say something...")
try:
    with sr.Microphone() as source:
        print("say something...")
        record.adjust_for_ambient_noise(source, duration=1)
        audio = record.listen(source)

    print(audio)
    result = record.recognize_google(audio, language='ru-Ru')  # language="en-En" language='ru-Ru'
    result = result.lower()
    print(result)

    if result == "скажи время":
        now = datetime.datetime.now()
        str_date = "Время сейчас -  {}: {}".format(str(now.hour), str(now.minute))
        print(str_date)
        sayToMe(str_date)
    elif result == "открой веб-сайт":
        webbrowser.open("http://itporger.com")


except sr.UnknownValueError as e:
    print("голос блы не распзнан")
except sr.RequestError as e:
    print("Чтото пошло не так, {}".format(e))

# import speech_recognition as sr
#
# r = sr.Recognizer()
#
# with sr.Microphone() as source:
#     print("Скажите что-нибудь")
#     audio = r.listen(source)
#     try:
#         print(r.recognize_google(audio, language="ru-RU"))
#     except sr.UnknownValueError:
#         print("Робот не расслышал фразу")
#     except sr.RequestError as e:
#         print("Ошибка сервиса; {0}".format(e))
