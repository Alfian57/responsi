import tkinter as tk
from tkinter import Tk
from ui.component.sidebar import Sidebar
from constant.ui_constant import UIConstants as const
from service.product_service import ProductService
from service.transaction_service import TransactionService
from ui.frame.product_frame import ProductFrame
from ui.frame.transaction_frame import TransactionFrame


class Dashboard:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Sistem Kasir Sederhana")
        self.root.geometry(f"{const.WINDOW_WIDTH}x{const.WINDOW_HEIGHT}")

        # Setup main layout
        self.main_frame = tk.Frame(
            self.root,
            bg=const.COLOR_MAIN_BG,
            width=const.WINDOW_WIDTH - const.SIDEBAR_WIDTH,
            height=const.WINDOW_HEIGHT,
        )
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.setup_services()
        self.setup_sidebar()

    def setup_services(self):
        self.product_service = ProductService()
        self.transaction_service = TransactionService()

    def setup_sidebar(self):
        self.show_products()
        menu_commands = {
            "Produk": self.show_products,
            "Transaksi": self.show_transactions,
        }

        sidebar = Sidebar(self.root, menu_commands)
        sidebar.create()

    def show_products(self):
        product_frame = ProductFrame(self.main_frame, self.product_service)
        product_frame.render()

    def show_transactions(self):
        transaction_frame = TransactionFrame(self.main_frame, self.transaction_service)
        transaction_frame.render()
