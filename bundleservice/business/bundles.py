"""
Bundle business object
"""
from bundleservice.data import BundlesDAO

class Bundles(object):
    dao = BundlesDAO()

    @classmethod
    def get(cls, **criteria):
        """
        Return bundles that match `criteria`
        """
        return cls.dao.get(**criteria)

    @classmethod
    def create(cls, **data):
        """
        Save new bundle to DB
        """
        return cls.dao.create(**data)
