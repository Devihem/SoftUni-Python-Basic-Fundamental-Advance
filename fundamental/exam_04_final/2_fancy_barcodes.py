import re
barcode_numbers = int(input())
barcode_pattern = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"
digits_extract_pattern = r"\d+"

for barcode in range(barcode_numbers):
    barcode_string = input()
    valid_barcodes = re.findall(barcode_pattern, barcode_string)
    if valid_barcodes:
        product_group = ""
        digits_match = re.findall(digits_extract_pattern, str(valid_barcodes))
        if digits_match:
            print(f"Product group: {''.join(digits_match)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
