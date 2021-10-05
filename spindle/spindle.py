import uuid 

class Spindle():
    def __init__(self, model=None):
        self._messages = {}
        self.values = {}
        if model: 
            for k, v in self._model_to_dict(model).items():
                self.values[k] = v

    def add_message(self, source, message):
        if not source in self._messages:
            self._messages[source] = []
        self._messages[source].append(message)
        self.values[message.property] = message.value

    def _model_to_dict(self, model) -> dict:
        if isinstance(model, dict):
            return {k: v for k, v in model.items() if not k.startswith('_')}
        else: 
            print(vars(model).items())
            return {k: v for k, v in vars(model).items() if not k.startswith('_')}
