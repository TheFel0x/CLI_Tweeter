import tweepy
import webbrowser
import time
import api_stuff

# login ----------------------------------------------------------------------------
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
# login done -----------------------------------------------------------------------

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

sre      --More stable reply.
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
    
    elif cmd == "re":   #reply
        id = input("ID:")
        tweet = input(">")
        api.update_status(tweet, in_reply_to_status_id = id)

    elif cmd == "sre":   #reply
        id = input("ID:")
        ats = input("ats:")
        tweet = input(">")
        api.update_status(ats + " " + tweet, id)
    
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
        id = input("ID:")
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
            api.update_status(tweet, media_ids=[img_obj1.media_id_string, img_obj2.media_id_string, img_obj3.media_id_string, img_obj4.media_id_string], in_reply_to_status_id = id)
        if count == 3:
            api.update_status(tweet, media_ids=[img_obj2.media_id_string, img_obj3.media_id_string, img_obj4.media_id_string], in_reply_to_status_id = id)
        if count == 2:
            api.update_status(tweet, media_ids=[img_obj3.media_id_string, img_obj4.media_id_string], in_reply_to_status_id = id)
        if count == 1:
            api.update_status(tweet, media_ids=[img_obj4.media_id_string], in_reply_to_status_id = id)
    
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
