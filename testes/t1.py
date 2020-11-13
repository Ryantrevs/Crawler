from Configuracoes import navegador
import time
from Configuracoes.changeMac import mac

sites = []

def main():
    f = open('./data/example1.txt', 'r', encoding='utf8')
    lista = f.readlines()
    mac.iniciar()
    nav = navegador.confNav()
    navegador.digitarSite(nav,'https://www.myip.com/')
    time.sleep(5)
    #navegador.digitarSite(nav,'https://google.com')
    #element = navegador.elemento(nav, lista[1])
    #navegador.click(element)
    #navegador.scroll(nav, lista[2])
    navegador.digitarSite(nav,'https://google.com')
    elemento2 = navegador.elemento(nav, lista[0])
    #time.sleep(10)
    navegador.digitar(elemento2, lista[1])
    #navegador.submit(elemento2)
    #elemento1 = navegador.elemento(nav,'//*[@id="tads"]/div[2]/div/div/div[1]/a/')
    #navegador.click(elemento1)

    navegador.google(nav)
    time.sleep(100)
    

    #print(elemento3)
    #navegador.click(elemento3)
