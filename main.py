import tkinter as tk
from dotenv import load_dotenv
from app.db import DB
from ui.dashboard import Dashboard


# MOHON BACA FILE README.md UNTUK PENJELASAN LEBIH LANJUT


def init():
    load_dotenv()


def main():
    root = tk.Tk()
    Dashboard(root)
    root.mainloop()


def cleanup():
    db = DB.get_instance()
    db.close()


if __name__ == "__main__":
    init()
    main()
    cleanup()
