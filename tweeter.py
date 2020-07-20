import tweepy
import webbrowser
import time
import api_stuff
import os.path
from os import path
import sys

def check_auth():
    if path.exists(os.path.join(os.path.dirname(__file__), 'auth.txt')):
        f = open(os.path.join(os.path.dirname(__file__), 'auth.txt'), "r")
        auth_lines = f.readlines()
        f.close()
        login(auth_lines)
    else:
        auth_lines = []
        register(auth_lines)
        
def register(auth_lines):
    consumer_key = api_stuff.consumer_key
    consumer_secret = api_stuff.consumer_secret
    callback_uri = 'oob'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
    redirect_url = auth.get_authorization_url()
    print(redirect_url)
    webbrowser.open(redirect_url)
    user_pin_input = input("pin:")
    auth.get_access_token(user_pin_input)
    api = tweepy.API(auth)
    me = api.me()
    print("Welcome " + me.screen_name + "!")
    # save user
    f = open(os.path.join(os.path.dirname(__file__), 'auth.txt'), "a")
    if len(auth_lines) > 0:
        f.write("\n" + me.screen_name + " " + auth.access_token + " " + auth.access_token_secret)
    else:
        f.write(me.screen_name + " " + auth.access_token + " " + auth.access_token_secret)
    tweeter(api)

def login(auth_lines):
    print("Who do you want to login as?")
    option = 0
    for line in auth_lines:
        print(str(option) + " - " + line.split()[0])
        option += 1
    print(str(option) + " - " + "New User\n")
    choice = input("nmbr(/q):")
    try:
        choice = int(choice)
    except ValueError:
        print("canceled.")
        sys.exit()
    if choice > len(auth_lines)-1:
        register(auth_lines)
    else:
        line = auth_lines[choice]
        print("Logging in as " + line.split()[0] + "...")
        access_token = line.split()[1]
        access_token_secret = line.split()[2]

        consumer_key = api_stuff.consumer_key
        consumer_secret = api_stuff.consumer_secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        me = api.me()
        print("Welcome " + me.screen_name + "!")
        tweeter(api)

