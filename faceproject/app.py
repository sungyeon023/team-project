from flask import Flask, render_template  # render_template 임포트

app = Flask(__name__)

# 홈 페이지 라우트
@app.route('/')
def home():
    return render_template('index.html')  # templates 폴더의 index.html 파일을 렌더링

if __name__ == '__main__':
    app.run(debug=True)
