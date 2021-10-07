import hashlib 

class Message:
    def __init__(self, source: str, property: str, value):
        self.source = source
        self.property = property
        self.value = value 
        self.signature = self.__get_signature()

    def __get_signature(self):
        return hashlib.md5(str(self.value).encode('utf-8')).hexdigest()