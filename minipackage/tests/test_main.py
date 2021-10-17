from minipackage.main import hello_world, hello_mcu


def test_say_hello():
    assert hello_world() == "Hello World!"

def test_say_hello_mcu():
    assert hello_mcu() == "Hello MCU!"
