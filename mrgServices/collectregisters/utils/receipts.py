import os
import dbf
import requests
import json
import csv
# import numpy as np

from datetime import datetime
from django.core.mail import send_mail, EmailMessage
import pymysql.cursors
from django.conf import settings


PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))


def createFileCSV(folder, dataType):
    date=datetime.now().strftime("%Y%m%d")
    if not os.path.exists(PROJECT_PATH+'/files/'+str(folder)+''):
        os.makedirs(PROJECT_PATH+'/files/'+str(folder)+'')
    filename = PROJECT_PATH+'/files/receipts/'+str(dataType)+date+'.csv'
    if os.path.exists(filename):
        ts = datetime.now().timestamp()
        new_filename = PROJECT_PATH+'/files/receipts/'+str(dataType)+date+'_'+str(ts)+'.csv'
        os.rename(filename, new_filename)
    return filename



def makeReceiptsFileCSV(values):

    filename = createFileCSV('receipts', 'ZDE')

    with open(filename, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['ls', 'email', 'dat_write', 'pr_paper'])
        for row in values:
            if 'pr_paper' in row:
                pass
            else:
                row['pr_paper'] = '0'
            filewriter.writerow([str(row['ls']).strip(), str(row['email']).strip(), str(row['dat_write']).strip(), str(row['pr_paper']).strip()])
    return filename

def getReceiptsFromSite():

    connection = pymysql.connect(
        host=settings.SITE_BASE_HOST,
        user=settings.SITE_BASE_USER,
        password=settings.SITE_BASE_PASSWORD,
        db=settings.SITE_BASE_DB,
        charset=settings.SITE_BASE_CHARSET,
        cursorclass=pymysql.cursors.DictCursor
        )

    print(connection)
    try:

        print ("connect successful!!")

        with connection.cursor() as cursor:
            # SQL
            cursor.execute("Select ls, email, dat_write, pr_paper from mmrg_dostavka_kvit WHERE dat_unload IS NULL AND unload = 0")
            first_part = cursor.fetchall()

            cursor.execute("Select ls, email, dat_write from mmrg_collecting_contacts WHERE unload_receipt IS NULL AND receipt_email = 1")
            second_part = cursor.fetchall()

            all_data = tuple(first_part) + tuple(second_part)
            filename = makeReceiptsFileCSV(all_data)

            # внесение изменений в базу
            if settings.DEBUG == False:
                date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                update_query = "UPDATE mmrg_dostavka_kvit SET unload = 1, dat_unload = %s WHERE dat_unload IS NULL AND unload = 0"
                cursor.execute(update_query, (date))
                connection.commit()

                update_query = "UPDATE mmrg_collecting_contacts SET unload_receipt = 1 WHERE unload_receipt = 0"
                cursor.execute(update_query, (date))
                connection.commit()


    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print ("commit successful!!")

    return filename