# -*- coding:utf8 -*-

import random

from PIL import Image, ImageFont, ImageDraw

words = ['过放荡不羁的生活，\n容易得像顺水推舟，\n但是要结识良朋益友，\n却难如登天。',
         '生活有度，\n人生添寿。',
         '我读的书愈多，\n就愈亲近世界，\n愈明了生活的意义，\n愈觉得生活的重要。']


def img_circle(ima):
    size = ima.size
    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        ima = ima.resize((r2, r2), Image.ANTIALIAS)
    imb = Image.new('RGBA', (r2, r2), (255, 255, 255, 0))
    pima = ima.load()
    pimb = imb.load()
    r = float(r2 / 2)  # 圆心横坐标
    for i in range(r2):
        for j in range(r2):
            lx = abs(i - r + 0.5)  # 到圆心距离的横坐标
            ly = abs(j - r + 0.5)  # 到圆心距离的纵坐标
            l = pow(lx, 2) + pow(ly, 2)
            if l <= pow(r, 2):
                pimb[i, j] = pima[i, j]
    return imb


def create_img(from_user, to_user):
    base_img = Image.open(f'./templates/template_{random.randrange(0, 7)}.jpg')
    my_tmp_img = Image.open(f"./img/{from_user}.jpg")
    my_region = img_circle(my_tmp_img)

    box = (60, 60, 270, 270)

    other_tmp_img = Image.open(f"./img/{to_user}.jpg")
    other_region = img_circle(other_tmp_img)
    other_box = (230, 60, 440, 270)

    my_region = my_region.resize((box[2] - box[0], box[3] - box[1]))
    other_region = other_region.resize((other_box[2] - other_box[0], other_box[3] - other_box[1]))
    base_img.paste(my_region, box)
    base_img.paste(other_region, other_box)
    path_to_ttf = './ttf/ArialUnicode.ttf'
    font = ImageFont.truetype(path_to_ttf, 40)
    draw = ImageDraw.Draw(base_img)
    draw.text(xy=(30, 400), text=random.choice(words), font=font, fill=(255, 0, 0, 255))

    # base_img.show() # 查看合成的图片
    # base_img.save(f'./head_img/{to_user}.jpg')  # 保存图片
    print(base_img)
    base_img.save(f'./abc.jpg')  # 保存图片


create_img("@0fefa2bcbebf42cc1320028a6ca21b286b6a2b7e30b134f2c58d955714c8fdb6",
           "@75ed156328bd2ae0cd261fa91327426d8bdee798a5672b0d7643a973ba9f7f8b")
