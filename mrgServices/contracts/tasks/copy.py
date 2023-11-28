from main.celery import app
from contracts.models import ContractVdgo
from contracts.utils import csv_contract, move_files

@app.task
def copy_to_network():
    unsended_contracts = ContractVdgo.objects.filter(consent = True, is_sended = False)

    print(unsended_contracts)

    for item in unsended_contracts:
        csv_res = csv_contract(item)
        print(csv_res)
        move_res = move_files(item.account_number)
        print(move_res)
        if move_res == "Success":
            item.is_sended = True
            item.save()
        else:
            item.error_text = "Can't copy files"
            item.is_error = True
            item.save()
