from .message import Message
from .thread import Thread
from .conflict import Conflict

class Spindle():
    def __init__(self):
        self._threads = {}
        
    def add_model(self, source, model):
        if model: 
            for k, v in self._model_to_dict(model).items():
                self.add_message(Message(source, k, v))
                
    def add_message(self, message):
        if not message.property in self._threads:
            self._threads[message.property] = Thread()
        self._threads[message.property].add(message)
        
    def values(self) -> dict:
        return {k: v.flat_value() for k, v in self._threads.items()}

    def conflicts(self) -> list:
        return {k: v for k, v in self._threads.items() if isinstance(v.value(), Conflict)}.keys()

    def _model_to_dict(self, model) -> dict:
        if isinstance(model, dict):
            return {k: v for k, v in model.items() if not k.startswith('_')}
        else: 
            print(vars(model).items())
            return {k: v for k, v in vars(model).items() if not k.startswith('_')}
