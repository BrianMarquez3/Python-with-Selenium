#Busqueda

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time


palabra_busqueda = "sele"
driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")
driver.get("https://www.google.com/")
time.sleep(3)

busqueda  = driver.find_element_by_name("q")
busqueda.send_keys(palabra_busqueda)
time.sleep(3)

for i in range(1,11):
    Elementos = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/ul/li["+str(i)+"]/div/div[2]/div/span/b").text
    print(palabra_busqueda + Elementos)
driver.close()



