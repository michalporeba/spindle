import pytest 
import types, uuid
from .fakes import FakeModel

def test_fake_has_random_number_property():
    a = FakeModel()
    b = FakeModel()
    assert a.number != b.number

def test_fake_has_random_text_property():
    a = FakeModel()
    b = FakeModel()
    assert a.text != b.text

def test_fake_has_more_than_one_property():
    sut = FakeModel()
    assert 1 < len([k for k, v in vars(sut).items() if not k.startswith('_')])

def test_fake_has_some_private_properties():
    sut = FakeModel()
    assert any([k for k, v in vars(sut).items() if k.startswith('_')])

def test_fake_should_have_an_empty_property():
    sut = FakeModel()
    assert sut.empty == None

def test_fake_to_dict_includes_all_properties():
    sut = FakeModel()
    d = sut.to_dict()
    assert isinstance(d, dict)
    assert d['number'] == sut.number 
    assert d['text'] == sut.text 
    assert d['empty'] == sut.empty 
    assert d['_private'] == sut._private
    assert len(d) == 4

def test_fake_to_dict_includes_all_properties():
    sut = FakeModel()
    ns = sut.to_ns()
    assert isinstance(ns, types.SimpleNamespace)
    assert ns.number == sut.number 
    assert ns.text == sut.text 
    assert ns.empty == sut.empty 
    assert ns._private == sut._private
    assert len(vars(ns)) == 4