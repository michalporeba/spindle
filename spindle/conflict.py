from .message import Message

class Conflict:

    def __init__(self, *messages: Message):
        self.candidates = list(*messages)

