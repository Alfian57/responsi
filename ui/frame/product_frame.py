import tkinter as tk
from tkinter import Frame
from ui.frame.base import Base
from constant.ui_constant import UIConstants as const
from service.product_service import ProductService
from dto.product_dto import ProductDTO


class ProductFrame(Base):

    def __init__(self, master: Frame, product_service: ProductService):
        columns = ["ID Produk", "Nama Produk", "Harga"]
        super().__init__(master, "Manajemen Produk", columns)
        self.product_service = product_service
        self.selected_item = None

        # Placeholder untuk tombol
        self.add_button = None
        self.update_button = None
        self.delete_button = None

    def render(self):
        # Hapus widget sebelumnya
        for widget in self.master.winfo_children():
            widget.destroy()

        # Buat layout dasar
        self.create_layout()

        # Form Tambah/Update Kategori
        form_frame = tk.Frame(self.master)
        form_frame.pack(pady=const.PADDING_MEDIUM, anchor="w")

        # Nama Produk
        product_name_label = tk.Label(
            form_frame,
            text="Nama Produk:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        product_name_label.grid(
            row=0,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        self.product_name_entry = tk.Entry(
            form_frame,
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        self.product_name_entry.grid(
            row=0,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        # Harga Produk
        product_price_label = tk.Label(
            form_frame,
            text="Harga Produk:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        product_price_label.grid(
            row=1,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        self.product_price_entry = tk.Entry(
            form_frame,
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        self.product_price_entry.grid(
            row=1,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=2, columnspan=2, pady=const.PADDING_MEDIUM)

        self.add_button = tk.Button(
            button_frame,
            text="Tambah",
            bg=const.COLOR_ADD_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.add_product,
        )
        self.add_button.pack(side="left", padx=const.PADDING_SMALL)

        self.update_button = tk.Button(
            button_frame,
            text="Perbarui",
            bg=const.COLOR_EDIT_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.update_product,
        )
        self.update_button.pack_forget()

        self.delete_button = tk.Button(
            button_frame,
            text="Hapus",
            bg=const.COLOR_DELETE_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.delete_product,
        )
        self.delete_button.pack_forget()

        # Buat tabel
        products = self.product_service.get_all_products()
        products = [
            (product.id_produk, product.nama_produk, product.harga)
            for product in products
        ]
        self.create_treeview(products)
        self.tree.bind("<<TreeviewSelect>>", self.select_item)

    def select_item(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0], "values")
            if item_data:
                self.selected_item = int(item_data[0])
                self.product_name_entry.delete(0, tk.END)
                self.product_name_entry.insert(0, item_data[1])

                self.product_price_entry.delete(0, tk.END)
                self.product_price_entry.insert(0, item_data[2])

                # Tampilkan tombol Edit dan Delete, sembunyikan Tambah
                self.add_button.pack_forget()
                self.update_button.pack(side="left", padx=const.PADDING_SMALL)
                self.delete_button.pack(side="left", padx=const.PADDING_SMALL)
            else:
                self.reset_buttons()

    def reset_buttons(self):
        self.selected_item = None
        self.product_name_entry.delete(0, tk.END)
        self.product_price_entry.delete(0, tk.END)

        self.update_button.pack_forget()
        self.delete_button.pack_forget()
        self.add_button.pack(side="left", padx=const.PADDING_SMALL)

    def add_product(self):
        product_name = self.product_name_entry.get().strip()
        product_price = self.product_price_entry.get().strip()

        product_dto = ProductDTO(nama_produk=product_name, harga=product_price)
        self.product_service.add_product(product_dto)

        self.reset_buttons()
        self.render()

    def update_product(self):
        product_name = self.product_name_entry.get().strip()
        product_price = self.product_price_entry.get().strip()

        product_dto = ProductDTO(
            id_produk=self.selected_item, nama_produk=product_name, harga=product_price
        )
        self.product_service.update_product(product_dto)

        self.reset_buttons()
        self.render()

    def delete_product(self):
        product_dto = ProductDTO(id_produk=self.selected_item)
        self.product_service.delete_product(product_dto)

        self.reset_buttons()
        self.render()
