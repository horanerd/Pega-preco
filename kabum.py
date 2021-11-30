from selenium import webdriver
import time
from bs4 import BeautifulSoup
import mysql.connector

navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#url = "https://www.kabum.com.br/hardware/placa-de-video-vga/amd-ati"
url = "https://www.kabum.com.br/hardware/placa-de-video-vga/nvidia"



navegador.get(url)
time.sleep(10)

element = navegador.find_element_by_xpath("//body//div[@id='__next']//main")
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
all_content = soup.find_all(class_="productCard")

navegador.quit()


for content in all_content:
    titulo = content.find('h2').text
    preco = content.find(class_="availablePricesCard").text

    con = mysql.connector.connect(host='localhost', database='preco', user='root', password='')
    inserir = con.cursor()
    sql = "insert into kabum (titulo, preco) values (%s, %s)"
    val = (titulo, preco)
    inserir.execute(sql, val)

    con.commit()

