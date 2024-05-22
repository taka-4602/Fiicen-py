from .main import Fiicen

fiicen=Fiicen(name="ユーザー名",password="パスワード")#ログイン、nameとpasswordを設定しなかったらログインをスキップします
print(fiicen.fly_circle(contents="メインの文章",vote_choices1="投票の選択肢1",vote_choices2="投票の選択肢2"))#リプライをつける時は circle_id="リプするサークルID"
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
