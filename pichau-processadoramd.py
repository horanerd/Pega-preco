from selenium import webdriver
import time
from bs4 import BeautifulSoup
import mysql.connector

navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#url = "https://www.pichau.com.br/hardware/processadores/intel"
url = "https://www.pichau.com.br/hardware/processadores/amd"



navegador.get(url)
time.sleep(2)

element = navegador.find_element_by_xpath("//body//main")
html_content = element.get_attribute('outerHTML')

div = navegador.find_element_by_xpath("//body//main//div[@class='MuiContainer-root']//div")
div_content = div.get_attribute('outerHTML')
#preco = BeautifulSoup(div_content, 'html.parser')

soup = BeautifulSoup(html_content, 'html.parser')
all_content = soup.find_all(class_="MuiGrid-item")




navegador.quit()

for content in all_content:
    titulo = content.find('h2').text
    preco_separa = content.find('div').text
    preco_separado = preco_separa.split('vista')
    preco_sno = preco_separado[-1].split('no')
    preco = preco_sno[0]


 
    con = mysql.connector.connect(host='localhost', database='preco', user='root', password='')
    inserir = con.cursor()
    sql = "insert into pichauprocessador (titulo, preco) values (%s, %s)"
    val = (titulo, preco)
    inserir.execute(sql, val)

    con.commit()

