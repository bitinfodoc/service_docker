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

def makeContactsFileCSV(values):
# ------------------------------------------------------------------------
    print('------------------------------------------------------')
    print(values)
    date=datetime.now().strftime("%Y%m%d")

    if not os.path.exists(PROJECT_PATH+'/files/contacts'):
        os.makedirs(PROJECT_PATH+'/files/contacts')

    filename = PROJECT_PATH+'/files/contacts/CONT'+date+'.csv'

    if os.path.exists(filename):
        ts = datetime.now().timestamp()
        new_filename = PROJECT_PATH+'/files/contacts/CONT'+date+'_'+str(ts)+'.csv'
        os.rename(filename, new_filename)

    with open(filename, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['ls', 'email', 'phone', 'date'])

        for row in values:
            print('-------------------------------------------------------')
            print(row)
            date = datetime.date(row['dat_write']).strftime("%d.%m.%Y")
            filewriter.writerow([row['ls'],  row['email'], row['phone'], date])

    return filename

def makeContactsFileDBF(values):
# ------------------------------------------------------------------------
    print('------------------------------------------------------')
    print(values)
    date=datetime.now().strftime("%Y%m%d")

    if not os.path.exists(PROJECT_PATH+'/files/contacts'):
        os.makedirs(PROJECT_PATH+'/files/contacts')

    filename = PROJECT_PATH+'/files/contacts/CONT'+date+'.dbf'

    if os.path.exists(filename):
        ts = datetime.now().timestamp()
        new_filename = PROJECT_PATH+'/files/contacts/CONT'+date+'_'+str(ts)+'.dbf'
        os.rename(filename, new_filename)

    table = dbf.Table(filename,
                      'ls N(12,0); mail C(100); dat_time C(30); phone C(30); ',
                    #   'ls N(12,0); pok N(7,0); tel C(30)',
                      codepage='utf8'
                      )

    table.open(dbf.READ_WRITE)

    for row in values:
        print('-------------------------------------------------------')
        print(row)
        # datum = (int(row['ls']), int(row['pok']), str(row['dat_write']), str(row['tel']))
        date = datetime.date(row['dat_write']).strftime("%d.%m.%Y")

        datum = (row['ls'], row['email'], date, row['phone'])
        table.append(datum)
    table.close()
# -------------------------------------------------------------------------
    return filename

def getContactsFromSite():

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
            sql = "Select ls, email, dat_write, phone from mmrg_collecting_contacts WHERE dat_unload IS NULL AND unload IS NULL"
            # sql = "Select ls, pok, dat_write, tel from mmrg_datametr WHERE dat_write between '2022-03-21 10:13:00' and '2022-03-25 10:00:00'"

            cursor.execute(sql)
            print ("cursor.description: ", cursor.description)
            # print (cursor.fetchall())

            filename = makeContactsFileCSV(cursor.fetchall())

            # внесение изменений в базу
            if settings.DEBUG == False:
                date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                update_query = "UPDATE mmrg_collecting_contacts SET unload = 1, dat_unload = %s WHERE dat_unload is null AND unload is null"
                cursor.execute(update_query, (date))

            connection.commit()
    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print ("commit successful!!")

    return filename