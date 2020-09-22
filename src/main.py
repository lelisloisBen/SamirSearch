from flask import Flask, request, jsonify
from google import google as MYBESTSEARCH
from flask_cors import CORS
from utils import APIException

app = Flask(__name__)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def hello_world():
    return "<div style='text-align: center; background-color: orange'><h1>Backend running...</h1><br/><h3>Welcome back samir</h3><img src='https://media.gettyimages.com/photos/woman-sitting-by-washing-machine-picture-id117852649?s=2048x2048' width='80%' /></div>"

@app.route('/info', methods=['GET'])
def getClientInfo():

    ip_address = request.remote_addr
    client_host = request.host
    client_url = request.host_url

    if request.method == 'GET':
        return jsonify({
            'server': 'success',
            'ip': ip_address,
            'host': client_host,
            'url': client_url
        })

@app.route('/search', methods=['POST'])
def searchComplex():
    body = request.get_json()
    
    if request.method == 'POST':
        theWord = body['word']

        myComplexSearchList = []

        for result in MYBESTSEARCH.search(theWord, 3):
            myComplexSearchList.append({
                "name": result.name,
                "link": result.link,
                "description": result.description
            })
        
        return jsonify({
            'server': 'success',
            'msg': myComplexSearchList
        })
    return "Error coming along..."

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)