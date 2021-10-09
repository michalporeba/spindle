from .conflict import Conflict 
from .message import Message

class Thread():
    def __init__(self):
        self.messages = []
        self.__current = None
        self.__parents = []
        self.__candidates = []
        self.__surces = []
        
    def add(self, message: Message):
        if len([m for m in self.messages if m.signature == message.signature]):
            return

        self.messages.append(message)
        
        if not message.signature in self.__parents: 
            self.__candidates.append(message.signature)
            
        newParents = [p for p in message.parents if not p in self.__parents]
        self.__candidates = [c for c in self.__candidates if not c in newParents]
        self.__parents.extend(message.parents)
        if not len(self.__candidates):
            self.__current = None
        if len(self.__candidates) == 1:
            self.__current = [m for m in self.messages if m.signature in self.__candidates][0].value
        else:
            self.__current = Conflict([m for m in self.messages if m.signature in self.__candidates])        
        
    def value(self):
        return self.__current

    def flat_value(self):
        if isinstance(self.__current, Conflict):
            return None
        return self.__current
    