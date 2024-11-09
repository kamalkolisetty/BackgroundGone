import os
from flask import Flask, render_template, request
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)  # Use default template folder

# Set a maximum file size (e.g., 16MB)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max 16MB file

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return render_template('error.html', error_message="No file part. Please upload an image.")

    file = request.files['file']
    
    if file.filename == '':
        return render_template('error.html', error_message="No selected file. Please choose an image to upload.")

    if not allowed_file(file.filename):
        return render_template('error.html', error_message="Invalid file type. Only PNG, JPG, and JPEG are allowed.")

    download_format = request.form.get('format', 'PNG').upper()  # Get the format (default to PNG)
    
    try:
        # Define the static folder for processed images
        static_folder = os.path.join(app.root_path, 'static', 'images')
        if not os.path.exists(static_folder):
            os.makedirs(static_folder)  # Create the folder if it doesn't exist

        # Process the image to remove background
        output_data = remove(file.read())
        output_image = Image.open(io.BytesIO(output_data)).convert("RGBA")

        # Determine the output file path and format
        if download_format == "JPEG":
            output_image = output_image.convert("RGB")  # JPEG does not support alpha (transparency)
            output_path = os.path.join(static_folder, 'output_image.jpeg')
            output_image.save(output_path, "JPEG")
        else:
            output_path = os.path.join(static_folder, 'output_image.png')
            output_image.save(output_path, "PNG")

        # Return the image path to be displayed and downloaded
        return render_template('index.html', image_url=f"/static/images/{os.path.basename(output_path)}")

    except Exception as e:
        print(f"Error processing image: {e}")
        return render_template('error.html', error_message=f"Error: {e}. Please try again later.")

if __name__ == '__main__':
    app.run(debug=True)
