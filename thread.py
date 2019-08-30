import threading
import time
from manipulation import Manipulation
from test import Test
from open import Open
import json

exitFlag = 0
controller = Manipulation("db", "idToken")
test = Test()
bcom = "command"

class myThread (threading.Thread):
    def __init__(self, threadID, banco, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.banco = banco
        self.counter = counter
    def run(self):
        print ("Starting " + self.banco)
        print_time(self.banco, self.counter, 1)
        print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        list = controller.list(threadName)
        if(counter == 1):
            fim = 0
        if(list != 0):
            aux = len(list)
        # print list
        if(fim < aux):
            i = 1
            for id in list:
                result = controller.listInfo(threadName, id)
                execute = result.get("execute")
                if(counter != 1):
                    if i == aux:
                        if(threadName == "car"):
                            test.motor(execute)
                        elif(threadName == "command"):
                            quebrar = execute.split(' ')
                            tam = len(quebrar)
                            if quebrar[0] == "assistir":
                                # op = Open()
                                i = 1
                                palavra = ""
                                while i < tam:
                                    palavra = palavra + quebrar[i] + " "
                                    i += 1
                                print(palavra)
                                # op.youtube(palavra)
                fim = aux
                i += 1
        counter += 1

# Create new threads
thread1 = myThread(1, "car", 1)
thread2 = myThread(2, "command", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")