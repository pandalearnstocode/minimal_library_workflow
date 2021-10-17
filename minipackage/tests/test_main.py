from minipackage.main import hello_world, hello_mcu, hello_dc


def test_say_hello():
    assert hello_world() == "Hello World!"


def test_say_hello_mcu():
    assert hello_mcu() == "Hello MCU!"


def test_say_hello_dc():
    assert hello_dc() == "Hello DC!"
