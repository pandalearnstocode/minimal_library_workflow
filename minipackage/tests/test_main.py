from minipackage.main import hello_world, hello_mcu, hello_dc, hello_mcu_dc


def test_say_hello():
    assert hello_world() == "Hello World!"


def test_say_hello_mcu():
    assert hello_mcu() == "Hello MCU!"


def test_say_hello_dc():
    assert hello_dc() == "Hello DC!"

def test_say_hello_mcu_dc():
    assert hello_mcu_dc() == "Hello MCU DC!"
