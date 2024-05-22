# Fiicen-py
FiicenというSNSに使えるAPIラッパー
### >>```pip install fiicen-py```<<  
## 必須モジュール  
- requests
- bs4
## 使い方  
#### example.py
```py
from fiicen_py import Fiicen

fiicen=Fiicen(name="ユーザー名",password="パスワード")#ログイン、nameとpasswordを設定しなかったらログインをスキップします
print(fiicen.fly_circle(contents="メインの文章",vote_choices1="投票の選択肢1",vote_choices2="投票の選択肢2"))
print(fiicen.change_profile(display_name="表示名",introduce="自己紹介"))
print(fiicen.follow(followed_id="ユーザーID"))#ユーザーIDの取得方法がリクエスト見るしかなさそうなので使い道ナシ？
print(fiicen.get_topic())#タイムラインをhtmlで取得する

fiicen=Fiicen()#アカウント作成の時はログインをスキップ
print(fiicen.create_account(name="ユーザー名",display_name="表示名",password="パスワード"))
print(fiicen.check_account_name(name="ユーザー名"))#ユーザー名が使用されているかどうか確認する...使いどころは不明
```
使い方は#コメントに書いてある通りで、それ以上はなにもないです  
返される値もステータスコードくらいで重要なものはありません  
### 返される値  
```.fly_circle()``` / ```.change_profile()``` / ```.follow()``` / ```.create_account()``` 
- **ステータスコード**  
  言わずもがな200が成功、それ以外はエラー  

```get_topic()``` 
- **html**  
  bs4などで要素を抽出する必要アリ

```.check_account_name()```
- **bool**  
  ```True``` or ```False```
## コンタクト
Discord サーバー / https://discord.gg/aSyaAK7Ktm
Discord ユーザー名 / .taka.
