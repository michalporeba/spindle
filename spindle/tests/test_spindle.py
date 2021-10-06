import pytest 
import types, uuid, hashlib
import spindle as spd
from .fakes import FakeModel
from spindle import Message

def test_values_from_single_model():
     model = FakeModel()
     sut = spd.create()
     sut.add_model('src', model.to_ns())
     assert sut.values()['text'] == model.text
     assert sut.values()['number'] == model.number

def test_message_setting_property():
    sut = spd.create()
    sut.add_message(Message('src', 'property_a', 'value_a'))
    assert not 'property_a' in sut.conflicts()
    assert sut.values()['property_a'] == 'value_a'

def test_message_setting_properties():
    sut = spd.create()
    sut.add_message(Message('src', 'prop_a', '123'))
    sut.add_message(Message('src', 'prop_b', '456'))
    assert not 'prop_a' in sut.conflicts()
    assert not 'prop_b' in sut.conflicts()
    assert sut.values()['prop_a'] == '123'
    assert sut.values()['prop_b'] == '456'

def test_concurrent_orfan_value_changes_result_in_conflict():
    sut = spd.create()
    sut.add_message(Message('src_a', 'my_prop', 12))
    sut.add_message(Message('src_b', 'my_prop', 42))
    assert 'my_prop' in sut.conflicts()
    
