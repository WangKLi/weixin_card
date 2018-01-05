from PIL import Image


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
    base_img = Image.open('./templates/template_1.jpg')
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
    # base_img.show() # 查看合成的图片
    base_img.save(f'./head_img/{to_user}.jpg')  # 保存图片