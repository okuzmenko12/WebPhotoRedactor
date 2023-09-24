# import cv2
#
# def remove_jpeg_artifacts(input_path, output_path):
#     # Загружаем изображение
#     img = cv2.imread(input_path)
#
#     # Применяем фильтр для сглаживания артефактов
#     denoised = cv2.fastNlMeansDenoisingColored(img, None, 4, 2, 7, 21)
#
#     # Сохраняем результат
#     cv2.imwrite(output_path, denoised)
#
# # Пример использования
# input_path = 'input.jpg'
# output_path = 'output.jpg'
# remove_jpeg_artifacts(input_path, output_path)


import requests

import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.picsart.io/tools/1.0/removebg"

files = {'image': open('input.png', 'rb')}

payload = {"format": "PNG"}

headers = {
    "accept": "application/json",
    "x-picsart-api-key": os.getenv('PICSART_KEY')
}

response = requests.post(url, data=payload, headers=headers, files=files)

print(response.json())
