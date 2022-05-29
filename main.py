import requests
import shutil
from lxml import html
from os import path
from tkinter import *
from tkinter.filedialog import askdirectory
from functools import partial


def download(search_key: StringVar, directory: StringVar, images_number: StringVar):
    search_key = "+".join(search_key.get().split(" "))
    directory = directory.get()
    images_number = int(images_number.get())

    if len(search_key) == 0 or not path.isdir(directory):
        return

    print(f"Keyword : {search_key}, Directory : {directory}, Images number : {images_number}")

    response = requests.get(
        "https://www.google.fr/search?q=" + search_key + "&tbm=isch&ved=2ahUKEwiw_-zyzfLsAhVNYBoKHZa5CJUQ2-cCegQIABAA&oq=dog&gs_lcp=CgNpbWcQA1AAWABgoxhoAHAAeACAAQCIAQCSAQCYAQCqAQtnd3Mtd2l6LWltZw&sclient=img&ei=4ranX7CGJc3AaZbzoqgJ&bih=610&biw=1280")
    tree = html.fromstring(response.content)
    url_list = list(map(lambda x: x.get("src"), tree.xpath("//img")))
    for i in range(1, min([len(url_list), images_number + 1])):
        image_url = url_list[i]
        filename = path.join(directory, r"image_" + search_key + str(i) + ".jpg")

        r = requests.get(image_url, stream=True)

        if r.status_code == 200:
            r.raw.decode_content = True
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

            print('Image sucessfully Downloaded: ', filename)
        else:
            print('Image Couldn\'t be retreived')
