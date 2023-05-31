import os
import dbf
import requests
import json
import csv

from datetime import datetime
from django.core.mail import send_mail, EmailMessage
import pymysql.cursors
from django.conf import settings


PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

def makeReceiptsFileCSV(values):
# ------------------------------------------------------------------------
    print('------------------------------------------------------')
    print(values)
    date=datetime.now().strftime("%Y%m%d")

    if not os.path.exists(PROJECT_PATH+'/files/receipts'):
        os.makedirs(PROJECT_PATH+'/files/receipts')

    filename = PROJECT_PATH+'/files/receipts/ZDE'+date+'.csv'

    if os.path.exists(filename):
        ts = datetime.now().timestamp()
        new_filename = PROJECT_PATH+'/files/receipts/ZDE'+date+'_'+str(ts)+'.csv'
        os.rename(filename, new_filename)

    with open(filename, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['ls', 'email', 'dat_write', 'pr_paper'])

        for row in values:
            print('-------------------------------------------------------')
            print(row)
            # date = datetime.date(row['dat_write']).strftime("%d.%m.%Y")
            filewriter.writerow([str(row['ls']).strip(),  str(row['email']).strip(), str(row['dat_write']).strip(), str(row['pr_paper']).strip()])

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
            # sql = "Select ls, email, dat_write, phone from mmrg_collecting_contacts"
            sql = "Select ls, email, dat_write, pr_paper from mmrg_dostavka_kvit WHERE dat_unload IS NULL AND unload = 0"
            # sql = "Select ls, pok, dat_write, tel from mmrg_datametr WHERE dat_write between '2022-03-21 10:13:00' and '2022-03-25 10:00:00'"

            cursor.execute(sql)
            print ("cursor.description: ", cursor.description)
            # print (cursor.fetchall())

            filename = makeReceiptsFileCSV(cursor.fetchall())

            # внесение изменений в базу
            if settings.DEBUG == False:
                date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                update_query = "UPDATE mmrg_dostavka_kvit SET unload = 1, dat_unload = %s WHERE dat_unload IS NULL AND unload = 0"
                cursor.execute(update_query, (date))

            connection.commit()
    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print ("commit successful!!")

    return filename