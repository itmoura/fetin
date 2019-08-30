# coding: utf-8

import time
from random import randrange
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Start navegador firefox
# /Users/itmoura/Desktop/chrome-win/chrome
# myprofile = webdriver.FirefoxProfile(r'C:/Users/itmoura/AppData/Roaming/Mozilla/Firefox/Profiles/ucsv42th.default-release')
# options = webdriver.ChromeOptions()
# options.add_argument("--kiosk") chrome_options=options

# browser.manage().window().maximize()

delay1 = 5
delay2 = 7

class Open:

    def youtube(self, search):
        browser = webdriver.Chrome( executable_path = '/Users/itmoura/Documents/chromedriver')
        act = ActionChains(browser)
        youtube = "https://www.youtube.com"
        browser.get(youtube)
        time.sleep(delay2)
        browser.find_element_by_id("search-button").click()
        time.sleep(delay1)
        browser.find_element_by_name("search_query").send_keys(search) # Youtube (Name = search_query )
        wait = WebDriverWait(browser, 3)
        visible = EC.visibility_of_element_located

        # Da enter para pesquisar
        act.send_keys(Keys.ENTER).perform()
        time.sleep(delay2)

        # Espera um tempinho
        # wait.until(visible((By.ID, "text")))

        # Varre todos os videos
        linkVideo = [i.get_attribute('href') for i in browser.find_elements_by_css_selector('a[id*=thumbnail]')]

        # Pega a quantidade de videos varridos
        qntVideo = len(linkVideo)

        # gera um numero aleatorio
        num = randrange(qntVideo)

        # abre um video de acordo com o num aleatorio
        browser.get(linkVideo[num])

        # Espera até q o "video-title" apareça
        time.sleep(delay2)
        browser.find_element_by_id("video-title").click()

        # Coloca em modo "teatro"
        act.send_keys(Keys.CONTROL + "t").perform()

    def google(self, search):
        browser = webdriver.Chrome( executable_path = '/Users/itmoura/Documents/chromedriver')
        act = ActionChains(browser)
        google = "https://www.google.com/imghp"
        browser.get(google)
        browser.find_element_by_name("q").send_keys(search) # GOOGLE (Name = q )

        # Da enter para pesquisar
        act.send_keys(Keys.ENTER).perform()

    def discordAdd(self, add):
        browser = webdriver.Chrome( executable_path = '/Users/itmoura/Documents/chromedriver')
        discord = "https://discordapp.com/channels/@me"
        browser.get(discord)
        act = ActionChains(browser)
        bct = ActionChains(browser)
        time.sleep(delay2)
        act.move_by_offset(930,20).click().perform()
        time.sleep(delay2)
        browser.find_element_by_class_name("addFriendInput-4bcerK").send_keys(add)
        time.sleep(delay2)
        # Da enter para pesquisar
        bct.send_keys(Keys.ENTER).perform()
        time.sleep(delay2)
        browser.quit()

    def ligar(self):
        browser = webdriver.Chrome( executable_path = '/Users/itmoura/Documents/chromedriver')
        act = ActionChains(browser)
        discord = "https://discordapp.com/channels/@me"
        browser.get(discord)

        time.sleep(delay2)

        linkChat = [i.get_attribute('href') for i in browser.find_elements_by_css_selector('a')]

        print linkChat
        for i in linkChat:
            quebra = i.split('/')
            if(len(quebra) > 2):
                if(quebra[3] == "channels") and (quebra[4] == "@me") and (len(quebra) > 4):
                    novaQuebra = i.split("@me")
                    if(len(novaQuebra) > 1):
                        print novaQuebra[1]
        # act.move_by_offset(831,124).click().perform()

        # Da enter para pesquisar
        # act.send_keys(Keys.ENTER).perform()

    # MOVE O MOUSE
    # act.move_by_offset(x, y).click().perform()
