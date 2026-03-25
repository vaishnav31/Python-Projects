#urllib3 and  insta bot library are used.

from instabot import Bot
bot=Bot()

#username and  password enter automatically loggin
bot.login(username="jone_python08",password="3658328")

#then  this fuction using  you want follow the aany person
bot.follow('ws')

#this fuction used to automatically upload the photo
bot.upload_story_photo("car.jpg",caption="i love python")

#automatically unfollow 
bot.unfollow("radom_car")

#automatically unfollow  everyone
bot.unfollow_everyone("automatically unfollow everyone")

#automatically send message
bot.send_message("i love python",["car_rahul"])

#get inforamtion of  follower
followers=bot.get_user_followers("car_rahul")
for follower in followers:
    print(bot.get_user_info(follower))

#information  about follower
following=bot.get_user_following("car_rahul")
for Following in following:
    print(bot.get_user_info(Following))