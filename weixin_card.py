import itchat
from img_mager import create_img
import time


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
    friends = itchat.get_friends()
    i = 0
    for friend in friends:
        try:
            print(friend)
            print(friend.UserName)
            if friend.RemarkName == '连鸿鹤':
                continue
            if i == 0:
                from_user = friend.UserName
                to_user = friend.UserName
            else:
                to_user = friend.UserName
            itchat.get_head_img(userName=friend.UserName, picDir="./img/" + friend.UserName + ".jpg")
            create_img(from_user, to_user)
            itchat.send_image(f"./head_img/{to_user}.jpg", toUserName=to_user)
            time.sleep(2)
            i = 10
        except Exception as e:
            print(e)


itchat.auto_login(hotReload=True)
itchat.run()




