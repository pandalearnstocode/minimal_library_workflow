from source.main import hello_world


def test_say_hello():
    assert hello_world() == "Hello World!"