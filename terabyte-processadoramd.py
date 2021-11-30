from selenium import webdriver
import time
from bs4 import BeautifulSoup
import mysql.connector

navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#url = "https://www.terabyteshop.com.br"
#url ="https://www.terabyteshop.com.br/hardware/processadores/intel"
url ="https://www.terabyteshop.com.br/hardware/processadores/amd-ryzen"


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
    sql = "insert into terabyteprocessador (titulo, preco) values (%s, %s)"
    val = (titulo, preco)
    inserir.execute(sql, val)

    con.commit()