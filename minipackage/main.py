import random


def hello_world():
    """This is a hello world function.

    Returns:
        str: Hello world
    """
    return "Hello World!"


def hello_mcu():
    """This is a hello mcu function.

    Returns:
        str: hello mcu
    """
    return "Hello MCU!"


def hello_dc():
    """This is a hello dc function.

    Returns:
        str: hello dc
    """
    return "Hello DC!"


def ramdom_function():
    return random.randint(0, 100)


def main():
    print(hello_world())
    print(hello_mcu())
    print(hello_dc())
    print(ramdom_function())
