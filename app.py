import os
import random
from flask import Flask, send_from_directory, make_response

app = Flask(__name__)

# Replace 'images' with the path to your folder containing random images
IMAGES_FOLDER = 'images'

# Get a list of all image files in the 'images' folder
image_files = [file for file in os.listdir(IMAGES_FOLDER) if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

@app.route('/random-image')
def random_image():
    # Pick a random image from the list of files
    random_image_file = random.choice(image_files)
    image_path = os.path.join(IMAGES_FOLDER, random_image_file)

    # Open the image file and read the image data
    with open(image_path, 'rb') as file:
        image_data = file.read()

    # Create a Flask response with the image data
    response = make_response(image_data)
    response.headers.set('Content-Type', 'image/jpeg')  # Adjust the Content-Type as needed (e.g., image/png for PNG images)

    return response

if __name__ == '__main__':
    app.run(debug=True)
