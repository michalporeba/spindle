import pytest 
import types, uuid, hashlib
import spindle as spd
from .fakes import FakeModel
from spindle import Message

def test_values_from_single_model():
     model = FakeModel()

     sut = spd.create(model.to_ns())

     assert sut.values['text'] == model.text
     assert sut.values['number'] == model.number

def test_message_setting_property():
    sut = spd.create()
    sut.add_message('src', Message('property_a', 'value_a'))
    assert sut.values['property_a'] == 'value_a'

def test_message_setting_properties():
    sut = spd.create()
    sut.add_message('src', Message('prop_a', '123'))
    sut.add_message('src', Message('prop_b', '456'))
    assert sut.values['prop_a'] == '123'
    assert sut.values['prop_b'] == '456'
