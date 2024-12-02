from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Compare route for face matching
@app.route('/compare', methods=['POST'])
def compare_faces():
    data = request.get_json()
    uploaded_image = data.get('uploadedImage')
    webcam_image = data.get('webcamImage')

    # Simulated similarity calculation
    similarity = 95  # Replace with actual face comparison logic if available

    return jsonify({'similarity': similarity})

if __name__ == '__main__':
    app.run(debug=True)
