from selenium import webdriver
import time
from bs4 import BeautifulSoup
import mysql.connector

navegador = webdriver.Chrome()

url = "https://www.pensador.com/frases_status_whatsapp/"
#url = "https://www.kabum.com.br/hardware/placa-de-video-vga/nvidia"



navegador.get(url)
time.sleep(3)

element = navegador.find_element_by_xpath("//body")
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
all_content = soup.find_all("blockquote")

navegador.quit()



for content in all_content:
    titulo = content.find('p').text


    con = mysql.connector.connect(host='localhost', database='frases', user='root', password='')
    inserir = con.cursor()
    sql = "insert into frases (frase) values (%s)"
    val = (titulo, )
    inserir.execute(sql, val)

    con.commit()


