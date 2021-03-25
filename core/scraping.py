from scraper import scrape_data_corotos 
from pyvirtualdisplay import Display
import os

with Display():

    #url = "https://www.corotos.com.do/sc/inmuebles-en-venta/casas"
    url = "https://www.corotos.com.do/sc/inmuebles-en-venta/apartamentos"
    tipo_neg = "Venta"
    #driver = os.getcwd()+"/chromedriver_88.exe"
    driver = os.getcwd()+"/geckodriver.exe"
    solo_agentes = 0
    no_dupli = 1
    resp = os.getcwd()

    #Vamos a llamar esto n veces teniendo en cuenta que siempre se para solo
    for n in range(1):
        feats = scrape_data_corotos(url,tipo_neg,2,driver,loads=1,solo_agentes=solo_agentes,no_dupli=no_dupli)

print(feats)
