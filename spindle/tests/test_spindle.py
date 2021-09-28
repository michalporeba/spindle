import pytest 
import spindle as spd

def test_creation():
    s = spd.create()
    assert s != None