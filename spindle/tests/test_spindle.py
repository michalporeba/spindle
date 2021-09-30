import pytest 
import types, uuid, hashlib
import spindle as spd

def test_spindle_gets_automatic_id_if_one_not_provided():
    a = spd.create()
    b = spd.create()
    assert a and b and a.values['id'] != b.values['id']

# def test_values_from_single_model():
#     model = types.SimpleNamespace()
#     a = model.a = random_string()
#     b = model.b = random_string()

#     sut = spd.create(model)

#     assert sut.values['a'] == a 
#     assert sut.values['b'] == b

def test_random_string_generator():
    a = random_string()
    b = random_string()
    assert a != b

def random_string() -> str:
    return hashlib.md5(str(uuid.uuid1()).encode('utf-8')).hexdigest()