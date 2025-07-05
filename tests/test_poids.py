import sys
import os
import json
import pytest  # type: ignore

# Ajouter le chemin vers le dossier contenant app.py du service-poids
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../service-poids')))

from service_poids.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_poids(client):
    response = client.post('/poids', json={'height': 180})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'poids_optimal' in data
    assert isinstance(data['poids_optimal'], float)
    assert data['poids_optimal'] == 72.0  # 0.9 * (180 - 100)