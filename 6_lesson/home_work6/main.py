import pyttsx3
import speech_recognition as sr

pc_voice = pyttsx3.init()


def start_program():
    pc_voice.say("Hello, user! Choose operation!")
    pc_voice.runAndWait()


def write_file():
    pass


def read_file():
    pass


def finish():
    finishing = False
    pc_voice.say("Bye Bye!Program finished")
    pc_voice.runAndWait()
    return finishing


def main():
    run_program = True
    while run_program:
        start_program()
        try:
            record = sr.Recognizer()

            with sr.Microphone() as source:
                print("speak...")
                record.adjust_for_ambient_noise(source, duration=1)
                audio = record.listen(source)
                print(audio)

            result = record.recognize_google(audio)  # language="en-En" language='ru-Ru'
            result = result.lower()
            print(result)

            if result == "write file":
                write_file()
            elif result == "read file":
                read_file()
            elif result == "exit":
                run_program = finish(result)
        except sr.UnknownValueError:
            print("voice can't recognize, repeat again")
            run_program = finish()
        except sr.RequestError as e:
            print('Connection error: {}', format(e))
            run_program = finish()


if __name__ == "__main__":
    main()
