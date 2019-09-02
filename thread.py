import threading
import time
from manipulation import Manipulation
from test import Test
from open import Open

exitFlag = 0
controller = Manipulation("db")
test = Test()
bcom = "command"
bcar = "car"
cad = 0

class myThread (threading.Thread):
    def __init__(self, threadID, banco, counter, cad):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.banco = banco
        self.counter = counter
    def run(self):
        print ("Starting " + self.banco)
        print_time(self.banco, self.counter, 1, cad)
        print ("Exiting " + self.name)

def print_time(threadName, delay, counter, cad):
    while counter:
        if(threadName == "cadastra"):
            time.sleep(delay)
            dados = {"execute": "assistir algo "+str(cad)}
            controller.register(bcom, dados)
            time.sleep(5)
            dados = {"execute": cad}
            controller.register(bcar, dados)
            cad += 1
        else:
            time.sleep(delay)
            list = controller.list(threadName)
            if(counter == 1):
                fim = 0
            if(list != 0):
                aux = len(list)
            else:
                aux = 0
            # print list
            if(fim < aux):
                i = 1
                for key in sorted(list.keys(), reverse=True):
                    if(counter != 1):
                        if(i == 1):
                            result = list[key]
                            execute = result.get(u'execute')
                            if(threadName == "car"):
                                test.motor(execute)
                            elif(threadName == "command"):
                                print (execute)
                                quebrar = execute.split(" ")
                                tam = len(quebrar)
                                print (tam)
                                if quebrar[0] == "assistir":
                                    # op = Open()
                                    x = 1
                                    palavra = ""
                                    while x < tam:
                                        palavra = palavra + quebrar[x] + " "
                                        x += 1
                                    print(palavra)
                                    # op.youtube(palavra)
                    fim = aux
                    i += 1
            counter += 1

# Create new threads
thread1 = myThread(1, "car", 1, 1)
thread2 = myThread(2, "command", 1.5, 1)
thread3 = myThread(3, "cadastra", 2, cad)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print ("Exiting Main Thread")