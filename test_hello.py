# test_hello.py
from hello import greet

def test_greet():
    assert greet("World") == "Hello, Universe!"
    assert greet("CI/CD") == "Hello, CI/CD!"
