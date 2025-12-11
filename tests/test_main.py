import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200

def test_contact_get(client):
    response = client.get('/contact')
    assert response.status_code == 200

def test_contact_post(client):
    response = client.post('/contact', data={'name': 'Test', 'email': 'test@example.com'})
    assert response.status_code == 200
    assert b'Thanks Test!' in response.data

def test_api_time(client):
    response = client.get('/api/time')
    assert response.status_code == 200
    assert 'current_time' in response.get_json()