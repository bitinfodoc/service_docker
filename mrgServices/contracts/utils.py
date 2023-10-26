
import requests
import os
from main import settings

def upload_image(account_number, document_type, url):
    print(url)
    url = 'https://www.orenburgregiongaz.ru/sites/default/files/vdgo/14135100/oct-2008_0004.jpg'

    image_data = requests.get(url).content
    image_file_extension = url.split('/')[-1].split('.')[-1]
    print(image_file_extension)



    # image_path = '/' + account_number + '/'
    image_name = document_type +'_'+ account_number + '.' + image_file_extension

    image_dir_path =  os.path.join(settings.MEDIA_ROOT, 'vdgo', account_number)

    image_path = os.path.join(image_dir_path, image_name)

    print('upload is true')
    if not os.path.exists(image_dir_path) :
        os.mkdir(image_dir_path)

    with open(image_path, 'wb') as handler:
        handler.write(image_data)
    print('upload is true')
    return True