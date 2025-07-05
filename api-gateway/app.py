from flask import Flask, request, jsonify, render_template
from werkzeug.middleware.proxy_fix import ProxyFix
import requests

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

SERVICE_AGE_URL = "http://localhost:5001/age"
SERVICE_POIDS_URL = "http://localhost:5002/poids"


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            birthdate = request.form.get('birthdate')
            height = request.form.get('height')

            age_resp = requests.post(SERVICE_AGE_URL, json={'birthdate': birthdate})
            poids_resp = requests.post(SERVICE_POIDS_URL, json={'height': float(height)})

            age = age_resp.json().get('age')
            poids = poids_resp.json().get('poids_optimal')

            result = f"Bonjour {name}, vous avez {age} ans et votre poids optimal est {poids} kg."
        except Exception as e:
            result = f"Erreur : {str(e)}"

    return render_template('index.html', result=result)

@app.route('/service-age', methods=['POST'])
def proxy_service_age():
    try:
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400
            
        data = request.get_json()
        if 'birthdate' not in data:
            return jsonify({"error": "birthdate is required"}), 400

        resp = requests.post(SERVICE_AGE_URL, json=data)
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Service age unavailable: {str(e)}"}), 502
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@app.route('/service-poids', methods=['POST'])
def proxy_service_poids():
    try:
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400
            
        data = request.get_json()
        if 'height' not in data:
            return jsonify({"error": "height is required"}), 400

        resp = requests.post(SERVICE_POIDS_URL, json=data)
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Service poids unavailable: {str(e)}"}), 502
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)