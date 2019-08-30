from connection import Connection
import json
from collections import OrderedDict

class Manipulation:
    def __init__(self, db, idToken):
        # Conecta com Banco
        con = Connection
        self.db = con.db
        self.idToken = con.idToken

    # Registra dados
    def register(self, banco, dados):
        idToken = self.idToken
        db = self.db
        db.child(banco).push(dados, idToken)

    # Ler dados
    def list(self, banco):
        idToken = self.idToken
        db = self.db
        list = db.child(banco).get(idToken).val()
        # listOrder = json.dumps(list, sort_keys=True)
        return list

    def listInfo(self, banco, id):
        idToken = self.idToken
        db = self.db
        list = db.child(banco).child(id).get(idToken).val()
        return list