
import requests
import os
from main import settings
from contracts.models import ContractVdgo

def createContractVdgoRecord(current_file_name):

    file = open(current_file_name, 'r')

    while True:
        line_result = file.readline().split('=')
        # print(line_result)
        # break
        if len(line_result) < 3:
            break
        if not line_result:
            break

        try:
            records = ContractVdgo.objects.filter(account_number = line_result[0])
            # print(records.values())

            if len(records) == 0:
                ContractVdgo(
                    account_number = str(line_result[0]).strip(),
                    account_number_rng = str(line_result[1]).strip(),
                    account_address = str(line_result[2]).strip()
                ).save()
            else:
                print('already exist')
        except:
            file.close
            print("Can't write LsRecord")
            pass

    file.close