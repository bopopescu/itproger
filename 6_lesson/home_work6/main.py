import pyttsx3
import speech_recognition as sr
from PIL import Image
from pytesseract import image_to_string as converter

pc_voice = pyttsx3.init()


def start_program():
    pc_voice.say("Hello, User! Say operation!")
    pc_voice.runAndWait()


def write_file():
    try:
        text = converter(Image.open('images/img1.jpg'))
    except Exception as e:
        print("Error image to text recognition: ", e)
        return False

    try:
        file = open("image_text.txt", "w")
        file.write(text)
        file.close()
    except Exception as e:
        print(e)
        return False

    return True


def read_file():
    try:
        file = open("image_text.txt", 'r')
        print(file.read())
        file.close()
    except Exception as e:
        print("Error read from file: ", e)
        finish()
        return False

    return True


def finish():
    pc_voice.say("Bye Bye.")
    pc_voice.runAndWait()


def main():
    run_program = True
    start_program()

    while run_program:
        try:
            record = sr.Recognizer()

            with sr.Microphone() as source:  # device_index=0, device_index=2
                print("Говори...")
                record.adjust_for_ambient_noise(source, duration=2)
                audio = record.listen(source)
                print("Recognition audio file : ", audio)

            result = record.recognize_google(audio, language='en-En')  # language='ru-Ru'
            # result = "Write File"
            # result = "Read File"
            # result = "Exit"

            result = result.lower()

            if result == "write file":
                print(result)
                if not write_file():
                    run_program = False
            elif result == "read file":
                print(result)
                if not read_file():
                    run_program = False
            elif result == "exit":
                print(result)
                run_program = False

        except sr.UnknownValueError:
            print("voice can't recognize, repeat again")
        except sr.RequestError as e:
            print('Connection error: ', e)
            run_program = False
        except Exception as some_error:
            print(some_error)
            run_program = False

    finish()


if __name__ == "__main__":
    main()
