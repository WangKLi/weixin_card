from PIL import Image

for i in range(7):
    print(i)
    base_img = Image.open(f'./templates/template_{i}.jpg')
    base_img = base_img.resize((500, 700))
    # base_img = base_img.crop((0, 0, 540, 940))
    base_img.save(f'./templates/template_{i}.jpg')