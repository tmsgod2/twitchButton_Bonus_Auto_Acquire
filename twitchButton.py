import datetime
import threading
from selenium import webdriver


def bonus_box():
    try:
        driver.find_element_by_xpath(
            """/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[5]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/button""").click()
        print("점수 획득!", datetime.datetime.now())

        threading.Timer(1500, bonus_box).start()
    except:
        threading.Timer(10, bonus_box).start()


print("아이디 : ", end='-')
Id = input()

print("비밀번호 : ", end='-')
password = input()


print("원하는 스트리머 주소 입력:")
address = input()

print("크롬 드라이브 접속 중....")
driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)

print("트위치 채널 이동중.....")
driver.get(address)
driver.find_element_by_xpath(
    """//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button""").click()

print("아이디 비밀번호 입력 및 로그인")
login = driver.find_element_by_id("login-username")
login.send_keys(Id)
login = driver.find_element_by_id("password-input")
login.send_keys(password)

driver.find_element_by_xpath(
    """/html/body/div[2]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button""").click()
print("토큰 입력:", end='-')
token = input()

token_input = driver.find_element_by_xpath(
    """/html/body/div[2]/div/div/div/div/div/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/input""")

token_input.send_keys(token)

driver.find_element_by_xpath(
    """/html/body/div[2]/div/div/div/div/div/div[1]/div/div/div[3]/div/div[2]/button""").click()

print("보너스 수집 진행", datetime.datetime.now())
bonus_box()
