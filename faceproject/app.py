from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 기본 경로('/') 추가
@app.route('/')
def home():
    return "홈 페이지입니다. API는 '/compare'에서 확인할 수 있습니다."

@app.route('/compare', methods=['POST'])
def compare_faces():
    # 얼굴 비교 로직
    return jsonify({"similarity": 95})

if __name__ == "__main__":
    app.run(debug=True)
