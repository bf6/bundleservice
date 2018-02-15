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
        errors = GetBundlesParamsSchema().validate(data=req.params)
        if errors:
            raise falcon.HTTPBadRequest(description=errors)
        resp.context['result'] = Bundles.get(req.params)

    def on_post(self, req, resp):
        """
        Handle POST /bundles/
        """
        errors = BundleSchema().validate(data=req.media)
        if errors:
            raise falcon.HTTPBadRequest(description=errors)
        Bundles.create(req.media)
        resp.status = falcon.HTTP_201
        resp.context['result'] = {"message": "Resource created"}
