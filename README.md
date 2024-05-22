# Fiicen-py
FiicenというSNSに使えるAPIラッパー
### >>```pip install fiicen-py```<<  
## 必須モジュール  
- requests
- bs4
#### アカウントジェネレーターを使う場合  
- selenium
## 使い方  
#### example.py
```py
from fiicen_py import Fiicen

fiicen=Fiicen(name="ユーザー名",password="パスワード")#ログイン、nameとpasswordを設定しなかったらログインをスキップします
print(fiicen.fly_circle(contents="メインの文章",vote_choices1="投票の選択肢1",vote_choices2="投票の選択肢2"))
print(fiicen.change_profile(display_name="表示名",introduce="自己紹介"))
print(fiicen.follow(followed_id="ユーザーID"))#ユーザーIDの取得方法がリクエスト見るしかなさそうなので使い道ナシ？
print(fiicen.get_topic())#タイムラインをhtmlで取得する
print(fiicen.notification())#通知の数をintで返す
print(fiicen.like(circle_id="サークルID"))#いいね！
print(fiicen.refly(circle_id="サークルID"))#リフライ
print(fiicen.fix_circle(circle_id="サークルID"))#プロフィールにサークルを固定
print(fiicen.report(circle_id="サークルID",type="通報理由"))#サークルを通報、理由は：harassment / sensitive / spam / suicide / spoofing / privacy / violence / misinformation / discrimination から選ぶ

fiicen=Fiicen()#アカウント作成の時はログインをスキップ
print(fiicen.create_account(name="ユーザー名",display_name="表示名",password="パスワード"))
print(fiicen.check_account_name(name="ユーザー名"))#ユーザー名が使用されているかどうか確認する...使いどころは不明
```
使い方は#コメントに書いてある通りで、それ以上はなにもないです  
返される値もステータスコードくらいで重要なものはありません  
### 返される値  
```.fly_circle()``` / ```.change_profile()``` / ```.follow()``` / ```.create_account()``` / ```.like()``` / ```.refly()``` / ```.report()``` 
- **ステータスコード**  
  言わずもがな200が成功、それ以外はエラーになる  

```get_topic()``` 
- **html**  
  bs4などで要素を抽出する必要アリ

```.check_account_name()```
- **bool**  
  ```True``` or ```False```

```.fix_circle()```
- **dict**  
  ```{result: "fixed"}``` or ```{result: "unfixed"}```

```.notification()```
- **int**  
  ```0,1,2,3,4,5,6......```
## アカウントジェネレーター  
#### fiicen_gen.py
```py
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
```  
5/22の夜にアカウント生成だけreCaptcha(v2)が必須になったみたいなので、ヘッドレスブラウザーでアカウントを作成するジェネレーターを作りました  
無料でキャプチャーを突破するのはこうするしかないと思います  
有料ソルバー使うってあなたはそもそもラッパー必要ないでしょ！🫵
## コンタクト
Discord サーバー / https://discord.gg/aSyaAK7Ktm  
Discord ユーザー名 / .taka.
