import requests
import pytest

API_GATEWAY_URL = "http://localhost:8000"

def test_service_age():
    """Test du service d'âge"""
    test_data = {"birthdate": "1990-01-01"}
    
    response = requests.post(
        f"{API_GATEWAY_URL}/service-age",
        json=test_data,
        headers={"Content-Type": "application/json"},
        timeout=10
    )
    
    # Debug: affiche la réponse complète en cas d'échec
    print(f"Response: {response.status_code}, {response.text}")
    
    assert response.status_code == 200, f"Le endpoint /service-age devrait retourner 200. Réponse: {response.status_code}, {response.text}"
    assert "age" in response.json()

def test_service_poids():
    """Test du service de poids"""
    test_data = {"height": 175}
    
    response = requests.post(
        f"{API_GATEWAY_URL}/service-poids",
        json=test_data,
        headers={"Content-Type": "application/json"},
        timeout=10
    )
    
    # Debug: affiche la réponse complète en cas d'échec
    print(f"Response: {response.status_code}, {response.text}")
    
    assert response.status_code == 200, f"Le endpoint /service-poids devrait retourner 200. Réponse: {response.status_code}, {response.text}"
    assert "poids_optimal" in response.json()