import re


def validate_barcode(barcode):
    return bool(re.match(r"^\d{8,13}$", barcode))


