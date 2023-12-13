import os
import shutil
from django.conf import settings
from smb.SMBConnection import SMBConnection

def move_files(account_number):

    print(settings.SMB_USER)

    conn = SMBConnection(
        settings.SMB_USER,
        settings.SMB_PASS,
        settings.SMB_GROUP,
        settings.SMB_REMOTE_NAME,
        domain=settings.SMB_DOMAIN,
        use_ntlm_v2=True,
        sign_options=SMBConnection.SIGN_WHEN_SUPPORTED,
        is_direct_tcp=True
    )

    conn.connect(settings.SMB_SHARE_IP, 445)

    # проверяем существоанаие дирректори, если нет добавляем
    filelist = conn.listPath('Reestrs', '/vdgo/')
    files_array = []
    for file in filelist:
        files_array.append(file.filename)
        print(file.filename)
    remote_folder = 'vdgo/Сайт_'+ account_number + '/'
    if str('Сайт_'+account_number) not in files_array: conn.createDirectory('Reestrs', remote_folder)

    surce_folder = os.path.join(settings.MEDIA_ROOT,'vdgo', account_number)
    surce_files = os.listdir(surce_folder)

    for file in surce_files:
        source_file_path = os.path.join(surce_folder, file)
        source_file = open(source_file_path, 'rb')

        remote_file_path = remote_folder+file

        conn.storeFile('Reestrs', remote_file_path, source_file)
        source_file.close()
    conn.disconnect()
    return "Success"
