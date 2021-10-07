from .conflict import Conflict 

class Thread():
    def __init__(self):
        self.messages = []
        self._current = None
        
    def add(self, message):
        self.messages.append(message)
        if len(self.messages) == 1:
            self._current = message.value    
        else:
            self._current = Conflict(self.messages)        
        
    def value(self):
        return self._current

    def flat_value(self):
        if isinstance(self._current, Conflict):
            return None
        return self._current
    