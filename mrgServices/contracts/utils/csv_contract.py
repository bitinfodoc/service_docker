import csv
import os
from django.conf import settings

def csv_contract(item):
    try:
        file_mame = item.account_number + '.txt'
        folder_path = os.path.join(settings.MEDIA_ROOT,'vdgo', item.account_number)
        file_path = os.path.join(folder_path, file_mame)

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        with open(file_path, 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                item.account_number,
                item.passport_name,
                item.account_address,
                item.passport_serial,
                item.passport_number,
                item.passport_issued_date,
                item.passport_issued,
                item.passport_issued_code,
                item.snils_number,
                item.passport_birth_date,
                item.passport_place,
                item.email,
                item.phone,
                item.inn_number,
            ])

        return folder_path
    except:
        return "error"