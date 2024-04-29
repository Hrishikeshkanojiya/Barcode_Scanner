# Barcode Reader POC Documentation

## Introduction
This Python code serves as a Proof of Concept (POC) for reading and decoding barcodes from images. It utilizes the OpenCV library for image processing and the Pyzbar library for decoding the barcode.

## Requirements
- Python >=3.8
- OpenCV (`cv2`) library
- Pyzbar (`pyzbar`) library

## Usage
1. Open a terminal with the Barcode Scanner directory.

2. Use the following command to run the code:
    ```terminal
    python api.py
    ```

3. Finally, click on the link provided in the terminal for the UI.
    
## Functionality
1. **Reading the Image:**
   - The function reads the image file specified by the user using OpenCV's `cv2.imread` function.

2. **Decoding the Barcode:**
   - It decodes the barcode(s) present in the image using the `decode` function from Pyzbar library.
   - If no barcode is detected or if the barcode is blank/corrupted, it prints an appropriate message.

3. **Processing Detected Barcodes:**
   - For each detected barcode, it extracts its data and position within the image.
   - It highlights the detected barcode on the image by drawing a rectangle around it using OpenCV's `cv2.rectangle` function.

4. **Displaying the Results:**
   - It prints the decoded data and type of each barcode.
   - If the barcode data starts with zero, it removes the leading zero and identifies it as a UPC-A type barcode.
   - It displays the image with detected barcodes and highlighted rectangles using OpenCV's `cv2.imshow` function.
   - The image window remains open until a key is pressed, after which it is closed using `cv2.destroyAllWindows`.

## Note
   - Ensure that the required libraries (`cv2` and `pyzbar`) are installed in your Python environment before running the code.
   - Provide the correct path to the image file that contains the barcode(s) you want to decode.

## Example
   ```python
   image_path = "example_image.jpg"
   BarcodeReader(image_path)
   ```
   
## Output
   - The decoded barcode data and type will be printed in the console.
   - The image window will display the original image with detected barcodes highlighted.

## Limitations
   - If a 13 digit barcode starts with a zero, the number will be detected as a 12 digit code.
   - If a EAN-8 or UPC-E barcode is detected, it will be converted to a EAN-13 type.

## References
   - OpenCV documentation
   - Pyzbar documentation