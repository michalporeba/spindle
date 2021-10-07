import pytest 
import types, uuid, hashlib
import spindle as spd
from .fakes import FakeModel
from spindle import Message, Conflict

def test_values_from_single_model():
     model = FakeModel()
     sut = spd.create()
     sut.add_model('src', model.to_ns())
     assert sut.values()['text'] == model.text
     assert sut.values()['number'] == model.number

def test_message_setting_property():
    sut = spd.create()
    sut.add_message(Message('src', 'property_a', 'value_a'))
    assert not len(sut.conflicts())
    assert sut.values()['property_a'] == 'value_a'

def test_message_setting_properties():
    sut = spd.create()
    sut.add_message(Message('src', 'prop_a', '123'))
    sut.add_message(Message('src', 'prop_b', '456'))
    assert not len(sut.conflicts())
    assert sut.values()['prop_a'] == '123'
    assert sut.values()['prop_b'] == '456'
    

def test_concurrent_orfan_value_changes_result_in_conflict():
    sut = spd.create()
    a = Message('src_a', 'my_prop', 12)
    b = Message('src_b', 'my_prop', 42)
    c = Message('src_c', 'my_prop', 73)
    sut.add_message(a, b, c)
    assert 'my_prop' in sut.conflicts()
    value = sut.values()['my_prop']
    assert isinstance(value, Conflict)
    assert len(value.candidates)==3
    assert a in value.candidates
    assert b in value.candidates
    assert c in value.candidates 
    
def test_conflicts_dont_get_mixed_up():
    sut = spd.create()
    a = Message('src_a', 'prop1', 12)
    b = Message('src_b', 'prop1', 42)
    c = Message('src_c', 'prop2', 73)
    d = Message('src_a', 'prop2', 88)
    x = Message('src_b', 'prop3', 45)
    sut.add_message(a, b, c, d, x)
    assert 'prop1' in sut.conflicts()
    assert 'prop2' in sut.conflicts()
    assert 'prop3' in sut.values()
    prop1 = sut.values()['prop1']
    prop2 = sut.values()['prop2']
    assert not a in prop2.candidates
    assert not b in prop2.candidates
    assert not x in prop2.candidates
    assert not c in prop1.candidates
    assert not d in prop1.candidates
    assert not x in prop1.candidates 