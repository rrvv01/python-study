from selenium import webdriver # webdriver를 이용해 해당 브라우저를 열기 위해
from selenium.webdriver import ActionChains # 일련의 작업들을(ex.아이디 입력, 비밀번호 입력, 로그인 버튼 클릭...) 연속적으로 실행할 수 있게 하기 위해
from selenium.webdriver.common.keys import Keys # 키보드 입력을 할 수 있게 하기 위해
from selenium.webdriver.common.by import By # html요소 탐색을 할 수 있게 하기 위해
from selenium.webdriver.support.ui import WebDriverWait # 브라우저의 응답을 기다릴 수 있게 하기 위해
from selenium.webdriver.support import expected_conditions as EC # html요소의 상태를 체크할 수 있게 하기 위해
import time# 이 외에도 필요한 모듈이 있다면 따로 호출해준다.
import urllib.request

# 브라우저 꺼짐 방지 옵션
#chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome()
driver.get('https://instagram.com')


time.sleep(3)

i = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
i.send_keys('guksuukim@naver.com')
p = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
p.send_keys('rmstn001~!')
l = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
l.click()

time.sleep(5)


#페이지이동
time.sleep(2)
driver.get('https://www.instagram.com/explore/tags/%EA%B9%80%EC%B1%84%EC%9B%90/')
#첫번째사진누름
driver.implicitly_wait(10)
e = driver.find_element(By.CSS_SELECTOR, '._aagw')
e.click()
#사진저장
time.sleep(5)
이미지 = driver.find_element(By.CSS_SELECTOR, '.x5yr21d').get_attribute('src')
urllib.request.urlretrieve(이미지, '1.jpg')



