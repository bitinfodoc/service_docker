from main.celery import app
from contracts.models import ContractVdgo
import os
from django.conf import settings
from datetime import datetime

@app.task
def create_contract_record(file_lines_array):

    for line in file_lines_array:
        # line_result = current_file_name.readline().split('=')

        line_result = line.split('=')
        # i = i + 1
        print(line_result)

        if len(line_result) < 3:
            pass

        # if not line_result:
        #     break

        try:
            records = ContractVdgo.objects.filter(account_number = line_result[0])
            print(line_result[0])
            print(line_result[1])
            print(line_result[2])
            print(line_result[3])

            if len(records) == 0:
                ContractVdgo(
                    account_number = str(line_result[0]),
                    account_number_rng = str(line_result[1]),
                    account_address = str(line_result[2]),
                    is_izs = str(line_result[3]),
                    last_update_date = datetime.now()
                ).save()
            else:
                records.update(
                    account_number = str(line_result[0]),
                    account_number_rng = str(line_result[1]),
                    account_address = str(line_result[2]),
                    is_izs = str(line_result[3]),
                    last_update_date = datetime.now()
                )

                print('already exist')
        except:
            # file.close
            print("Can't write Contract VDGO Record")
            pass
    # return True
    # file.close