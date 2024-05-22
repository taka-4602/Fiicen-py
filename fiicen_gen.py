from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

def account_gen(account_name:str,display_name:str,password:str):
    driver.get('https://fiicen.jp/login/')#reCaptha追加されてるのにこのリクエストがないとcsrftokenが生成されないやばいバグが修正されてない (5/22)
    driver.get('https://fiicen.jp/signup/')
    sleep(1)
    try:
        account_name_input=driver.find_element(By.ID,"account_name")
    except:
        sleep(2)
        account_name_input=driver.find_element(By.ID,"account_name")
    account_name_input.send_keys(account_name)
    driver.find_element(By.XPATH, '//*[@onclick="openSignupPage(1, 2);"]').click()
    sleep(1)
    account_display_name_input=driver.find_element(By.ID,"display_name")
    account_display_name_input.send_keys(display_name)
    driver.find_element(By.XPATH, '//*[@onclick="openSignupPage(2, 3);"]').click()
    sleep(1)
    password_input=driver.find_element(By.ID,"password")
    password_input.send_keys(password)
    driver.find_element(By.XPATH, '//*[@onclick="openSignupPage(3, 4);"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@onclick="openSignupPage(4, 5);"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@onclick="openSignupPage(5, 6), submitSignup()"]').click()
    return "OK"

account_gen("ユーザー名","表示名","パスワード")