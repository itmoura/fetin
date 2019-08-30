# -*- coding: utf-8 -*-

from manipulation import Manipulation
# from open import Open
import _thread
import time
from open import Open

controller = Manipulation("db", "idToken")

class main:
    # TODOS AS 'TABELAS'
    bc = "contact"
    bcom = "command"
    bcar = "car"
    ba = "aprendizado"

    # salvando no bd
    dados = {"execute": "assistir vaui se foder"}
    controller.register(bcom, dados)

    # list = controller.list(bcom)
    # print (list)
    # op = Open()
    # for id in list:
    #     result = controller.listInfo(bcom, id)
    #     print(result)
        # execute = result.get(u'execute')
        # quebrar = execute.split(' ')
        # tam = len(quebrar)
        # if quebrar[0] == "Assistir":
        #     i = 1
        #     palavra = ""
        #     while i < tam:
        #         palavra = palavra + quebrar[i] + " "
        #         i += 1
        #     op.youtube(palavra)

    # op.discordAdd("itmoura#6974")