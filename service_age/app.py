from flask import Flask, request, jsonify
from datetime import datetime




app = Flask(__name__)

@app.route('/age', methods=['POST'])
def get_age():
    data = request.json
    birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d')
    age = (datetime.today() - birthdate).days // 365
    return jsonify({'age': age})




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
