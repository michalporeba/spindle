import random, uuid, hashlib
import types

class FakeModel():
    def __init__(self):
        self.empty = None
        self.number = random.randint(11,99)
        self.text = hashlib.md5(str(uuid.uuid1()).encode('utf-8')).hexdigest()
        self._private = 'this should not be included'

    def to_dict(self):
        return {k: v for k, v in vars(self).items()}

    def to_ns(self):
        return types.SimpleNamespace(**self.to_dict())