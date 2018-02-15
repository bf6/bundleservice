"""
Bundle business object
"""
from bundleservice.data import BundlesDAO

class Bundles(object):
    dao = BundlesDAO()

    @classmethod
    def get(cls, criteria: dict):
        """
        Return bundles that match `criteria`
        """
        return cls.dao.get(**criteria)

    @classmethod
    def create(cls, bundle: dict):
        """
        Save new bundle to DB and return
        """
        return cls.dao.create(**bundle)
