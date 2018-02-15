import pytest
from falcon import testing

from bundleservice.service import api

@pytest.fixture()
def client():
    return testing.TestClient(api)

def test_get_bundle(client):
    mock_params = {
        'device_uuid': 'b21ad0676f26439482cc9b1c7e827de4',
        'sensor_type': 'temperature',
        'start_time': 1510093202,
        'end_time': 1510093202,
    }
    mock_response = [{
        'device_uuid': 'b21ad0676f26439482cc9b1c7e827de4',
        'sensor_type': 'temperature',
        'sensor_value': 50.0,
        'sensor_reading_time': 1510093202,
    }]
    result = client.simulate_get('/bundles', params=mock_params)
    assert result.json == mock_response

def test_post_bundle(client):
    mock_body = {
        'device_uuid': 'b21ad0676f26439482cc9b1c7e827de4',
        'sensor_type': 'temperature',
        'sensor_value': 50.0,
        'sensor_reading_time': 1510093202,
    }
    result = client.simulate_post('/bundles', json=mock_body)
    assert result.json == {'message': 'Resource created'}

def test_missing_query_params(client):
    mock_params = {
        'sensor_type': 'temperature',
        'start_time': 1510093202,
        'end_time': 1510093202,
    }
    result = client.simulate_get('/bundles', params=mock_params)
    assert result.json
    assert result.status == '400 Bad Request'
    assert 'device_uuid' in result.json['description']

def test_missing_body(client):
    mock_body = {
        'device_uuid': 'b21ad0676f26439482cc9b1c7e827de4',
        'sensor_value': 50.0,
        'sensor_reading_time': 1510093202,
    }
    result = client.simulate_post('/bundles', json=mock_body)
    assert result.json
    assert result.status == '400 Bad Request'
    assert 'sensor_type' in result.json['description']

def test_extra_stuff_in_body(client):
    """ Should ignore extra fields """

    mock_body = {
        'device_uuid': 'b21ad0676f26439482cc9b1c7e827de4',
        'sensor_type': 'temperature',
        'sensor_value': 50.0,
        'sensor_reading_time': 1510093202,
        'favorite_color': 'clear',
    }
    result = client.simulate_post('/bundles', json=mock_body)
    assert result.json
    assert result.status == '201 Created'

def test_extra_query_params(client):
    mock_params = {
        'device_uuid': 'b21ad0676f26439482cc9b1c7e827de4',
        'sensor_type': 'temperature',
        'start_time': 1510093202,
        'end_time': 1510093202,
        'wipe_database': True,
    }
    mock_response = {
        'device_uuid': 'b21ad0676f26439482cc9b1c7e827de4',
        'sensor_type': 'temperature',
        'sensor_value': 50.0,
        'sensor_reading_time': 1510093202,
    }
    result = client.simulate_get('/bundles', params=mock_params)
    assert mock_response in result.json
