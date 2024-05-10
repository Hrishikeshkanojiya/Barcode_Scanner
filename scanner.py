import cv2
import numpy as np
from pyzbar import pyzbar

from logger import setup_logger
from processing import process_barcode

logger = setup_logger()


def BarcodeReader(image):
    # read the image in numpy array using cv2
    img = cv2.imread(image)
    barcode_output = []

    # Decode the barcode image
    detectedBarcodes = pyzbar.decode(img)

    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (1, 21)))

    dens = np.sum(img, axis=0)

    thresh = closed.copy()
    for idx, val in enumerate(dens):
        if (val < 10800).all():
            thresh[:, idx] = 0

    (_, thresh2) = cv2.threshold(thresh, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Decode the barcode image
    undetectedBarcodes = pyzbar.decode(thresh2)

    # If no barcodes detected, print a warning message
    if not detectedBarcodes and not undetectedBarcodes:
        logger.warning("No barcodes detected or your barcode is blank/corrupted!")
    elif not detectedBarcodes:
        # Traverse through all the undetected barcodes in image
        for barcode in undetectedBarcodes:
            process_barcode(barcode, img, barcode_output)
    elif not undetectedBarcodes:
        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:
            process_barcode(barcode, img, barcode_output)
    else:
        # Traverse through all the detected barcodes in image
        for barcode in undetectedBarcodes:
            process_barcode(barcode, img, barcode_output)

    return img, barcode_output
