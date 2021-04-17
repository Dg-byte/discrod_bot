

import os
from PIL import Image
import requests

imgs = {
    "vs_bg": "./img/vs_bg.png",
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
    return vs_bg

#vs_create("1","2")

