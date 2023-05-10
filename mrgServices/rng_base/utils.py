from rng_base.models import RngBaseRecord
from io import BytesIO

def createRngBaseRecord(current_file):

    file_lines = current_file.read().decode().splitlines()

    for line in file_lines:
        line_result = line.split('|')
        if len(line_result) < 10:
            break
        meter = False
        if int(line_result[7]) == 1:
            meter = True
        record = RngBaseRecord()
        record.account_number = line_result[2]
        record.account_balance = line_result[6]
        record.service_type_code = line_result[3]
        record.meter = meter
        record.meter_readings = line_result[8]
        record.save()

        # прерываем цикл, если строка пустая
        if not line:
            break

    return {
            "status": 0
        }