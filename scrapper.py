import time
import requests
import os
youtubekey=os.getenv("google_key")
graphapi=os.getenv("graphapi_access")
facebookappid=os.getenv("facebook_appid")
appsecret_proof=os.getenv("appsecret_proof")
facebookaccess_token=os.getenv("facebookaccess_token")
def scrape(link):
    result = None
    arr=[]
    arr.append(link.split("."))
    temp=[]
    n=0
    if arr[0][1].lower()=="youtube":
        link=link.strip("/")
        temp.append(link.split("/"))
        subs=requests.get(f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id=%s&key=%s" % (temp[0][-1],youtubekey)).json()
        return subs["items"][0]["statistics"]["subscriberCount"]
    elif arr[0][1].lower()=="instagram":
        

        link=link.strip("/")
        temp.append(link.split("/"))
        followers=requests.get("https://graph.facebook.com/v3.2/17841419573538314?fields=business_discovery.username(%s){followers_count}&access_token=%s" % (temp[0][-1],graphapi)).json()
        return followers["business_discovery"]["followers_count"]
        
            
    elif arr[0][1].lower()=="facebook":
        
        link=link.strip("/")
        temp.append(link.split("/"))
        followers=requests.get("https://graph.facebook.com/v3.2/%s/?fields=fan_count&appsecret_proof=%s&access_token=%s" % (temp[0][-1],appsecret_proof,facebookaccess_token )).json()
        return followers["fan_count"]
                
        
        