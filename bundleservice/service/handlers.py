"""
Route handler for /bundles/
"""
import falcon
from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from bundleservice.business import Bundles
from bundleservice.business.schemas import BundleSchema


class GetBundlesParamsSchema(Schema):
    """
    Schema used to validate query params for GET /bundles/
    """
    device_uuid = fields.UUID(required=True)
    sensor_type = fields.Str(
        validate=OneOf(['temperature','humidity']),
        required=True,
        )
    start_time = fields.Integer(required=True)
    end_time = fields.Integer(required=True)


class BundlesHandler(object):

    def on_get(self, req, resp):
        """
        Handle GET /bundles/
        """
        schema = GetBundlesParamsSchema()
        errors = schema.validate(data=req.params)
        if errors:
            raise falcon.HTTPBadRequest(description=errors)

        resp.context['result'] = Bundles.get(
            device_uuid=req.params['device_uuid'],
            sensor_type=req.params['sensor_type'],
            start_time=req.params['start_time'],
            end_time=req.params['end_time'],
            )

    def on_post(self, req, resp):
        """
        Handle POST /bundles/
        """
        schema = BundleSchema()
        errors = schema.validate(data=req.media)
        if errors:
            raise falcon.HTTPBadRequest(description=errors)

        Bundles.create(
            device_uuid=req.media['device_uuid'],
            sensor_type=req.media['sensor_type'],
            sensor_value=req.media['sensor_value'],
            sensor_reading_time=req.media['sensor_reading_time'],
            )
        resp.status = falcon.HTTP_201
        resp.context['result'] = {"message": "Resource created"}
