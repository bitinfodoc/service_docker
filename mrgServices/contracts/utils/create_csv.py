import csv
import os
from django.conf import settings


def remove_symbols(string = None):
    if string == None:
        return ""
    trans_table = {
        ord('(') : None,
        ord(')') : None,
        ord('-') : None,
        ord(',') : None,
        ord(':') : None,
        ord('.') : None,
        ord(' ') : None,
    }
    print('--- String is ' + string)
    print('string formated')

    return string.translate(trans_table)

def format_date(string = None):
    if string == None:
        return ""
    trans_table = {
        ord('-') : ord('.'),
    }
    print('--- Daste is ' + string)
    print('date formated')
    return string.translate(trans_table)

def csv_contract(item):
    try:
        file_mame = item.account_number + '.txt'

        vdgo_folder_path = os.path.join(settings.MEDIA_ROOT,'vdgo')
        if not os.path.exists(vdgo_folder_path):
            print('vdgo folder is not exist')
            os.mkdir(vdgo_folder_path)

        folder_path = os.path.join(vdgo_folder_path, item.account_number)
        file_path = os.path.join(folder_path, file_mame)

        if not os.path.exists(folder_path):
            print('ls folder is not exist')
            os.mkdir(folder_path)

        with open(file_path, 'w', encoding='UTF-8') as file:
            writer = csv.writer(file, delimiter = ";")
            writer.writerow([
                item.account_number,
                item.passport_name,
                item.account_address,
                item.passport_serial,
                item.passport_number,
                format_date(item.passport_issued_date),
                item.passport_issued,
                remove_symbols(item.passport_issued_code),
                remove_symbols(item.snils_number),
                format_date(item.passport_birth_date),
                item.passport_place,
                item.email,
                remove_symbols(item.phone),
                item.inn_number,
                int(item.sms),
            ])
        print('file is writed')
        return folder_path
    except:
        print('error')
        return "error"