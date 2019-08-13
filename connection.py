# coding: utf-8

import pyrebase

class Connection:
    # config conexão
    config = {
        "apiKey": "AIzaSyDWSstoBOOyIakddI8KGNNzeItRh7wWDGo",
        "authDomain": "flucy-3397e.firebaseapp.com",
        "databaseURL": "https://flucy-3397e.firebaseio.com",
        "projectId": "flucy-3397e",
        "storageBucket": "flucy-3397e.appspot.com",
        "messagingSenderId": "97125697837",
        "appId": "1:97125697837:web:b9658f7bd7f5e63d"
    }
    firebase = pyrebase.initialize_app(config)

    # autentificação
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password("flucyfetin38@gmail.com", "fetin*38")

    # idToken
    idToken = user['idToken']

    db = firebase.database()

# PODE SER UTEIS
# "apiKey": "5adc3efc2397d89c392bc48f8100194d686b30d4",
# "authDomain": "flucy-fetin.firebaseapp.com",
# "databaseURL": "https://flucy-3397e.firebaseio.com",
# "storageBucket": "flucy-fetin.appspot.com",
# "serviceAccount": "./key/fetin.json"