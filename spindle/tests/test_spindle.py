import pytest 
import types, uuid, hashlib
import spindle as spd
from .fakes import FakeModel

def test_values_from_single_model():
     model = FakeModel()

     sut = spd.create(model.to_ns())

     assert sut.values['text'] == model.text
     assert sut.values['number'] == model.number
