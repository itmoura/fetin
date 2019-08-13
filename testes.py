import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyrebase
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# BANCO
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# ref = db.reference('server/saving-data/fireblog')

# config = {
#     "apiKey": "AAAAAgRtufc:APA91bF-pSwNQIYe0kW4eo7UVUtISESRd5yNomtolB9eGAHownDgV-Ksp6NoAdeQ6e5oClRl785jcjv_Mj1o0QEd1fnwe58PkJmTbxZGsnbHajdcevRgy2y_Z34pxSCtYO2LfqQfN_Ui",
#     "authDomain": "fetin-99767.firebaseapp.com",
#     "databaseURL": "https://project-8664234487.firebaseio.com",
#     "storageBucket": "fetin-99767.appspot.com"
# }

cred = credentials.Certificate('C:/Users/itmoura/IdeaProjects/fetin/key/fetin/fetin-99767.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://project-8664234487.firebaseio.com'
})
#
ref = db.reference('fetin-99767')
users_ref = ref.child('users')
users_ref.set({
    '0kdIEeSAwGnkMRIGMkj9a': {
        'name': "Italo",
        'idade': 20
    }
})
print(ref.get())

# Start navegador firefox
# browser = webdriver.Firefox(executable_path = '/Users/itmoura/Documents/geckodriver')

# youtube = "http://www.youtube.com"
# google = "http://google.com"
# local = "file:///C:/Users/itmoura/IdeaProjects/fetin/read.json"
# python = "https://www.python.org/"
#
#
# te = browser.get(local)
# json_content = browser.find_element_by_css_selector('body').text
# print(json_content)

# ESPERA
# time.sleep(10)
# Fechar navegador
# browser.quit()

# query = 1;
#
# if(query == 0):
#     browser.get(google)
#     browser.find_element_by_name("q").send_keys(pesquisa) # GOOGLE (Name = q )
# else:
#     browser.get(youtube)
#     browser.find_element_by_name("search_query").send_keys(pesquisa) # Youtube (Name = search_query )
#
# act = ActionChains(browser)
# act.send_keys(Keys.ENTER).perform()
# act.click(browser.find_element_by_id("dismissable")).perform()
# time.sleep(5)
# act.click(browser.find_element_by_xpath("//a[@class='yt-simple-endpoint style-scope ytd-video-renderer']")).perform()
# act.click(browser.find_element_by_id("img"))

