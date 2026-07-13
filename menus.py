import tkinter as tk
from utils import browse

def choice(x, y, window):
    z = "c" + x
    globals()[z] = y
    window.destroy()


def menu(x):
    if x == 0:
        root_0 = tk.Tk()
        root_0.title("What is it that you want to do?")

        btn1 = tk.Button(root_0, text="Encode", command=lambda: choice("0", "encode", root_0))
        btn1.pack(pady=10)

        btn2 = tk.Button(root_0, text="Decode", command=lambda: choice("0", "decode", root_0))
        btn2.pack(pady=10)
    
        root_0.mainloop()

        from coder import decode, encode

        if "c0" not in globals():
            return
        
        if c0 == "decode":
            decode()
        else:
            encode()
            
    elif x == 1:
        root_1 = tk.Tk()
        root_1.title("What type of input you have?")

        btn1 = tk.Button(root_1, text="Text To Be Typed", command=lambda: choice("1", "Text To Be Typed", root_1))
        btn1.pack(pady=10)

        btn2 = tk.Button(root_1, text="File", command=lambda: choice("1", "File", root_1))
        btn2.pack(pady=10)
        root_1.mainloop()

        if "c1" not in globals():
            return None
        
        if c1 == "File":
            return "File"

        return c1
            
    elif x == 2:
        root_2 = tk.Tk()
        root_2.title("Enter some text")

        tk.Label(root_2, text="Type something:").pack(pady=5)

        entry = tk.Entry(root_2, width=30)
        entry.pack(pady=5)

        tk.Button(root_2, text="Submit", command=lambda: choice("2", entry.get(), root_2)).pack(pady=10)

        root_2.mainloop()

        if "c2" not in globals():
            return None

        return c2
    
    elif x == 3:
        root_3 = tk.Tk()
        root_3.title("Choose File Name")

        tk.Label(root_3, text="Desired file name:").pack(pady=5)

        entry = tk.Entry(root_3, width=30)
        entry.pack(pady=5)

        tk.Button(root_3, text="Submit", command=lambda: choice("3", entry.get(), root_3)).pack(pady=10)

        root_3.mainloop()

        return c3