from lsvalidate.models import LsRecord

def createLsRecord(current_file_name):

    file = open(current_file_name, 'r')

    while True:
        line_result = file.readline().split('=')
        if len(line_result) < 2:
            break
        if not line_result:
            break
        try:
            records = LsRecord.objects.filter(account_number_rng = line_result[0])
            # print(records.values())

            if len(records) == 0:
                LsRecord(
                    account_number = str(line_result[1]).strip(),
                    account_number_rng = str(line_result[0]).strip()
                ).save()
            else:
                print('already exist')
        except:
            file.close
            print("Can't write LsRecord")
            pass

    file.close
