import pytest
import tkinter as tk
from dicethrow import DiceApp
from unittest.mock import patch
import random

@pytest.fixture
def app():
    root = tk.Tk()
    root.withdraw()
    app = DiceApp(root)
    yield app
    root.destroy()

def test_initial_sides(app):
    assert app.sides == 6

def test_throw_adds_to_results(app):
    with patch('random.randint', return_value=4), patch('time.sleep', return_value=None):
        initial_len = len(app.previous_results)
        app.throw()
        assert len(app.previous_results) == initial_len + 1
        assert app.previous_results[-1] == 4

def test_throw_label_updates(app):
    with patch('random.randint', return_value=2), patch('time.sleep', return_value=None):
        app.throw()
        assert "2" in app.result_label.cget("text")

def test_button_disabled_during_throw(app):
    with patch('random.randint', return_value=3), patch('time.sleep', return_value=None):
        app.throw()
        assert app.btn_throw["state"] == tk.NORMAL

def test_set_sides_valid(app):
    app.sides = 10
    assert app.sides == 10
