def greet(name):
    if not name:
        raise ValueError("name must not be empty")
    return f"Hola, {name}!"


def shout(text):
    return text.upper() + "!"
