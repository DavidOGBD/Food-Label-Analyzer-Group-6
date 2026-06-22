import re


def validate_barcode(barcode):

    pattern = r"^\d{8,13}$"

    return bool(re.match(pattern, barcode))
