from lsvalidate.models import LsRecord

# def createLsRecord(current_file):

#     file_lines = current_file.read().decode().splitlines()

#     for line in file_lines:
#         line_result = line.split('=')
#         print(line_result)
#         if len(line_result) < 2:
#             break
#         record = LsRecord()
#         record.account_number = line_result[1]
#         record.account_number_rng = line_result[0]
#         record.save()

#         # прерываем цикл, если строка пустая
#         if not line:
#             break

#     return {
#             "status": 0
#         }