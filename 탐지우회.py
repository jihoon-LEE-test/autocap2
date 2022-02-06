from selenium import webdriver
import subprocess
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
import time
import pyperclip

try:
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp1"')  # 디버거 크롬 구동
except:
    subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp1"')  # 디버거 크롬 구동

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')
options.add_argument("--start-maximized")
options.add_argument('headless')
options.add_argument('--incognito')
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_extension(r'GoFullPage---Full-Page-Screen-Capture.crx') # uBlock Origin extension crx 파일 추가
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)

except:
    chromedriver_autoinstaller.install('./')
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)

driver.implicitly_wait(20)
driver.get('https://www.naver.co.kr')

time.sleep(2)
driver.get('https://www.google.com/webhp?hl=en')
