from flask import Flask, request, jsonify, render_template
import base64
import cv2
import numpy as np

app = Flask(__name__)

# HTML 파일을 렌더링
@app.route('/')
def index():
    return render_template('index.html')  # HTML 파일은 templates/index.html에 있어야 함

# 이미지 비교 엔드포인트
@app.route('/compare', methods=['POST'])
def compare_faces():
    try:
        # JSON 데이터 파싱
        data = request.get_json()
        uploaded_image_base64 = data.get('uploadedImage')
        webcam_image_base64 = data.get('webcamImage')

        # Base64 디코딩
        uploaded_image = decode_base64_to_image(uploaded_image_base64)
        webcam_image = decode_base64_to_image(webcam_image_base64)

        # 얼굴 비교 (간단히 픽셀 차이로 유사도 계산 - 실제 프로젝트에서는 OpenCV, DeepFace 사용)
        similarity = calculate_similarity(uploaded_image, webcam_image)

        # 결과 반환
        return jsonify({'similarity': similarity})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Base64 문자열을 이미지로 디코딩
def decode_base64_to_image(base64_string):
    base64_data = base64_string.split(',')[1]
    image_data = base64.b64decode(base64_data)
    np_array = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    return image

# 두 이미지를 비교하여 유사도 계산 (여기서는 간단한 MSE 사용)
def calculate_similarity(image1, image2):
    if image1.shape != image2.shape:
        # 크기가 다른 이미지를 리사이즈
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    # Mean Squared Error 계산
    mse = np.mean((image1 - image2) ** 2)
    max_pixel_value = 255.0
    similarity = max(0, 100 - (mse / (max_pixel_value ** 2)) * 100)  # 간단한 100% 기준 변환
    return round(similarity, 2)

if __name__ == '__main__':
    app.run(debug=True)


