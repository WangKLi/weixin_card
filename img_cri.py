from PIL import Image
ima = Image.open("./img/@69111985642e59bbabd61ec152b5517fb4f52a2c5e11c81da00c128ae826d9a1.jpg").convert("RGBA")
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

imb.save("./test_circle.png")
