from Configuracoes import opcoes
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote

def confNav():
    opt = opcoes.configurar()
    navegador = webdriver.Chrome(options=opt, executable_path=r'/home/patrick/Documentos/chromedriver')
    navegador.maximize_window()
    navegador.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    navegador.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    print(navegador.execute_script("return navigator.userAgent;"))
    return navegador

def digitarSite(navegador,site):
    navegador.get(site)

def elemento(navegador,path):
    wait = WebDriverWait(navegador, 10)
    elemento = wait.until(EC.presence_of_element_located((By.XPATH, path)))
    return elemento

def click(elemento):
    elemento.click()

def scroll(navegador,valor):
    query = "window.scrollTo(0, {})".format(valor)
    navegador.execute_script(query)

def submit(elemento):
    elemento.submit()

def digitar(elemento,texto):
    elemento.send_keys(texto)

def find(navegador):
    links = navegador.find_elements_by_class_name('rc') #I went on Google Search and found the container class for the link
    for link in links:
        #url = link.find_element_by_tag_name('a').get_attribute("href") #this code extracts the url of the HTML link
        print(link.find_element_by_tag_name('a').get_attribute("href"))

def google(navegador):
    elementos = navegador.find_elements_by_class_name("uEierd")
    for elemento in elementos:
        print(elemento.find_elements_by_tag_name('span')[2].text)
    return elementos



    
