from main.celery import app
from contracts.models import ContractVdgo

@app.task
def createContractVdgoRecord(current_file_name):

    file = open(current_file_name, 'r')

    while True:
        line_result = file.readline().split('=')
        if len(line_result) < 3:
            break
        if not line_result:
            break
        try:
            records = ContractVdgo.objects.filter(account_number = line_result[0])
            print(line_result[0])
            print(line_result[1])
            print(line_result[2])

            if len(records) == 0:
                ContractVdgo(
                    account_number = str(line_result[0]).strip(),
                    account_number_rng = str(line_result[1]).strip(),
                    account_address = str(line_result[2])
                ).save()
            else:
                print('already exist')
        except:
            file.close
            print("Can't write Contract VDGO Record")
            pass

    file.close