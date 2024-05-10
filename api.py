import os
from flask import render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import cv2
import secrets
from CONSTANTS import ALLOWED_EXTENSIONS, STATIC_EMAIL, STATIC_PASSWORD, app
from logger import setup_logger
from scanner import BarcodeReader


logger = setup_logger()


def generate_secret_key():
    return secrets.token_hex(16)


# Set the secret key
app.secret_key = generate_secret_key()


# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get email and password from the form
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if email and password match the static values
        if email == STATIC_EMAIL and password == STATIC_PASSWORD:
            # Set the 'logged_in' session variable to True
            session['logged_in'] = True
            # Redirect to the barcode detection page upon successful login
            return redirect(url_for('barcode_detection'))

    # Render the login page template
    return render_template('login.html')


# Route for the barcode detection page
@app.route('/', methods=['GET', 'POST'])
def barcode_detection():
    # Check if the user is logged in (i.e., 'logged_in' session variable is True)
    # if not session.get('logged_in'):
    #     # If not logged in, redirect to the login page
    #     logger.warning(
    #         "Unsuccessful Login")
    #     return redirect(url_for('login'))

    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')

        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', message='No selected file')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            processed_img, barcode_data = BarcodeReader(filepath)

            # Resize the uploaded image to 250x250
            resized_img = cv2.resize(processed_img, (250, 250))
            processed_filename = f"processed_{filename}"
            processed_filepath = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
            cv2.imwrite(processed_filepath, resized_img)

            return render_template('index.html', processed_image_file=processed_filename, barcode_data=barcode_data)

    return render_template('index.html')


if __name__ == '__main__':
    # app.secret_key = generate_secret_key()
    app.run(debug=True)
