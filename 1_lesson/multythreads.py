import time
import threading


def sleepTime(wait, name):
    print("Выводит текст: {}".format(name))
    time.sleep(wait)
    print("Выводим тест повторно: ".format(name))


td = threading.Thread(target=sleepTime, name="SleepTime", args=(3, "Call sleep time function"))
td.start()


print("Hello for all")