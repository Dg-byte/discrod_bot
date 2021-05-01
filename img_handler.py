

  
import os, requests, glob
from PIL import Image


imgs = {
    "vs_bg": "./img/vs_bg.png",
    "vs_bg_animated": "./img/vs_bg_animated/frame_*.jpg",
}

#os.path.join(Путь относительно main.py)

async def vs_create(url1: str, url2: str):
    #Основа vs_screen
    vs_bg = Image.open(os.path.join(imgs["vs_bg"]))

    #Размер аватаров
    size = (150, 150)

    #Скачиваем аватары по url 
    fighter1 = Image.open(requests.get(url1, stream=True).raw).resize(size)
    fighter2 = Image.open(requests.get(url2, stream=True).raw).resize(size)

    #Определяем позицию для аватаров
    pos1 = (vs_bg.width//2 - fighter1.width*2, vs_bg.height//2 - fighter1.height//2)
    pos2 = (vs_bg.width//2 + fighter2.width, vs_bg.height//2 - fighter2.height//2)

    #Вставляем аватары в vs_screen
    vs_bg.paste(fighter1, pos1)
    vs_bg.paste(fighter2, pos2)

        #Сохранили изображение result.png
    vs_bg.save(os.path.join("./img", "result.png"))
    #return vs_bg

#vs_create("1","2")

async def vs_create_animated(url1:str, url2:str):

    # bg_size = (1344, 756)
    # .resize(bg_size)
    vs_bg, *img = [Image.open(path) for path in glob.glob(imgs["vs_bg_animated"])]

    size = (150, 150)

    fighter1 = Image.open(requests.get(url1, stream = True).raw).resize(size)
    fighter2 = Image.open(requests.get(url2, stream = True).raw).resize(size)

    pos1 = ((vs_bg.width//2 - fighter1.width*2)+60, (vs_bg.height//2 - fighter1.height//2)-50)
    pos2 = ((vs_bg.width//2 + fighter2.width)-60, (vs_bg.height//2 - fighter1.height//2)+50)

    vs_bg.paste(fighter1, pos1)
    vs_bg.paste(fighter2, pos2)

    for im in img:
        im.paste(fighter1, pos1)
        im.paste(fighter2, pos2)


    vs_bg.save(fp=os.path.join("./img", "result.gif"), append_images=img, save_all=True, duration=20, loop=0)
