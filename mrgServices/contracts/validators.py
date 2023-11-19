import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):

    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', 'bmp']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate_account_number(value):
    if (len(value) == 8 or len(value) == 12) and value.isdigit() == True:
        return {"result": True}
    else:
        return {"result": False}