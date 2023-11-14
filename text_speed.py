"""
Code that functions as a way to cheap the humanbenchmark's typewriter
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui
import time

browser = webdriver.Chrome()
browser.get("https://humanbenchmark.com/tests/typing")
data = browser.page_source

soup = BeautifulSoup(data, 'html.parser')
span_tags = soup.find_all('span', class_ = 'incomplete')

time.sleep(5) #because accept cookies fucks me in the ass 
text = ''.join([span.text for span in span_tags])
pyautogui.typewrite(text)
time.sleep(10)
