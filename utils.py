from tkinter import filedialog


def ce(x):
    if isinstance(x, (bytes, bytearray)):
        first = x[:1]
        return 5 if first == b"0" else 6

    x = str(x)
    return 5 if x.startswith("0") else 6

def choice(x, y, window):
    z = "c" + x
    globals()[z] = y
    window.destroy()


def browse(kind):
    if kind == "Text":
        kindx = kind
        ex = "txt"
        mode = "r"

    else:
        kindx = "Quantum Being"
        ex = "qb*"
        mode = "rb"

    filename = filedialog.askopenfilename(
        title=f"Select {kindx} File",
        filetypes=[(f"{kindx} Files", f"*.{ex}")]
    )

    if not filename:
        return None

    if mode == "r":
        with open(filename, mode, encoding="utf-8") as f:
            r_data = f.read()
        return 5, r_data.encode("utf-8")

    with open(filename, mode) as f:
        r_data = f.read()

    edition = ce(r_data)
    u_data = r_data[1:]
    return edition, u_data
