from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import os

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    img_file = request.files['image']
    img_file.save("temp.jpg")

    try:
        text = pytesseract.image_to_string(Image.open("temp.jpg"), lang="ind")
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        os.remove("temp.jpg")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)