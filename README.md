# Barcode_Scanner

The EAN-13 to UPC-A code snippet is down below:


def ean13_to_upca(ean13):
    # Remove the leading digit (country code)
    ean12 = ean13[1:]
    # Calculate the checksum for UPC-A
    checksum = calculate_checksum(ean12)
    # Return the converted UPC-A barcode
    return ean12 + str(checksum)

def calculate_checksum(digits):
    # Calculate checksum for UPC-A
    odd_sum = sum(int(digits[i]) for i in range(0, len(digits), 2))
    even_sum = sum(int(digits[i]) * 3 for i in range(1, len(digits), 2))
    total_sum = odd_sum + even_sum
    remainder = total_sum % 10
    if remainder == 0:
        return 0
    else:
        return 10 - remainder
