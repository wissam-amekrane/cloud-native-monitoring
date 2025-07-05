import sys
import os
import json
import pytest # type: ignore

# Ajouter le chemin vers le dossier contenant app.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../service-age')))

from service_age.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_age(client):
    response = client.post('/age', json={'birthdate': '2000-01-01'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'age' in data
    assert isinstance(data['age'], int)