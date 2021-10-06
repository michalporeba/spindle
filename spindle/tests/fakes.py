import random, uuid, hashlib
import types

class FakeModel():
    ids = list(range(99))
    
    def __init__(self):
        random.shuffle(FakeModel.ids)
        self.empty = None
        self.number = FakeModel.ids.pop()
        self.text = hashlib.md5(str(uuid.uuid1()).encode('utf-8')).hexdigest()
        self._private = 'this should not be included'

    def to_dict(self):
        return {k: v for k, v in vars(self).items()}

    def to_ns(self):
        return types.SimpleNamespace(**self.to_dict())