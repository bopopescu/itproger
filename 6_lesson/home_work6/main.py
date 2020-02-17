import pyttsx3
import speech_recognition as sr
from PIL import Image
from pytesseract import image_to_string as converter

pc_voice = pyttsx3.init()


def start_program():
    pc_voice.say("Hello, User! Choose operation!")
    pc_voice.runAndWait()


def write_file():
    try:
        text = converter(Image.open('imes/img1.jpg'))
    except Exception as e:
        print("Error image to text recognition: ", e)
        finish()
        return False

    file = open("image_text.txt", "w")
    file.write(text)
    file.close()

    return True


def read_file():
    try:
        file = open("image_text.txt", 'r')
        print(file.read())
    except Exception as e:
        print(e)
        finish()
        return False
    finally:
        file.close()

    return True


def finish():
    pc_voice.say("Bye Bye.Program finished.")
    pc_voice.runAndWait()
    return False


def main():
    run_program = True

    while run_program:
        start_program()
        try:
            record = sr.Recognizer()

            with sr.Microphone() as source:
                print("Говори...")
                record.adjust_for_ambient_noise(source, duration=1)
                audio = record.listen(source)
                print("Recognition audio file : ", audio)

            result = record.recognize_google(audio)  # language="en-En" language='ru-Ru'
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
                run_program = finish()
        except sr.UnknownValueError:
            print("voice can't recognize, repeat again")
            run_program = finish()
        except sr.RequestError as e:
            print('Connection error: {}', format(e))
            run_program = finish()
        except Exception as some_error:
            print(some_error)
            run_program = finish()

if __name__ == "__main__":
    main()
