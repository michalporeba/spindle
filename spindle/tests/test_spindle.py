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

def test_multiple_repetitions_of_a_message_doesnt_affect_scalar_value():
    sut = spd.create()
    m = Message('src', 'my_prop', 42)
    sut.add_message(m)
    sut.add_message(m)
    assert not 'my_prop' in sut.conflicts()
    assert sut.values()['my_prop'] == 42

def test_single_line_of_a_scalar_value_message():
    sut = spd.create()
    a = Message('src', 'my_prop', 1)
    b = Message('src', 'my_prop', 3, a.signature)
    c = Message('src', 'my_prop', 2, b.signature)
    sut.add_message(a, b, c)
    assert not 'my_prop' in sut.conflicts()
    assert sut.values()['my_prop'] == 2

def test_single_line_of_a_scalar_value_message_in_reverse_order():
    sut = spd.create()
    a = Message('src', 'my_prop', 1)
    b = Message('src', 'my_prop', 3, a.signature)
    c = Message('src', 'my_prop', 2, b.signature)
    sut.add_message(c, b, a)
    assert not 'my_prop' in sut.conflicts()
    assert sut.values()['my_prop'] == 2

def test_simple_conflict_resolution():
    sut = spd.create()
    a = Message('src1', 'my_prop', 'abc')
    b = Message('src2', 'my_prop', 'def') 
    sut.add_message(a,b)
    assert 'my_prop' in sut.conflicts()
    r = Message('src1', 'my_prop', 'abcdef', a.signature, b.signature)
    sut.add_message(r)
    assert not 'my_prop' in sut.conflicts()
    assert sut.values()['my_prop'] == 'abcdef'

def test_complex_conflict_resolution():
    sut = spd.create()
    a = Message('src1', 'p', 'abc')
    b = Message('src2', 'p', 'def') 
    b1 = Message('src2', 'p', 'de', b.signature)
    b2 = Message('src3', 'p', 'defg', b.signature)
    sut.add_message(a,b, b1, b2)
    assert 'p' in sut.conflicts()
    assert len([m for m in sut.values()['p'].candidates if m.value == 'abc'])
    assert len([m for m in sut.values()['p'].candidates if m.value == 'de'])
    assert len([m for m in sut.values()['p'].candidates if m.value == 'defg'])
    assert not len([m for m in sut.values()['p'].candidates if m.value == 'def'])
    # resolve the b branch
    r1 = Message('src2', 'p', 'x', b1.signature, b2.signature)
    sut.add_message(r1)
    assert 'p' in sut.conflicts()
    assert len([m for m in sut.values()['p'].candidates if m.value == 'abc'])
    assert len([m for m in sut.values()['p'].candidates if m.value == 'x'])
    # resolve it all
    r2 = Message('src2', 'p', 'abcx', a.signature, r1.signature)
    sut.add_message(r2)
    assert not 'p' in sut.conflicts()
    assert sut.values()['p'] == 'abcx'

def test_automatically_resolve_same_value_from_different_sources():
    sut = spd.create()
    a = Message('src1', 'p', 'abc')
    b1 = Message('src2', 'p', 'x', a.signature)
    b2 = Message('src3', 'p', 'x', a.signature)
    sut.add_message(a, b1, b2)
    assert not 'p' in sut.conflicts()
    assert sut.values()['p'] == 'x'
    assert not 'src1' in sut.values()['p'].sources()
