from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Naver-Client-Id, X-Naver-Client-Secret'
    return response

@app.after_request
def after_request(response):
    return add_cors(response)

@app.route('/proxy', methods=['GET', 'POST', 'OPTIONS'])
def proxy():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    
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
    return jsonify(res.json()), res.status_code

if __name__ == '__main__':
    app.run()
