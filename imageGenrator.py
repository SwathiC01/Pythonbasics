import requests
import os
from typing import Union

def get_extension(image_url: str) -> Union[str, None]:
    extensions: list[str] = ['.png', '.jpeg', '.jpg', '.gif', '.svg']
    for ext in extensions:
        if ext in image_url:
            return ext
        
def download_image(image_url: str, name: str, folder: str = None):
    ext=get_extension(image_url)
    if ext:
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception('Image extension could not be founded..')
    
    # Check if name already exists
    if os.path.isfile(image_name):
        raise Exception('File name already exists...')
        
    # Download image
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: "{image_name}" successfully')

    except Exception as e:
        print(f'Error {e}')

if __name__ == '__main__':
    image_url: str = input("Enter the url: ")
    image_name: str = input("Enter the image name: ")

    print("Downloading....")
    download_image(image_url, name=image_name, folder='images')




