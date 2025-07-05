from flask import Flask, request, jsonify



app = Flask(__name__)

@app.route('/poids', methods=['POST'])
def get_poids():
    data = request.json
    height = float(data['height'])
    poids = 0.9 * (height - 100)
    return jsonify({'poids_optimal': round(poids, 1)})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
