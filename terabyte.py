from selenium import webdriver
import time
from bs4 import BeautifulSoup
import mysql.connector

navegador = webdriver.Chrome()

#url = "https://www.terabyteshop.com.br"
#url ="https://www.terabyteshop.com.br/hardware/placas-de-video/nvidia-geforce"
url ="https://www.terabyteshop.com.br/hardware/placas-de-video/amd-radeon"


navegador.get(url)
time.sleep(10)

element = navegador.find_element_by_xpath("//body//div[@id='body']//div[@class='container']")
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
all_content = soup.find_all(class_="pbox")

navegador.quit()


for content in all_content:
    titulo = content.find('h2').text
    preco = content.find(class_="prod-new-price").text

    con = mysql.connector.connect(host='localhost', database='preco', user='root', password='')
    inserir = con.cursor()
    sql = "insert into terabyte (titulo, preco) values (%s, %s)"
    val = (titulo, preco)
    inserir.execute(sql, val)

    con.commit()