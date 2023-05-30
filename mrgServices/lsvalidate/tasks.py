import json
# import requests

from main.celery import app
from lsvalidate.models import LsRecord
from lsvalidate.utils import createLsRecord

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
    createLsRecord('/app/reestrs/els_delta.txt')