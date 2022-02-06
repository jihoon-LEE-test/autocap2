from selenium import webdriver
import subprocess
from selenium.webdriver.common.alert import Alert
import time
import warnings
import pyautogui
warnings.filterwarnings(action='ignore')
# selenium으로 무엇인가 입력하기 위한 import
from selenium.webdriver.common.keys import Keys
try:
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp1"')  # 디버거 크롬 구동
except:
    subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp1"')  # 디버거 크롬 구동


options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("--start-maximized")
options.add_argument("disable-gpu")
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_extension(r'GoFullPage---Full-Page-Screen-Capture.crx')
options.add_argument('--incognito')
# 유의: chromedriver를 위에서 받아준
# chromdriver(windows는 chromedriver.exe)의 절대경로로 바꿔주세요!

driver = webdriver.Chrome('chromedriver', options=options)
url1= 'https://www.google.co.kr/search?q=%ED%95%98%EB%82%98%EB%8B%98%EC%9D%98%EA%B5%90%ED%9A%8C+%EC%84%B8%EA%B3%84%EB%B3%B5%EC%9D%8C%EC%84%A0%EA%B5%90%ED%98%91%ED%9A%8C&ei=Pk3_YeG0A4XqwQPJ8ZOIDQ&ved=0ahUKEwjhy4DDner1AhUFdXAKHcn4BNEQ4dUDCA4&uact=5&oq=%ED%95%98%EB%82%98%EB%8B%98%EC%9D%98%EA%B5%90%ED%9A%8C+%EC%84%B8%EA%B3%84%EB%B3%B5%EC%9D%8C%EC%84%A0%EA%B5%90%ED%98%91%ED%9A%8C&gs_lcp=Cgdnd3Mtd2l6EAMyCwguEIAEEMcBEKMCMgUIABCABDIFCAAQgAQyCwguEIAEEMcBEK8BMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgUILhCABDoECAAQQzoRCC4QgAQQsQMQgwEQxwEQowI6BggAEAoQHjoFCCEQoAE6CAgAEA0QChAeOgoILhDHARCjAhANOgQIABANOgoILhDHARCvARANOgYIABANEB46BAgAEB46AggmSgYIPBICMjFKBAhBGAFKBAhGGABQ0gVY80hglUtoFXAAeASAAZICiAGvIpIBBjIuMzQuMpgBAKABAcABAQ&sclient=gws-wiz'
url2= 'https://www.google.com/search?q=world+mission+society+church+of+god&rlz=1C1SQJL_koKR866KR866&oq=world+&aqs=chrome.0.69i59j69i57j0i433i512j0i131i433i512j46i199i465i512j69i60l3.865j0j9&sourceid=chrome&ie=UTF-8'
url3= 'https://www.google.com.pe/search?q=Iglesia+de+Dios+Sociedad+Misionera+Mundial&rlz=1C1SQJL_koKR866KR866&oq=Iglesia+de+Dios+Sociedad+Misionera+Mundial&aqs=chrome..69i57.393j0j4&sourceid=chrome&ie=UTF-8'

driver.get(url1)
driver.implicitly_wait(1)

#설정 버튼
driver.find_element_by_xpath('//*[@id="searchform"]/div[2]/div/div[1]').click()
driver.implicitly_wait(3)
#검색언어 버튼 클릭
driver.find_element_by_xpath('//*[@id="elPddd"]/div[3]/div[2]/a').click()
driver.implicitly_wait(3)
#한국어 버튼 클릭
driver.find_element_by_xpath('//*[@id="langtko"]/div/span[2]').click()
#저장버튼 누르기
driver.find_element_by_xpath('//*[@id="form-buttons"]/div[1]').click()
driver.implicitly_wait(3)
#알림창 끄기
while True:
    if Alert(driver):
        da = Alert(driver)
        da.accept()
        break;
    time.sleep(0.5)
#기다림
driver.implicitly_wait(3)

#설정 버튼
driver.find_element_by_xpath('//*[@id="searchform"]/div[2]/div/div[1]').click()
#검색언어 버튼 클릭
driver.find_element_by_xpath('//*[@id="elPddd"]/div[3]/div[2]/a').click()

driver.implicitly_wait(3)
#검색결과 버튼 클릭
driver.find_element_by_xpath('//*[@id="srhSecLink"]/a').click()
#자세히 클릭
driver.find_element_by_xpath('//*[@id="regionanchormore"]').click()
#대한민국 클릭
driver.find_element_by_xpath('//*[@id="regionoKR"]/div/span[2]').click()
#저장버튼 클릭
driver.find_element_by_xpath('//*[@id="form-buttons"]/div[1]').click()

