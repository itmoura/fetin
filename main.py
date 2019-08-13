from manipulation import Manipulation

class main:
    controller = Manipulation("db", "idToken")

    # TODOS AS 'TABELAS'
    bc = "contact"
    bcom = "command"
    ba = "aprendizado"

    # salvando no bd
    dados = {"read": "Floquinho, Quantos anos voce tem?", "write": "Eu tenho 2 anos"}
    controller.register(ba, dados)

    list = controller.list(bc)
    for id in list:
        result = controller.listInfo(bc, id)
        username = result.get(u'username')
        read = result.get(u'read')
        print read, username