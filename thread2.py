# -*- coding: utf-8 -*-
# coding: utf-8

import threading
import time
from manipulation import Manipulation
from test import Test
from voice import Voice
from open import Open

exitFlag = 0
controller = Manipulation("db")
test = Test()
voice = Voice()
bcom = "command"
bcar = "car"
bt = "teach"
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
    def kill(self):
        self.killed = True

def print_time(threadName, delay, counter, cad):
    while counter:
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
                        if(threadName == "car"):
                            move = result.get(u'move')
                            outroTest = test.motor(move)
                            print (outroTest)
                        elif(threadName == "command"):
                            execute = result.get(u'execute')
                            quebrar = execute.split(" ")
                            tam = len(quebrar)
                            if(quebrar[0] == "assistir"):
                                if thread2.isAlive():
                                    print ("Matei thread2")
                                    thread2.kill()
                                elif threadaux.isAlive():
                                    print ("Matei AUX")
                                    threadaux.kill()
                                op = Open()
                                x = 1
                                palavra = ""
                                while x < tam:
                                    palavra = palavra + quebrar[x] + " "
                                    x += 1
                                if thread2.isAlive():
                                    print ("Deixei vivo AUX")
                                    threadaux.start()
                                elif threadaux.isAlive():
                                    print ("Deixei vivo 2")
                                    thread2.start()
                                op.youtube(palavra)
                            elif(quebrar[0] == "pesquisar"):
                                op = Open()
                                x = 1
                                palavra = ""
                                while x < tam:
                                    palavra = palavra + quebrar[x] + " "
                                    x += 1
                                op.google(palavra)
                            elif(quebrar[0] == "aprender"):
                                if(tam > 1):
                                    if(quebrar[1] == "portugues"):
                                        if(tam > 3):
                                            pt = controller.list(bt+"/portugues")
                                            for key in sorted(pt.keys()):
                                                letra = pt[key]
                                                qLetra = letra.get(u'letra')
                                                if(qLetra == quebrar[3]):
                                                    descricaoLetra = letra.get(u'descricao')
                                                    print (descricaoLetra)
                                                    voice.fala(descricaoLetra)
                                        else:
                                            voice.fala("Voce nao informou uma letra para aprender")
                                else:
                                    voice.fala("Você não disse o que deseja aprender")
                            elif(quebrar[0] == "ligar"):
                                x = 1
                                palavra = ""
                                while x < tam:
                                    palavra = palavra + quebrar[x] + " "
                                    x += 1
                                print ("estou ligando para ", palavra)
                fim = aux
                i += 1
        counter += 1

# Create new threads
thread1 = myThread(1, "car", 1, 1)
thread2 = myThread(2, "command", 1.5, 1)
threadaux = myThread(3, "command", 1.5, 1)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
threadaux.join()
print ("Exiting Main Thread")