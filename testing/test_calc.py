import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import calc

def test_add():
    assert calc.add(1, 2) == 3

