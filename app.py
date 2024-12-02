import face_recognition
from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # 모든 출처에서의 요청을 허용

# 얼굴 비교를 처리하는 API
@app.route('/compare', methods=['POST'])
def compare_faces():
    # 클라이언트로부터 전송된 이미지 데이터를 받기
    data = request.get_json()

    uploaded_image_data = data['uploadedImage']
    webcam_image_data = data['webcamImage']
    
    # 이미지를 파일로 변환하기 위한 코드
    uploaded_image = Image.open(io.BytesIO(np.fromstring(uploaded_image_data.split(",")[1], dtype=np.uint8)))
    webcam_image = Image.open(io.BytesIO(np.fromstring(webcam_image_data.split(",")[1], dtype=np.uint8)))
    
    # face_recognition에서 얼굴을 찾는 과정
    uploaded_face_encoding = face_recognition.face_encodings(np.array(uploaded_image))[0]
    webcam_face_encoding = face_recognition.face_encodings(np.array(webcam_image))[0]

    # 두 얼굴의 일치도를 계산
    results = face_recognition.compare_faces([uploaded_face_encoding], webcam_face_encoding)
    
    # 얼굴 일치율 계산 (기본적으로 True/False 반환)
    if results[0]:
        # 일치율 100%로 가정
        similarity_score = 100
    else:
        # 일치하지 않으면 0%
        similarity_score = 0

    # 결과 반환
    return jsonify({'similarity': similarity_score})

if __name__ == '__main__':
    app.run(debug=True)
