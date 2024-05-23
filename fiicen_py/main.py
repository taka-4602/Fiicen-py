import requests
from bs4 import BeautifulSoup

class FiicenError(Exception):
    pass
class Fiicen():
    def __init__(self,name:str=None,password:str=None,proxy:dict=None) -> None:
        self.proxy=proxy
        self.session=requests.Session()
        self.session.get("https://fiicen.jp/login/",proxies=self.proxy)#このリクエストがないとcsrftokenが生成されないやばいバグがある
        self.headers={
            "X-Csrftoken": self.session.cookies['csrftoken'],
        }
        if name!=None and password!=None:
            login_get=self.session.get("https://fiicen.jp/login/",proxies=self.proxy)
            soup=BeautifulSoup(login_get.text,"html.parser")
            account_info={
                "csrfmiddlewaretoken":str(soup.find("input").get("value")),
                "account_name":name,
                "password":password
            }
            
            login=self.session.post("https://fiicen.jp/login/",headers=self.headers,data=account_info,proxies=self.proxy)
            soup=BeautifulSoup(login.text,"html.parser")
            title=soup.find("title")
            if title.text=="ログイン / Fiicen":
                error=soup.find(class_="info-error")
                raise FiicenError(error.text)

    def check_account_name(self,name:str):
        return bool(requests.get(f"https://fiicen.jp/signup/check_account_name/?account_name={name}").json()['is_taken'])
    
    def create_account(self,name:str,display_name:str,password:str):
        self.session.get("https://fiicen.jp/signup/",proxies=self.proxy)
        account_info={
            "account_name":name,
            "display_name":display_name,
            "password":password,
            "gender":"9"
        }
        create=self.session.post("https://fiicen.jp/signup/",headers=self.headers,data=account_info,proxies=self.proxy)
        try:
            if create.json()["status"]!="success":
                raise FiicenError(create.json())
        except:
            raise FiicenError(create.text)
        return create.status_code

    def fly_circle(self,contents:str,vote_choices1:str="",vote_choices2:str=""):
        circle_info={
            "contents": contents,
            "vote_choices1": vote_choices1,
            "vote_choices2": vote_choices2,
        }
        fly=self.session.post("https://fiicen.jp/circle/create/",headers=self.headers,data=circle_info,proxies=self.proxy)
        if fly.status_code!=200:
            raise FiicenError(fly.text)
        return fly.status_code
    
    def get_topic(self):
        topic=self.session.get("https://fiicen.jp/circle/block/topic/1/",headers=self.headers,proxies=self.proxy)
        if topic.status_code!=200:
            raise FiicenError(topic.text)
        return topic.text
    
    def change_profile(self,display_name:str,introduce:str):
        profile_info={
            "display_name":display_name,
            "introduce":introduce
        }
        profile=self.session.post("https://fiicen.jp/settings/profile/",headers=self.headers,data=profile_info,proxies=self.proxy)
        if profile.status_code!=200:
            raise FiicenError(profile.text)
        return profile.status_code
    
    def follow(self,followed_id:str):
        follow_info={
            "followed_id":followed_id
        }
        follow=self.session.post("https://fiicen.jp/account/follow/",headers=self.headers,data=follow_info,proxies=self.proxy)
        if follow.status_code!=200:
            raise FiicenError(follow.text)
        return follow.status_code
    
    def like(self,circle_id:str):
        like_info={
            "circle_id":circle_id
        }
        like=self.session.post("https://fiicen.jp/circle/like/",headers=self.headers,data=like_info,proxies=self.proxy)
        if like.status_code!=200:
            raise FiicenError(like.text)
        return like.status_code
    
    def refly(self,circle_id:str):
        refly_info={
            "circle_id":circle_id
        }
        refly=self.session.post("https://fiicen.jp/circle/refly/",headers=self.headers,data=refly_info,proxies=self.proxy)
        if refly.status_code!=200:
            raise FiicenError(refly.text)
        return refly.status_code
    
    def notification(self):
        noti=self.session.post("https://fiicen.jp/notification/count/",headers=self.headers,proxies=self.proxy)
        if noti.status_code!=200:
            raise FiicenError(noti.text)
        return int(noti.json()["count"])
    
    def fix_circle(self,circle_id:str):
        fix_info={
            "circle_id":circle_id
        }
        fix=self.session.post("https://fiicen.jp/circle/fix/",headers=self.headers,data=fix_info,proxies=self.proxy)
        if fix.status_code!=200:
            raise FiicenError(fix.text)
        return fix.json()
    
    def report(self,circle_id:str,type:str="harassment"):
        if type=="harassment" or type=="sensitive" or type=="spam" or type=="suicide" or type=="spoofing" or type=="privacy" or type=="violence" or type=="misinformation" or type=="discrimination":
            None
        else:
            raise FiicenError("typeは 'harassment' / 'sensitive' / 'spam' / 'suicide' / 'spoofing' / 'privacy' / 'violence' / 'misinformation' / 'discrimination' のどれかから選んでください")
        report_info={
            "type": type
        }
        report=self.session.post(f"https://fiicen.jp/report/circle/{circle_id}",headers=self.headers,data=report_info,proxies=self.proxy)
        if report.status_code!=200:
            raise FiicenError(report.text)
        return report.status_code
    
    def vote(self,circle_id:str,choices_id:str):
        vote_info={
            "circle_id": circle_id,
            "choices_id": choices_id
        }
        vote=self.session.post("https://fiicen.jp/circle/vote/",headers=self.headers,data=vote_info,proxies=self.proxy)
        if vote.status_code!=200:
            raise FiicenError(vote.text)
        return vote.json()