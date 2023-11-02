from main.celery import app
from contracts.models import ContractVdgo
from contracts.utils import csv_contract, move_files

@app.task
def copy_to_network():
    unsended_contracts = ContractVdgo.objects.filter(consent = True, is_sended = False)

    print(unsended_contracts)
    items_folders = []
    for item in unsended_contracts:
        folder = csv_contract(item)
        # item.is_sended = True
        # item.save()
        if folder != "error":
            items_folders.append(folder)

    move_files(items_folders)
