from flask import Flask, request
import json
from flask_cors import CORS
from luhnscalculator import checkIsValidSequence,getCheckDigit

app = Flask(__name__)
CORS(app)

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/check_is_valid', methods=['GET'])
def check_is_valid():
    sequence = request.args.get('sequence', None)

    if sequence is None:
        response = {'error': 'Parameter "sequence" is required.'}
        return json.dumps(response), 400, {'Content-Type': 'application/json'}

    try:
        isValidSequence = checkIsValidSequence(sequence)

        response = {
            'isValid': isValidSequence,
        }

        return json.dumps(response), 200, {'Content-Type': 'application/json'}

    except Exception as e:
        response = {'error': str(e)}
        return json.dumps(response), 400, {'Content-Type': 'application/json'}

@app.route('/check_digit', methods=['GET'])
def checkDigit():
    sequence = request.args.get('sequence', None)
    if sequence is None:
        response = {'error': 'Parameter "sequence" is required.'}
        return json.dumps(response), 400, {'Content-Type': 'application/json'}
    try:
        checkValue=getCheckDigit(sequence)
        response={
            'checkDigit' : checkValue
         }
        return json.dumps(response), 200, {'Content-Type': 'application/json'}
    except Exception as e:
        response = {'error': str(e)}
        return json.dumps(response), 400, {'Content-Type': 'application/json'}
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
