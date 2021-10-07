import hashlib 

class Message:
    def __init__(self, source: str, property: str, value, *parents: str):
        self.source = source
        self.property = property
        self.value = value 
        self.parents = list(parents)
        self.signature = self.__get_signature()

    def __get_signature(self):
        signature = hashlib.md5(str(self.value).encode('utf-8')).hexdigest()
        for parent in self.parents:
            signature = hashlib.md5((signature+parent).encode('utf-8')).hexdigest()
        return signature