from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from PIL import Image
import io
import base64

app = Flask(__name__, static_folder='www')

@app.route('/')
def index():
    return send_from_directory('www', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('www', path)

@app.route('/api/process-image', methods=['POST'])
def process_image():
    """Process uploaded images with additional Python functionality"""
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    img = Image.open(file.stream)
    
    # Example processing: resize image
    width, height = img.size
    img_resized = img.resize((width // 2, height // 2))
    
    # Convert back to base64 for response
    buffered = io.BytesIO()
    img_resized.save(buffered, format=img.format or 'JPEG')
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    return jsonify({
        'processed': True,
        'image': f'data:image/{img.format.lower() if img.format else "jpeg"};base64,{img_str}',
        'width': width // 2,
        'height': height // 2
    })

if __name__ == '__main__':
    # Create www directory if it doesn't exist
    if not os.path.exists('www'):
        os.makedirs('www')
        # Copy files to www directory
        import shutil
        for file in os.listdir('.'):
            if file.endswith(('.html', '.js', '.json', '.png', '.svg', '.jpeg', '.jpg')):
                shutil.copy(file, 'www/')
    
    app.run(debug=True, host='0.0.0.0', port=8080)