def tweeter(api):
    while True:
        print("(h for help)")
        cmd = input()
        if cmd == "h":      #help
            print("""
tw      --Tweet.
[>] enter your Tweet.

re      --Reply.
[ID:] ID of the Tweet that you want to reply to.
[>] enter your reply.

sre      --More stable reply. (not needed anymore)
[ID:] ID of the Tweet that you want to reply to.
[ats:] all mentioned @'s
[>] enter your reply.

crt     --Comment-Retweet.
[URL:] URL of the Tweet that you want to comment retweet.
[>] enter your comment.

itw     --Image-Tweet
[count:] how many images you want to attach. (1-4)
[path:] path of your image. The images will be in the order in which you add them.
[>] enter your Tweet.

ire     --Image-Reply
[ID:] ID of the Tweet that you want to reply to.
[count:] how many images you want to attach. (1-4)
[path:] path of your image. The images will be in the order in which you add them.
[>] enter your reply.

isre     --Image-Stable-Reply (not needed anymore)
[ID:] ID of the Tweet that you want to reply to.
[ats:] all mentioned @'s
[count:] how many images you want to attach. (1-4)
[path:] path of your image. The images will be in the order in which you add them.
[>] enter your reply.

icrt    --Image-Comment-Retweet.
[URL:] URL of the Tweet that you want to comment retweet.
[count:] how many images you want to attach. (1-4)
[path:] path of your image. The images will be in the order in which you add them.
[>] enter your comment.

q       --Quit.

h       --Help.""")
    
        elif cmd == "tw":   #tweet
            tweet = input(">")
            api.update_status(tweet)
    
        elif cmd == "re":   #reply
            tw_id = input("ID:")
            tweet = input(">")
            api.update_status(tweet, in_reply_to_status_id = tw_id,  auto_populate_reply_metadata = True)

        elif cmd == "sre":   #reply
            tw_id = input("ID:")
            ats = input("ats:")
            tweet = input(">")
            api.update_status(ats + " " + tweet, in_reply_to_status_id = tw_id)
    
        elif cmd == "crt":  #comment-RT
            url = input("URL:")
            tweet = input(">")
            api.update_status(tweet + " " + url)
    
        elif cmd == "itw":  #image+tweet
            count = int(input("count:"))
            if count > 3:
                img_obj1 = api.media_upload(input("path:"))
            if count > 2:
                img_obj2 = api.media_upload(input("path:"))
            if count > 1:
                img_obj3 = api.media_upload(input("path:"))
            if count > 0:
                img_obj4 = api.media_upload(input("path:"))

            tweet = input(">")
        
            if count >= 4:
                api.update_status(tweet, media_ids=[img_obj1.media_id_string, img_obj2.media_id_string, img_obj3.media_id_string, img_obj4.media_id_string])
            if count == 3:
                api.update_status(tweet, media_ids=[img_obj2.media_id_string, img_obj3.media_id_string, img_obj4.media_id_string])
            if count == 2:
                api.update_status(tweet, media_ids=[img_obj3.media_id_string, img_obj4.media_id_string])
            if count == 1:
                api.update_status(tweet, media_ids=[img_obj4.media_id_string])
    
        elif cmd == "ire":  #image+reply
            tw_id = input("ID:")
            count = int(input("count:"))
            if count > 3:
                img_obj1 = api.media_upload(input("path:"))
            if count > 2:
                img_obj2 = api.media_upload(input("path:"))
            if count > 1:
                img_obj3 = api.media_upload(input("path:"))
            if count > 0:
                img_obj4 = api.media_upload(input("path:"))

            tweet = input(">")
        
            if count >= 4:
                api.update_status(tweet, media_ids=[img_obj1.media_id_string, img_obj2.media_id_string, img_obj3.media_id_string, img_obj4.media_id_string], in_reply_to_status_id = tw_id, auto_populate_reply_metadata = True)
            if count == 3:
                api.update_status(tweet, media_ids=[img_obj2.media_id_string, img_obj3.media_id_string, img_obj4.media_id_string], in_reply_to_status_id = tw_id, auto_populate_reply_metadata = True)
            if count == 2:
                api.update_status(tweet, media_ids=[img_obj3.media_id_string, img_obj4.media_id_string], in_reply_to_status_id = tw_id, auto_populate_reply_metadata = True)
            if count == 1:
                api.update_status(tweet, media_ids=[img_obj4.media_id_string], in_reply_to_status_id = tw_id, auto_populate_reply_metadata = True)
            
        elif cmd == "isre":  #image+stable reply
            tw_id = input("ID:")
            ats = input("ats:")
            count = int(input("count:"))
            if count > 3:
                img_obj1 = api.media_upload(input("path:"))
            if count > 2:
                img_obj2 = api.media_upload(input("path:"))
            if count > 1:
                img_obj3 = api.media_upload(input("path:"))
            if count > 0:
                img_obj4 = api.media_upload(input("path:"))

            tweet = input(">")
        
            if count >= 4:
                api.update_status(ats + " " + tweet, media_ids=[img_obj1.media_id_string, img_obj2.media_id_string, img_obj3.media_id_string, img_obj4.media_id_string], in_reply_to_status_id = tw_id)
            if count == 3:
                api.update_status(ats + " " + tweet, media_ids=[img_obj2.media_id_string, img_obj3.media_id_string, img_obj4.media_id_string], in_reply_to_status_id = tw_id)
            if count == 2:
                api.update_status(ats + " " + tweet, media_ids=[img_obj3.media_id_string, img_obj4.media_id_string], in_reply_to_status_id = tw_id)
            if count == 1:
                api.update_status(ats + " " + tweet, media_ids=[img_obj4.media_id_string], in_reply_to_status_id = tw_id)
    
        elif cmd == "icrt": #image+comment-RT
            url = input("URL:")
            count = int(input("count:"))
            if count > 3:
                img_obj1 = api.media_upload(input("path:"))
            if count > 2:
                img_obj2 = api.media_upload(input("path:"))
            if count > 1:
                img_obj3 = api.media_upload(input("path:"))
            if count > 0:
                img_obj4 = api.media_upload(input("path:"))

            tweet = input(">")
        
            if count >= 4:
                api.update_status(tweet + url, media_ids=[img_obj1.media_id_string, img_obj2.media_id_string, img_obj3.media_id_string, img_obj4.media_id_string])
            if count == 3:
                api.update_status(tweet + url, media_ids=[img_obj2.media_id_string, img_obj3.media_id_string, img_obj4.media_id_string])
            if count == 2:
                api.update_status(tweet + url, media_ids=[img_obj3.media_id_string, img_obj4.media_id_string])
            if count == 1:
                api.update_status(tweet + url, media_ids=[img_obj4.media_id_string])
    
        elif cmd == "q":    #quit
            break

check_auth()
