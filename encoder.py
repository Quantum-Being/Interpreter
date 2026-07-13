from libraries import library5, library6
from menus import menu

file_name = menu(3)

def e5(x):
    binary = "0"
    chunks = [x[i:i+5] for i in range(0, len(x), 5)]
    n_chunks = len(chunks)
    binary = ""

    for i in range(n_chunks):
        if chunks[i] in library5:
            binary += library5[chunks[i]]



    with open("output.qb5", "wb") as f:
        f.write(binary.encode("ascii"))

def e6(x):
    binary = "0"
    chunks = [x[i:i+6] for i in range(0, len(x), 6)]
    n_chunks = len(chunks)
    binary = ""

    for i in range(n_chunks):
        if chunks[i] in library6:
            binary += library6[chunks[i]]



    with open(file_name + ".qb6", "wb") as f:
        f.write(binary.encode("ascii"))