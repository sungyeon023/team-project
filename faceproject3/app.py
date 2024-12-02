from flask import Flask, render_template, request, jsonify
import face_recognition
import numpy as np
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

def decode_base64_image(base64_string):
    """Base64 이미지를 PIL 이미지로 디코딩"""
    base64_data = base64_string.split(",")[1]
    byte_data = base64.b64decode(base64_data)
    return Image.open(BytesIO(byte_data))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare_faces():
    try:
        data = request.json
        uploaded_image_base64 = data.get('uploadedImage')
        webcam_image_base64 = data.get('webcamImage')

        if not uploaded_image_base64 or not webcam_image_base64:
            return jsonify({'error': '이미지가 제공되지 않았습니다.'}), 400

        # Base64 이미지를 디코딩하고 얼굴 인코딩 생성
        uploaded_image = decode_base64_image(uploaded_image_base64)
        webcam_image = decode_base64_image(webcam_image_base64)

        uploaded_array = np.array(uploaded_image)
        webcam_array = np.array(webcam_image)

        # 얼굴 인코딩 생성
        uploaded_encodings = face_recognition.face_encodings(uploaded_array)
        webcam_encodings = face_recognition.face_encodings(webcam_array)

        if len(uploaded_encodings) == 0 or len(webcam_encodings) == 0:
            return jsonify({'error': '얼굴을 찾을 수 없습니다.'}), 400

        # 첫 번째 얼굴만 비교 (단일 얼굴 시나리오 가정)
        similarity_score = face_recognition.face_distance([uploaded_encodings[0]], webcam_encodings[0])
        similarity_percentage = (1 - similarity_score[0]) * 100  # 0~100%로 변환

        return jsonify({'similarity': round(similarity_percentage, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
