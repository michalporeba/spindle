from .message import Message
from .thread import Thread
from .conflict import Conflict
from typing import Union
import types

class Spindle():
    def __init__(self):
        self.__threads = {}
        
    def add_model(self, source: str, model: Union[types.SimpleNamespace, dict]):
        if model: 
            for k, v in self.__model_to_dict(model).items():
                self.add_message(Message(source, k, v))
                
    def add_message(self, *messages: Message):
        for message in messages:
            if not message.property in self.__threads:
                self.__threads[message.property] = Thread()
            self.__threads[message.property].add(message)
        
    def values(self) -> dict:
        return {k: v.value() for k, v in self.__threads.items()}

    def conflicts(self) -> list:
        return {k: v for k, v in self.__threads.items() if isinstance(v.value(), Conflict)}.keys()

    def __model_to_dict(self, model: Union[types.SimpleNamespace, dict]) -> dict:
        if isinstance(model, dict):
            return {k: v for k, v in model.items() if not k.startswith('_')}
        else: 
            return {k: v for k, v in vars(model).items() if not k.startswith('_')}