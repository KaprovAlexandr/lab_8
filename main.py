def pr1():
    from PIL import Image
    filename = "123.jpg"
    with Image.open(filename) as img:
        img.show()
        img_crop = img.crop((0, 230, 1024, 1094))
        img_crop.save("img_postcard.jpg")
        img_crop.show()


def pr2():
    from PIL import Image
    sl = {'День рождения':'sdr.jpg', 'Новый год':'noviygod.jpg', 'Масленица':'maslenitsa.jpg', '23 Февраля':'23.jpg'}
    n = input('Введите название праздника:')
    img = Image.open(sl[n])
    img.show()

def pr3():
    from PIL import Image,ImageFont,ImageDraw
    filename = "123.jpg"
    with Image.open(filename) as img:
        img.show()
        img_crop = img.crop((0, 230, 1024, 1094))
        img_crop.save("img_postcard.jpg")
        img_crop.show()
        a = input("Введите имя пользователя, которого хотите поздравить: ")
        font = ImageFont.truetype("arial.ttf",25)
        drawer = ImageDraw.Draw(img_crop)
        drawer.text((400,50), str(a) + ',Поздравляю', font = font, fill = 'black')
        img_crop.save('new_img.jpg')
        img_crop.show()



