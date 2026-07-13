from menus import menu
from utils import browse
from encoder import e5, e6
from decoder import d5, d6

class ExceptionType(Exception):
    pass

def encode():
    menu(1)

    if "c1" not in __dict__:
        return

    if c1 == "File":
        result = browse("Text")
        if not result:
            return
        e, u_data = result
    else:
        text_value = menu(2)
        if text_value is None:
            return
        u_data = text_value.encode("utf-8")
        e = 5

    edition = globals().get("ed", e)

    if edition == 5:
        e5(u_data)
    elif edition == 6:
        e6(u_data)
    else:
        raise ExceptionType("Unsupported character(s) used, pls refer to README for the list of supported characters.")


def decode():
    edition, u_data = browse("QB")
    
    if edition == 5:
        d5(u_data)
    elif edition == 6:
        d6(u_data)
    else:
        raise ExceptionType("Tampered or invalid file type. Please provide a valid Quantum Being file.")