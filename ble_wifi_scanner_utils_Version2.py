"""
Utility functions for BLE/Wi-Fi scanner.
Shared helpers for parsing, windowing, etc.
"""

from typing import List, Tuple, Optional

def window_tail(vals: List[float], limit: int) -> Tuple[List[int], List[float]]:
    """Return indexes and tail values for plotting window."""
    n = max(1, int(limit))
    tail = list(vals[-n:])
    return list(range(len(tail)), tail)

def parse_signal_to_dbm(token: str) -> Optional[int]:
    """Parse signal strength token to dBm integer."""
    # TODO: Copy and improve your signal parsing logic here
    pass