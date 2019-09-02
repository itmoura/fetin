from connection import Connection
import json
from collections import OrderedDict

class Manipulation:
    def __init__(self, db):
        # Conecta com Banco
        con = Connection
        self.db = con.db

    # Registra dados
    def register(self, banco, dados):
        db = self.db
        db.child(banco).push(dados)

    # Ler dados
    def list(self, banco):
        db = self.db
        list = db.child(banco).get().val()
        if(list != None):
            return list
        else:
            return 0

    def listInfo(self, banco, id):
        db = self.db
        list = db.child(banco).child(id).get().val()
        return list