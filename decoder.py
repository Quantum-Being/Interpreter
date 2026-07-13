from libraries import library5d as library5, library6d as library6
from menus import menu

def d5():
    menu(3)

    with open("output.qb5", "rb") as f:
        binary = f.read().decode("ascii")

    chunks = [binary[i:i+5] for i in range(0, len(binary), 5)]
    n_chunks = len(chunks)
    decoded = ""

    for i in range(n_chunks):
        if chunks[i] in library5:
            decoded += library5[chunks[i]]

    with open("decoded.txt", "w") as f:
        f.write(decoded)

def d6():
    file_name = menu(3)

    with open(file_name + ".qb6", "rb") as f:
        binary = f.read().decode("ascii")

    chunks = [binary[i:i+6] for i in range(0, len(binary), 6)]
    n_chunks = len(chunks)
    decoded = ""

    for i in range(n_chunks):
        if chunks[i] in library6:
            decoded += library6[chunks[i]]

    with open(file_name + ".txt", "w") as f:
        f.write(decoded)
