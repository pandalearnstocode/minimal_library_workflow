import minipackage as minipack


def test_hello_world_lib():
    assert minipack.hello_world() == "Hello World!"


def test_hello_mcu_lib():
    assert minipack.hello_mcu() == "Hello MCU!"

def test_hello_dc_lib():
    assert minipack.hello_dc() == "Hello DC!"
