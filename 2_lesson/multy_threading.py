import time
import threading


def sleepTime(wait, name):
    print("Выводит текст: {}".format(name))
    time.sleep(wait)
    print("Выводим тест повторно: {}".format(name))


start = time.time()

t_list = []

for i in range(5):
    name = "Sleep time: " + str(i + 1)
    print("{} был запущен".format(name))
    td = threading.Thread(target=sleepTime, name="SleepTime", args=(3, name))
    td.start()
    t_list.append(td)

for t in t_list:
    t.join()

for i in range(5):
    sleepTime(3, i)



end = time.time()

print("Время обработки: ", (end - start))
