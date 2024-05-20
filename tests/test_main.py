# tests/test_main.py
from src.main import helo_world
 
def test_helo_world():
    assert helo_world() == "Helo, world!