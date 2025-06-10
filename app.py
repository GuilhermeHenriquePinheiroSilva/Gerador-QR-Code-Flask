from flask import Flask, request, jsonify, render_template
import qrcode
import base64
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite acesso do frontend


@app.route('/')
def home(): 
    return render_template('index.html');


@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'Texto não fornecido'}), 400

    # Gerar o QR code
    qr = qrcode.make(text)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    base64_img = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return jsonify({'qr_code': base64_img})

if __name__ == '__main__':
    app.run(debug=True)
