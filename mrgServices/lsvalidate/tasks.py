import json
import os
# import requests

from main.celery import app
from lsvalidate.models import LsRecord
from lsvalidate.utils import createLsRecord
from django.conf import settings
from smb.SMBConnection import SMBConnection


@app.task
def ls_upload( file_lines ):
    for line in file_lines:
        line_result = line.split('=')
        if len(line_result) < 2:
            break
        try:
            records = LsRecord.objects.filter(account_number_rng = line_result[0])
            print(records)
            if len(records) == 0:
                LsRecord(
                    account_number = str(line_result[1]).strip(),
                    account_number_rng = str(line_result[0]).strip()
                ).save()
            else:
                print('already exist')
        except:
            print("Can't write LsRecord")
            pass

        # прерываем цикл, если строка пустая
        if not line:
            break

@app.task
def auto_upload_delta():

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
    filelist = conn.listPath('Reestrs', '/ls_delta')

    for remote_file in filelist:
        # files_array.append(remote_file.filename)

        if remote_file.filename == '.' or remote_file.filename == '..':
            pass
        else:
            shared_file = '/ls_delta/' + remote_file.filename
            print('filename is')
            print(remote_file.filename)
            file_obj = os.path.join(settings.MEDIA_ROOT, 'els_delta_tmp.txt')

            with open(file_obj, 'wb') as fp:
                conn.retrieveFile('Reestrs', shared_file, fp, timeout=30)

            result = createLsRecord(file_obj)

            if result == True:
                conn.deleteFiles('Reestrs', shared_file)
