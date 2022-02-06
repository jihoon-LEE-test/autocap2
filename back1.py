from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import shutil
import time
from selenium.webdriver.chrome.options import Options
import pyautogui as pg
import pyperclip
import os
driver=webdriver.Chrome()

driver.get("https://www.google.com/")

def wating_img(name):
    while True:
        find_img = pg.locateOnScreen(name)
        if find_img == None:
            print(find_img)
            time.sleep(2)
        else:
            break
        pg.click(name)


os.system('Chrome.lnk')
pg.moveTo(818, 64)
pg.click()

pyperclip.copy("하나님의 교회")

# 클립보드에 있는 내용을 붙여넣기
pg.hotkey("ctrl", "v")
pg.press('enter')

time.sleep(1)
print(pg.position())

time.sleep(0.5)

pg.moveTo(1675, 187)
pg.click()


if pg.locateOnScreen('ko1.png'):
    w = pg.locateOnScreen('ko1.png')
    pg.click(w)

elif pg.locateOnScreen('en1.png'):
    w = pg.locateOnScreen('en1.png')
    pg.click(w)
else:
    w = pg.locateOnScreen('es1.png')

    pg.click(w)




