https://pythondocs.net/selenium/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95/
https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/
https://pythondocs.net/selenium/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95/
//*[@id="input"]
driver.close() #현재 탭 닫기
driver.quit()  #브라우저 닫기

driver.back() #뒤로가기
driver.forward() #앞으로가기

driver.window_handles[0] #브라우저 탭 객체를 리스트로 반환. [0] 은 인덱싱. 첫번재 탭을 의미

driver.switch_to.window(driver.window_handles[0]) #첫번째 탭으로 이동
driver.switch_to.window(driver.window_handles[1]) #두번째 탭으로 이동
driver.switch_to.window(driver.window_handles[2]) #세번째 탭으로 이동

driver.switch_to.window(driver.window_handles[0]) #닫을 탭으로 이동 후

driver.close()

driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/button/span[2]') #xpath 로 접근
driver.find_element_by_class_name('ico_search_submit')  #class 속성으로 접근
driver.find_element_by_id('ke_kbd_btn') #id 속성으로 접근
driver.find_element_by_link_text('회원가입')    #링크가 달려 있는 텍스트로 접근
driver.find_element_by_css_selector('#account > div > a')   #css 셀렉터로 접근
driver.find_element_by_name('join') #name 속성으로 접근
driver.find_element_by_partial_link_text('가입')  #링크가 달려 있는 엘레먼트에 텍스트 일부만 적어서 해당 엘레먼트에 접근
driver.find_element_by_tag_name('input')    #태그 이름으로 접근

driver.find_element_by_tag_name('input').find_element_by_tag_name('a')  #input 태그 하위태그인 a 태그에 접근
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/button/span[2]').find_element_by_name('join') #xpath 로 접근한 엘레먼트의 안에 join 이라는 속성을 가진 tag 엘레

driver.find_element_by_id('ke_kbd_btn').click()

driver.find_element_by_id('ke_awd2_btn').send_keys('텍스트 입력')