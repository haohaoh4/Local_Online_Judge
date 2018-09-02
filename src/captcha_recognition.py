import os
import urllib
import time
from PIL import Image


def downloads_pic(begin_id, end_id):
    i = begin_id
    url = 'http://www.luogu.org/download/captcha'
    pic_path = "F:\Local_Online_Judge\Captcha_tmp\pic%s.png"
    while i <= end_id:
        i = i + 1
        urllib.request.urlretrieve(url, filename=(pic_path % i))
        time.sleep(0.5)


def get_pics():
    i = 1
    pic_path = "F:\Local_Online_Judge\Captcha_tmp\\"
    image_array = []
    image_label = []
    file_list = os.listdir(pic_path)
    for file in file_list:
        image = Image.open(pic_path + file)  # 打开图片
        file_name = file.split(".")[0]  # 获取文件名，此为图片标签
        image_array.append(image)
        image_label.append(file_name)
        print(pic_path + file.split(".")[0])
        i = i + 1
    return image_array, image_label


def output(image_list, image_n):
    place = "F:\Local_Online_Judge\Captcha_out\\"
    i = 0
    for p in image_list:
        p = process(p)  # no need to return,it's a reference
        split_into_char(p)
        print(place + image_n[i] + ".png")
        p.save(place + "pic" + image_n[i] + ".png")
        i = i + 1


def process(image_arry):
    image = image_arry.convert('L')
    threshold_grey = 218
    image = image.convert('L')  # 转换为灰度图像，即RGB通道从3变为1
    im2 = Image.new("L", image.size, 255)
    for y in range(image.size[1]):  # 遍历所有像素，将灰度超过阈值的像素转变为255（白）
        for x in range(image.size[0]):
            pix = image.getpixel((x, y))
            if int(pix) > threshold_grey:  # 灰度阈值
                im2.putpixel((x, y), 255)
            else:
                im2.putpixel((x, y), 0)
    return im2


def split_into_char(p):
    pixels = []
    for x in range(p.size[0]):
        tmp = []
        for y in range(p.size[1]):
            tmp.append(p.getpixel((x, y)))
        pixels.append(tmp)
    for x in range(1, p.size[0]-1):
        for y in range(1, p.size[1]-1):
            if pixels[x][y]==0:
                if pixels[x-1][y]==255 and pixels[x+1][y]==255 and pixels[x][y+1]==255 and pixels[x][y-1]==255:
                    p.putpixel((x, y), 255)
            #if pixels[x][y]==255:
            #    if pixels[x-1][y]==0 and pixels[x+1][y]==0 and pixels[x][y+1]==0 and pixels[x][y-1]==0:
            #        p.putpixel((x, y), 0)
    print(pixels)


images, image_l = get_pics()
output(images, image_l)
