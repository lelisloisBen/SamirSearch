from flask import Flask, request, jsonify, json
from googlesearch import search as MYSEARCH
from google import google as MYBESTSEARCH
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return "hello Samir, Your Backend is running..."

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