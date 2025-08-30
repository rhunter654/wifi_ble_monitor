import pytest
from ble_wifi_scanner.utils import window_tail, parse_signal_to_dbm

def test_window_tail():
    vals = [1,2,3,4,5]
    idx, tail = window_tail(vals, 3)
    assert idx == [0,1,2]
    assert tail == [3,4,5]

def test_parse_signal_to_dbm():
    assert parse_signal_to_dbm("-43 dBm") == -43
    # Add more cases
