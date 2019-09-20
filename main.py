# -*- coding: utf-8 -*-

from manipulation import Manipulation
# from open import Open
import time
from open import Open

controller = Manipulation("db")

class main:
    # TODOS AS 'TABELAS'
    bc = "contact"
    bcom = "command"
    bcar = "car"
    ba = "aprendizado"
    bt = "teach"

    # salvando no bd
    # dados = {"letra": "B", "descricao": "Eu vou falar aqui tudo sobre a letra B!"}
    # controller.register('teach/portugues', dados)

    # list = controller.list(bcom)
    # print (list)
    op = Open()

    op.youtube("Luccas Neto")

    # for key in sorted((list.keys()), reverse=True):
    #     result = list[key]
    #     print(result.get(u'execute'))
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