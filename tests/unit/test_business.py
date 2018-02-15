"""
Test business layer objects
"""
from unittest.mock import patch
from bundleservice.business.bundles import Bundles

@patch('bundleservice.business.bundles.Bundles.dao')
def test_bundles_get(MockBundlesDAO):
    mock_data = {
        'device_uuid': 'b21ad0676f26439482cc9b1c7e827de4',
        'sensor_type': 'temperature',
        'start_time': 0,
        'end_time': 1510093202,
    }
    bundles = Bundles.get(**mock_data)
    MockBundlesDAO.get.assert_called_with(**mock_data)

@patch('bundleservice.business.bundles.Bundles.dao')
def test_bundles_create(MockBundlesDAO):
    mock_data = {
        'device_uuid': 'b21ad0676f26439482cc9b1c7e827de4',
        'sensor_type': 'humidity',
        'sensor_value': 0.5,
        'sensor_reading_time': 1510093202,
    }
    bundles = Bundles.create(**mock_data)
    MockBundlesDAO.create.assert_called_with(**mock_data)
