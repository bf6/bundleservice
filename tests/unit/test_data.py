"""
Test data access objects
"""
from unittest.mock import patch
from bundleservice.data.daos import BundlesDAO
from bundleservice.data.models import Bundle


@patch('bundleservice.data.daos.db_session')
def test_bundlesdao_get(MockDbSession):
    mock_data = {
        'device_uuid': 'b21ad0676f26439482cc9b1c7e827de4',
        'sensor_type': 'temperature',
        'start_time': 0,
        'end_time': 1510093202,
    }
    bundles = BundlesDAO().get(**mock_data)
    assert MockDbSession.query.call_count

@patch('bundleservice.data.daos.db_session')
def test_bundlesdao_create(MockDbSession):
    mock_data = {
        'device_uuid': 'b21ad0676f26439482cc9b1c7e827de4',
        'sensor_type': 'humidity',
        'sensor_value': 0.5,
        'sensor_reading_time': 1510093202,
    }
    BundlesDAO().create(**mock_data)
    assert MockDbSession.add.call_count
    assert isinstance(MockDbSession.add.call_args[0][0], Bundle)

