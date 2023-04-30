'''
Copyright Leonardo Erlacher
All right reserved
'''


import tkinter as tk
from gui import RecordGUI


def run():
    root = tk.Tk()
    app = RecordGUI(root)
    root.mainloop()


if __name__ == '__main__':
    run()
