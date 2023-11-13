import os
import shutil
from django.conf import settings

def move_files(folders):
    # print(folders)

    for folder in folders:

        folder_from = folder
        ls = folder.split('\\')[-1]
        print(ls)

        folder_to = os.path.join(settings.SHARED_DIR, ls)
        print('folder from')
        print(folder_from)
        print('folder to')
        print(folder_to)

        if not os.path.exists(folder_to):
            os.mkdir(folder_to)

        for f in os.listdir(folder_from):
                if os.path.isfile(os.path.join(folder_from, f)):
                    shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
                if os.path.isdir(os.path.join(folder_from, f)):
                    shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))