#알람 끄기
while True:
    if Alert(driver):
        da = Alert(driver)
        da.accept()
        break;
    time.sleep(0.5)

driver.implicitly_wait(1)
time.sleep(1)
pyautogui.hotkey('f5')
time.sleep(1)
pyautogui.hotkey('alt', 'shift','p')

time.sleep(7)

################################################################
#영어 검색 시작
driver.get(url2)

#설정 버튼
driver.find_element_by_xpath('//*[@id="searchform"]/div[2]/div/div[1]').click()
driver.implicitly_wait(3)
#검색언어 버튼 클릭
driver.find_element_by_xpath('//*[@id="elPddd"]/div[3]/div[2]/a').click()
driver.implicitly_wait(3)
#영어 버튼 클릭
driver.find_element_by_xpath('//*[@id="langten"]/div/span[2]').click()
#저장버튼 누르기
driver.find_element_by_xpath('//*[@id="form-buttons"]/div[1]').click()
driver.implicitly_wait(3)
#알림창 끄기
while True:
    if Alert(driver):
        da = Alert(driver)
        da.accept()
        break;
    time.sleep(0.5)
#기다림
driver.implicitly_wait(3)

#설정 버튼
driver.find_element_by_xpath('//*[@id="searchform"]/div[2]/div/div[1]').click()
#검색언어 버튼 클릭
driver.find_element_by_xpath('//*[@id="elPddd"]/div[3]/div[2]/a').click()

driver.implicitly_wait(3)
#검색결과 버튼 클릭
driver.find_element_by_xpath('//*[@id="srhSecLink"]/a').click()
#자세히 클릭
driver.find_element_by_xpath('//*[@id="regionanchormore"]').click()
#미국 클릭
driver.find_element_by_xpath('//*[@id="regionoUS"]/div/span[2]').click()
#저장버튼 클릭
driver.find_element_by_xpath('//*[@id="form-buttons"]/div[1]').click()

#알람 끄기
while True:
    if Alert(driver):
        da = Alert(driver)
        da.accept()
        break;
    time.sleep(0.5)

#캡처 전 화면 새로고치고 충분히 기다리기
driver.implicitly_wait(1)
time.sleep(1)
pyautogui.hotkey('f5')
time.sleep(1)

#캡쳐 시작
pyautogui.hotkey('alt', 'shift','p')
time.sleep(7)


################################################################
#서어 검색 시작
driver.get(url3)

#설정 버튼
driver.find_element_by_xpath('//*[@id="searchform"]/div[2]/div/div[1]').click()
driver.implicitly_wait(3)
#검색언어 버튼 클릭
driver.find_element_by_xpath('//*[@id="elPddd"]/div[3]/div[2]/a').click()
driver.implicitly_wait(3)
#서어 버튼 클릭
driver.find_element_by_xpath('//*[@id="langtes"]/div/span[2]').click()
#저장버튼 누르기
driver.find_element_by_xpath('//*[@id="form-buttons"]/div[1]').click()
driver.implicitly_wait(3)
#알림창 끄기
while True:
    if Alert(driver):
        da = Alert(driver)
        da.accept()
        break;
    time.sleep(0.5)
#기다림
driver.implicitly_wait(3)

#설정 버튼
driver.find_element_by_xpath('//*[@id="searchform"]/div[2]/div/div[1]').click()
#검색언어 버튼 클릭
driver.find_element_by_xpath('//*[@id="elPddd"]/div[3]/div[2]/a').click()

driver.implicitly_wait(3)
#검색결과 버튼 클릭
driver.find_element_by_xpath('//*[@id="srhSecLink"]/a').click()
#자세히 클릭
driver.find_element_by_xpath('//*[@id="regionanchormore"]').click()
#페루 클릭
driver.find_element_by_xpath('//*[@id="regionoPE"]/div/span[2]').click()
#저장버튼 클릭
driver.find_element_by_xpath('//*[@id="form-buttons"]/div[1]').click()

#알람 끄기
while True:
    if Alert(driver):
        da = Alert(driver)
        da.accept()
        break;
    time.sleep(0.5)

#캡처 전 화면 새로고치고 충분히 기다리기
driver.implicitly_wait(1)
time.sleep(1)
pyautogui.hotkey('f5')
time.sleep(1)

#캡쳐 시작
pyautogui.hotkey('alt', 'shift','p')

