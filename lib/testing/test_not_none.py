#!/usr/bin/env python3

from not_none_functions import return_not_none
from bool_functions import return_true

def test_return_not_none():
    '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
    result = return_not_none()
    assert result is None, "Expected None, but got a non-None value."

def test_return_true():
    '''in bool_functions, function "return_true" returns True.'''
    assert return_true() == True