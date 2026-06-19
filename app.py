from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['POST'])
def proxy():
    client_id = request.headers.get('X-Naver-Client-Id')
    client_secret = request.headers.get('X-Naver-Client-Secret')
    
    res = requests.post(
        'https://openapi.naver.com/v1/datalab/search',
        headers={
            'Content-Type': 'application/json',
            'X-Naver-Client-Id': client_id,
            'X-Naver-Client-Secret': client_secret,
        },
        json=request.get_json()
    )
    
    response = jsonify(res.json())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, res.status_code

@app.route('/proxy', methods=['OPTIONS'])
def proxy_options():
    response = jsonify({})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
    return response, 200

if __name__ == '__main__':
    app.run()
