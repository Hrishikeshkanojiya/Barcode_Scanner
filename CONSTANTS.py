import os

from flask import Flask

app = Flask(__name__)
# Define the upload folder and allowed extensions for uploaded files
UPLOAD_FOLDER = 'static/images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
STATIC_EMAIL = 'user@example.com'
STATIC_PASSWORD = 'Pass@123'
