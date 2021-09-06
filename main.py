from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import json

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
navegador = webdriver.Chrome()


#url = "https://www.terabyteshop.com.br/produto/19167/placa-de-video-colorful-geforce-rtx-3060-nb-duo-12gb-l-v-gddr6x-256bit-lhr212327118801"
url = "https://www.terabyteshop.com.br/produto/18165/placa-de-video-biostar-geforce-gt-610-2gb-ddr3-64bit-vn6103thx6"
navegador.get(url)

time.sleep(1)


element = navegador.find_element_by_xpath("//div[@class='info-det-prod']")
titulo = navegador.find_element_by_xpath("//h1[@class='tit-prod']")
html_content = element.get_attribute('outerHTML')
titulo_content = titulo.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
soup_title = BeautifulSoup(titulo_content, 'html.parser')
preco = soup.find("p", class_="val-prod valVista").string
result_title = soup_title.find("h1", class_="tit-prod").string


navegador.quit()

print (result_title)

# Dump and Save to JSON file (Converter e salvar em um arquivo JSON)
with open('preco.json', 'w', encoding='utf-8') as jp:
    js = json.dumps(preco, indent=4)
    jss = json.dumps(result_title, indent=4)
    jp.write(js)
    jp.write(jss)


