#Hover Action

import unittest
from selenium import webdriver # se Improta libreria
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")
driver.get("https://www.google.com/")
time.sleep(3)
elem = driver.find_element_by_link_text("Privacidad")

hover = ActionChains(driver).move_to_element(elem)
hover.perform()