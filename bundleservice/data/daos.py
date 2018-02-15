"""
Data access object definitions
"""
import sqlalchemy as sa
from bundleservice.data.models import Bundle, db_session


class BundlesDAO(object):

    def get(self, device_uuid: str, sensor_type: str,
            start_time: int, end_time: int):
        """
        Fetch and return bundles from DB
        """
        result = db_session.query(
            Bundle.device_uuid,
            Bundle.sensor_type,
            Bundle.sensor_value,
            Bundle.sensor_reading_time
            )\
            .select_from(Bundle)\
            .filter(
                Bundle.device_uuid == device_uuid,
                Bundle.sensor_type == sensor_type,
                Bundle.sensor_reading_time >= start_time,
                Bundle.sensor_reading_time <= end_time,
            ).all()
        return [bundle._asdict() for bundle in result]

    def create(self, **kwargs):
        """
        Add bundle to DB
        """
        new_bundle = Bundle(**kwargs)
        db_session.add(new_bundle)
