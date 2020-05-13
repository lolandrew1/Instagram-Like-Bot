import selenium
from selenium import webdriver
import time
import keyboard

browser = webdriver.Firefox()
browser.get('https://www.instagram.com/')

time.sleep(1)


elemLogin = browser.find_element_by_css_selector('div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
elemPassword = browser.find_element_by_css_selector('div.-MzZI:nth-child(3) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')

elemLogin.send_keys('andrwwng')
elemPassword.send_keys('Americansoldiers1!')

elemLogin.submit()

#log into instagram-------------------------------------

time.sleep(5)

try:
    elemNotNow = browser.find_element_by_css_selector('button.aOOlW:nth-child(2)')
    elemNotNow.click()

except selenium.common.exceptions.NoSuchElementException:
    print('could not find the turn notifications on button')
    pass

#don't turn on notifications----------------------------

try:
    elemNotSave = browser.find_element_by_css_selector('button.sqdOP:nth-child(1)')
    elemNotSave.click()

except selenium.common.exceptions.NoSuchElementException:
    print('could not find the save password and login button')
    pass

#don't save password and login---------------------------

try:
    elemNotNow = browser.find_element_by_css_selector('button.aOOlW:nth-child(2)')
    elemNotNow.click()

except selenium.common.exceptions.NoSuchElementException:
    print('could not find the turn notifications on button')
    pass

#don't turn on notifications----------------------------



try:
    elemClose = browser.find_element_by_css_selector('div.WaOAr:nth-child(3) > button:nth-child(1) > svg:nth-child(1) > path:nth-child(1)')
    elemClose.click()
except selenium.common.exceptions.NoSuchElementException: 
    print('could not find the close button')
    pass

#closes the see who liked the photo popup, button-----------------------

likePart1 = 'article._8Rm4L:nth-child('
likePart2 = ') > div:nth-child(3) > section:nth-child(1) > span:nth-child(1) > button:nth-child(1) > svg:nth-child(1)'
#likePart1 + (number) + likePart2 <- the css_selector for each pic

for i in range(1, 5):
    likeSelec = likePart1 + str(i) + likePart2
    likeElem = browser.find_element_by_css_selector(likeSelec)
    likeElem.click()


    for j in range(1, 22):
        time.sleep(0.1)
        keyboard.press('down')

#scroll and like photos----------------------------------