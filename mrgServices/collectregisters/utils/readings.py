import os
import dbf
import requests
import json

from datetime import datetime
from django.core.mail import send_mail, EmailMessage
import pymysql.cursors
from django.conf import settings


PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

def makeReadingsFile(values):
# ------------------------------------------------------------------------
    date=datetime.now().strftime("%Y%m%d")
    # date = "20230816"

    if not os.path.exists(PROJECT_PATH+'/files/readings'):
        os.makedirs(PROJECT_PATH+'/files/readings')
    filename = PROJECT_PATH+'/files/readings/POK'+date+'.dbf'
    if os.path.exists(filename):
        ts = datetime.now().timestamp()
        new_filename = PROJECT_PATH+'/files/readings/POK'+date+'_'+str(ts)+'.dbf'
        os.rename(filename, new_filename)

    table = dbf.Table(filename,
                      'ls N(12,0); pok N(7,0); dat_time C(30); tel C(30)',
                    #   'ls N(12,0); pok N(7,0); tel C(30)',
                      codepage='utf8'
                      )
    table.open(dbf.READ_WRITE)

    for row in values:
        # datum = (int(row['ls']), int(row['pok']), str(row['dat_write']), str(row['tel']))
        date = datetime.date(row['dat_write']).strftime("%d.%m.%Y")

        datum = (row['ls'], row['pok'], date, row['tel'])
        table.append(datum)
    table.close()
# -------------------------------------------------------------------------
    return filename


def getReadingsFromSite():

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
            sql = "Select ls, pok, dat_write, tel from mmrg_datametr WHERE dat_unload is null AND unload = 0"
            # sql = "Select ls, pok, dat_write, tel from mmrg_datametr WHERE dat_write between '2022-08-16 00:00:01' and '2022-08-17 00:00:01'"

            cursor.execute(sql)
            print ("cursor.description: ", cursor.description)

            filename = makeReadingsFile(cursor.fetchall())

            # внесение изменений в базу
            if settings.DEBUG == False:
                date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                update_query = "UPDATE mmrg_datametr SET unload = 1, dat_unload = %s WHERE dat_unload is null AND unload = 0"
                cursor.execute(update_query, (date))

            connection.commit()
    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print ("commit successful!!")

    return filename