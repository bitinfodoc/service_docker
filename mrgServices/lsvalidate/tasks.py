import json
# import requests

from main.celery import app
from lsvalidate.models import LsRecord

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
                LsRecord(account_number = line_result[1], account_number_rng = line_result[0]).save()
            else:
                print('already exist')
        except:
            print("Can't write LsRecord")
            pass

        # прерываем цикл, если строка пустая
        if not line:
            break