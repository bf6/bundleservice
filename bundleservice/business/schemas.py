"""
Define the shape of business objects here
"""
from marshmallow import fields, Schema
from marshmallow.validate import OneOf, Range

class BundleSchema(Schema):
    """
    All Bundles should be shaped like this :)
    """
    device_uuid = fields.UUID(required=True)
    sensor_type = fields.Str(
        validate=OneOf(['temperature','humidity']),
        required=True,
        )
    sensor_value = fields.Decimal(
        validate=Range(min=0.0, max=100.0),
        required=True,
        )
    sensor_reading_time = fields.Integer(required=True)

