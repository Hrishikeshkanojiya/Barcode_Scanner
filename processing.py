import cv2
from logger import setup_logger

logger = setup_logger()


def process_barcode(barcode, img, barcode_output):
    # Locate the barcode position in image
    (x, y, w, h) = barcode.rect

    # Put the rectangle in image to highlight the barcode
    cv2.rectangle(img, (x - 10, y - 10), (x + w + 10, y + h + 30), (255, 0, 0), 2)

    # Convert bytes to string
    barcode_data = barcode.data.decode("utf-8")

    # Check if the barcode data starts with zero
    if barcode_data.startswith("0"):
        # Remove the first zero if it exists
        barcode_data = barcode_data[1:]
        logger.info(f"Data: {barcode_data} Type: UPC-A")  # Log barcode data with type
        barcode_output.append(barcode_data)
    else:
        # If no zero at the beginning, print without changes
        logger.info(f"Data: {barcode_data} Type: {barcode.type}")  # Log barcode data with type
        barcode_output.append(barcode_data)
