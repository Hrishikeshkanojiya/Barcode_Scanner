from flask import Flask, render_template, request,jsonify, redirect, url_for
from werkzeug.utils import secure_filename
from pyzbar import pyzbar
import cv2

app = Flask(__name__)

# Define the upload folder and allowed extensions for uploaded files
UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def BarcodeReader(image):
    # read the image in numpy array using cv2
    img = cv2.imread(image)
    barcode_output = []

    # Decode the barcode image
    detectedBarcodes = pyzbar.decode(img)

    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:

        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:

            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect

            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x - 10, y - 10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)

            if barcode.data != b"":
                # Convert bytes to string
                barcode_data = barcode.data.decode("utf-8")

                # Check if the barcode data starts with zero
                if barcode_data.startswith("0"):
                    # Remove the first zero if it exists
                    barcode_data = barcode_data[1:]
                    print("Data:", barcode_data)
                    print("Type:", "UPC-A")
                    barcode_output.append(barcode_data)
                else:
                    # If no zero at the beginning, print without changes
                    print("Data:", barcode_data)
                    print("Type:", barcode.type)
                    barcode_output.append(barcode_data)
        return barcode_output



# # Route to upload an image and detect barcodes
# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # Check if the post request has the file part
#         if 'file' not in request.files:
#             return render_template('index.html', message='No file part')
#
#         file = request.files['file']
#
#         # If the user does not select a file, the browser submits an empty file without a filename
#         if file.filename == '':
#             return render_template('index.html', message='No selected file')
#
#         # If the file exists and has an allowed extension
#         if file and allowed_file(file.filename):
#             # Save the uploaded file to the upload folder
#             filename = secure_filename(file.filename)
#             filepath = f"{app.config['UPLOAD_FOLDER']}/{filename}"
#             file.save(filepath)
#
#             # Detect barcodes in the uploaded image
#             barcode_data = BarcodeReader(filepath)
#             print(barcode_data)
#             # Render the template with the uploaded image and barcode data
#             return render_template('index.html', image_file=filename, barcode_data=barcode_data)

    # Render the initial upload form
    # return render_template('index.html')


STATIC_EMAIL = 'user@example.com'
STATIC_PASSWORD = 'password'


# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get email and password from the form
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if email and password match the static values
        if email == STATIC_EMAIL and password == STATIC_PASSWORD:
            # Redirect to the barcode detection page upon successful login
            return redirect(url_for('barcode_detection'))

    # Render the login page template
    return render_template('login.html')


# Route for the barcode detection page
@app.route('/barcode_detection', methods=['GET', 'POST'])
def barcode_detection():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return render_template('index.html', message='No selected file')

        # If the file exists and has an allowed extension
        if file and allowed_file(file.filename):
            # Save the uploaded file to the upload folder
            filename = secure_filename(file.filename)
            filepath = f"{app.config['UPLOAD_FOLDER']}/{filename}"
            file.save(filepath)

            # Detect barcodes in the uploaded image
            barcode_data = BarcodeReader(filepath)
            print(barcode_data)
            # Render the barcode detection page with the uploaded image and barcode data
            return render_template('index.html', image_file=filename, barcode_data=barcode_data)

    # Render the barcode detection page template
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)



