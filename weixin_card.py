import itchat
from PIL import Image


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
    friends = itchat.get_friends()
    for friend in friends:
        print(friend)
        print(friend.UserName)
        itchat.get_head_img(userName=friend.UserName, picDir="D:\\pythonProject\\weixin_card\\img\\" + friend.UserName + ".jpg")
        base_img = Image.open(r'D:\pythonProject\weixin_card\template.png')
        tmp_img = Image.open(r'D:\pythonProject\weixin_card\template.png')
        region = tmp_img
        box = (166, 64, 320, 337)

        # 使用 paste(region, box) 方法将图片粘贴到另一种图片上去.
        # 注意，region的大小必须和box的大小完全匹配。但是两张图片的mode可以不同，合并的时候回自动转化。如果需要保留透明度，则使用RGMA mode
        # 提前将图片进行缩放，以适应box区域大小
        # region = region.rotate(180) #对图片进行旋转
        region = region.resize((box[2] - box[0], box[3] - box[1]))
        base_img.paste(region, box)
        # base_img.show() # 查看合成的图片
        base_img.save('D:\\pythonProject\\weixin_card\\out\\' + friend.UserName + ".jpg")  # 保存图片


itchat.auto_login(hotReload=True)
itchat.run()




