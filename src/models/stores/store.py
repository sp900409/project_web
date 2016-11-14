import uuid

from src.common.database import Database
import src.models.stores.constants as StoreConstants
import src.models.stores.errors as StoreErrors

class Store(object):
    def __init__(self, name, url_prefix, tag_name, query, _id=None):
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = uuid.uuid4().hex if _id is None else _id


    def __repr__(self):
        return "<Store {}>".format(self.name)

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }

    @classmethod
    def get_by_id(cls, id):
        return cls(**Database.find_one(StoreConstants.COLLECTIONS, {"_id": id}))

    def save_to_mongo(self):
        Database.update(StoreConstants.COLLECTIONS, {'_id': self._id}, self.json())

    @classmethod
    def get_by_name(cls, store_name):
        return cls(**Database.find_one(StoreConstants.COLLECTIONS, {"name": store_name}))

    @classmethod
    def get_by_url_prefix(cls, url_prefix):
        return cls(**Database.find_one(StoreConstants.COLLECTIONS, {"url_prefix": {'$regex':'^{}'.format(url_prefix)}}))

    @classmethod
    def find_by_url(cls,url):
        """
        Return a store from a url like http://www.johnlewis.com/item/dsafsdagljksld
        :param url: The item's url
        :return: a Store, or reises a StoreNotFoundExcept if no store matchs the URL
        """
        for i in range(0, len(url)+1):
            try:
                store = cls.get_by_url_prefix(url[:i])
                return store
            except:
                raise StoreErrors.StoreNotFoundException("he URL Prefix used to find store didn't give us any result")

    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find(StoreConstants.COLLECTIONS, {})]

    def delete(self):
        Database.remove(StoreConstants.COLLECTIONS,{'_id': self._id})
