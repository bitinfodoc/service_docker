import pdfkit
from jinja2 import Environment, FileSystemLoader
import os
from django.conf import settings

def pdf_contract(contract):

    print(os.name)
    # if os.name == 'nt':


    print(contract.account_number)
    try:
        account_number = contract.account_number
        ls = [*str(contract.account_number)]
        template_data = {
            'ls': ls,
            'address': contract.account_address,
            'name': contract.passport_name,
            "passport_place": contract.passport_place,
            "passport_birth_date": contract.passport_birth_date,
            "passport_serial": contract.passport_serial,
            "passport_number": contract.passport_number,
            "passport_issued_date" : contract.passport_issued_date,
            "passport_issued" : contract.passport_issued,
            "passport_issued_code": contract.passport_issued_code,
            "passport_address_registration": contract.passport_address_registration,

            "snils_number": contract.snils_number,

            "phone": contract.phone,
            "email": contract.email,
            "confirm": contract.confirm,
            "consent": contract.consent,

            "sms": contract.sms,
        }

        print('template data created')
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("templates/template.html")

        pdf_template = template.render(template_data)


        options = {
            'page-size': 'A4',
            'margin-top': '0.25in',
            'margin-right': '0.25in',
            'margin-bottom': '0.25in',
            'margin-left': '0.25in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'no-outline': None
        }
        temp_folder_path = os.path.join(settings.MEDIA_ROOT,'tmp')

        if not os.path.exists(temp_folder_path):
            print('Temp folder is not exist')
            os.mkdir(temp_folder_path)
        print('account_number')
        print(account_number)
        file_mame = "unsigned_"+account_number+".pdf"

        file_path = os.path.join(temp_folder_path, file_mame)

        print(file_path)


        if os.name == 'nt':
            print("hello nt")
            path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
            res = pdfkit.from_string(pdf_template, file_path, options=options, configuration=config)
        # print(res)
        else:
            pdfkit.from_string(pdf_template, file_path, options=options)
        # result_file_path = os.path.join()

        return {"pdf_path": file_path, "pdf_name": file_mame, "error": False}

    except:
        return {"error": "cant create file PDF"}