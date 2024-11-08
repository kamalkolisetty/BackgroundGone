
# Image Background Remover

This project provides a simple web application to remove the background from images using machine learning. The user uploads an image, and the app processes it, removing the background and providing the processed image for download.

## Features

- Upload an image in formats like PNG, JPEG, etc.
- Removes the background of the uploaded image.
- Displays the processed image on the same page.
- Provides an option to download the processed image (PNG).

## Technologies Used

- **Flask**: Lightweight web framework for Python to handle HTTP requests.
- **rembg**: Python library for removing image backgrounds using machine learning.
- **Pillow (PIL)**: Python Imaging Library to handle image manipulations.
- **Bootstrap**: Frontend framework for a responsive and user-friendly UI.

## Setup and Installation

### Prerequisites

Ensure that you have Python 3.7+ installed on your machine.

### 1. Clone the repository

```bash
git clone https://github.com/kamalkolisetty/BackgroundGone.git
```

### 2. Navigate to the project directory

```bash
cd BackgroundGone
```

### 3. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On MacOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## How to Use

1. Go to the main page (the root URL).
2. Click on "Choose Image to Upload" and select an image from your device.
3. Once the image is uploaded, the background will be automatically removed.
4. The processed image will be displayed below. You can then download it by clicking the "Download Image" button.

## Error Handling

If no file is uploaded or if the uploaded file is invalid, a user-friendly error message will be displayed.

## Future Improvements


- Allowing users to crop or edit the image before background removal.
- Adding support for batch processing of multiple images.
