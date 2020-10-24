from day_07b import *

def test_get_every_nth_state():
    assert get_every_nth_state(n=3)[0] == 'North Carolina'
    assert get_every_nth_state(n=4)[1] == 'Colorado'

def test_get_state_abbrev():
    assert get_state_abbrev('Alabama') == 'AL'
