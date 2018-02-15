"""
Instantiate API class, define routes and set route handlers here
"""
import falcon
from bundleservice.service.handlers import BundlesHandler
from bundleservice.service.middleware import Serializer


api = falcon.API(middleware=[Serializer()])
api.add_route('/bundles', BundlesHandler())
