from pathlib import Path


class ProtoDatabase:
    def __init__(self, path, proto_types, engine):
        """
        :param proto_types: types of objects that will be stored in the db
        :param engine: tinydb or sqlite.
        """
        self.engine = engine
        self.proto_types = proto_types
        self.path = Path(path)

        # if path already exists - load
        if self.path.exists():

            if self.engine == 'sqlite':
                import sqlite3
                self.db = sqlite3.connect('//' + str(self.path))
            elif self.engine == 'tinydb':
                import tinydb
                self.db = tinydb.load(self.path)
        else:
            # create new

            if self.engine == 'sqlite':
                import sqlite3
                self.db = sqlite3.connect('//' + str(self.path))
            elif self.engine == 'tinydb':
                import tinydb
                self.db = tinydb.create(self.path)

    def add_item(self, item, uid=None):  # item - protobuf instance
        if uid is None:
            # take from item
            uid = item.uid

        # add
        item = item.serialize()
        table = type(item).name
        if self.engine == 'sqlite':
        # add to sqlite

        self.db

    def get_item(self, uid, proto_type=None):
