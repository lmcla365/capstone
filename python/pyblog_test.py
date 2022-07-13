#!/usr/bin/env python3

import solar

def test_get_observer_location():
    val = get_observer_location()
    assert val == '39.0438 -77.4874'

def test_print_position():
    val = print_position('123.45', '64.78')
    assert val == 'The Sun is currently at: 123.45 degrees azimuth 64.78 degrees altitude'