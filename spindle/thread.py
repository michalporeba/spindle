from .conflict import Conflict 
from .message import Message

class Thread():
    def __init__(self):
        self.messages = []
        self.__current = None
        
    def add(self, message: Message):
        if len([m for m in self.messages if m.signature == message.signature]):
            return

        self.messages.append(message)
        if len(self.messages) == 1:
            self.__current = message.value    
        else:
            self.__current = Conflict(self.messages)        
        
    def value(self):
        return self.__current

    def flat_value(self):
        if isinstance(self.__current, Conflict):
            return None
        return self.__current
    