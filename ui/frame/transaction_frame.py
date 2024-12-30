import tkinter as tk
from tkinter import Frame
from ui.frame.base import Base
from constant.ui_constant import UIConstants as const
from service.transaction_service import TransactionService
from dto.transaction_dto import TransactionDTO
from dto.product_dto import ProductDTO


class TransactionFrame(Base):

    def __init__(self, master: Frame, transaction_service: TransactionService):
        columns = [
            "ID Transaksi",
            "Nama Produk",
            "Harga",
            "Jumlah",
            "Total Harga",
            "Tanggal Transaksi",
        ]
        super().__init__(master, "Manajemen Transaksi", columns)
        self.transaction_service = transaction_service
        self.selected_item = None

        # Placeholder untuk tombol
        self.add_button = None
        self.delete_button = None
        self.edit_button = None

        # Placeholder untuk form
        self.products = self.transaction_service.get_all_products()

        # Mapping dictionaries
        self.products_map = {item.nama_produk: item.id_produk for item in self.products}

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
        product_label = tk.Label(
            form_frame,
            text="Buku:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        product_label.grid(
            row=0,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        product_options = list(self.products_map.keys())
        self.product_var = tk.StringVar(
            value=product_options[0] if product_options else ""
        )
        self.product_dropdown = tk.OptionMenu(
            form_frame, self.product_var, *product_options
        )
        self.product_dropdown.grid(
            row=0,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        # Jumlah Transaksi
        transaction_quantity_label = tk.Label(
            form_frame,
            text="Jumlah:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        transaction_quantity_label.grid(
            row=1,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        self.transaction_quantity_entry = tk.Entry(
            form_frame,
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        self.transaction_quantity_entry.grid(
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
            command=self.add_transaction,
        )
        self.add_button.pack(side="left", padx=const.PADDING_SMALL)

        self.edit_button = tk.Button(
            button_frame,
            text="Edit",
            bg=const.COLOR_EDIT_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.edit_transaction,
        )
        self.edit_button.pack_forget()

        self.delete_button = tk.Button(
            button_frame,
            text="Hapus",
            bg=const.COLOR_DELETE_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.delete_transaction,
        )
        self.delete_button.pack_forget()

        # Export Button
        self.export_button = tk.Button(
            self.master,
            text="Export",
            bg=const.COLOR_ADD_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.export_transactions,
        )
        self.export_button.pack(pady=const.PADDING_SMALL, anchor="w")

        # Buat tabel
        transactions = self.transaction_service.get_all_transactions()
        transactions = [
            (
                transactions.id_transaksi,
                transactions.produk.nama_produk,
                transactions.produk.harga,
                transactions.jumlah,
                transactions.total_harga,
                transactions.tanggal_transaksi,
            )
            for transactions in transactions
        ]
        self.create_treeview(transactions)
        self.tree.bind("<<TreeviewSelect>>", self.select_item)

    def select_item(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0], "values")
            if item_data:
                self.selected_item = int(item_data[0])
                self.product_var.set(item_data[1])

                self.transaction_quantity_entry.delete(0, tk.END)
                self.transaction_quantity_entry.insert(0, item_data[3])

                # Tampilkan tombol Edit dan Delete, sembunyikan Tambah
                self.add_button.pack_forget()
                self.edit_button.pack(side="left", padx=const.PADDING_SMALL)
                self.delete_button.pack(side="left", padx=const.PADDING_SMALL)
            else:
                self.reset_buttons()

    def reset_buttons(self):
        self.selected_item = None
        self.product_var.set(self.product_var.get())
        self.transaction_quantity_entry.delete(0, tk.END)

        self.edit_button.pack_forget()
        self.delete_button.pack_forget()
        self.add_button.pack(side="left", padx=const.PADDING_SMALL)

    def export_transactions(self):
        self.transaction_service.export_transactions()

    def add_transaction(self):
        transaction_product_id = self.products_map.get(self.product_var.get().strip())
        transaction_quantity = self.transaction_quantity_entry.get().strip()

        product = self.transaction_service.get_product(transaction_product_id)

        transaction_dto = TransactionDTO(
            id_produk=transaction_product_id,
            jumlah=transaction_quantity,
            produk=product,
        )
        self.transaction_service.add_transaction(transaction_dto)

        self.reset_buttons()
        self.render()

    def edit_transaction(self):
        transaction_product_id = self.products_map.get(self.product_var.get().strip())
        transaction_quantity = self.transaction_quantity_entry.get().strip()

        product = self.transaction_service.get_product(transaction_product_id)

        transaction_dto = TransactionDTO(
            id_transaksi=self.selected_item,
            id_produk=transaction_product_id,
            jumlah=transaction_quantity,
            produk=product,
        )
        self.transaction_service.update_transaction(transaction_dto)

        self.reset_buttons()
        self.render()

    def delete_transaction(self):
        transaction_dto = TransactionDTO(id_produk=self.selected_item)
        self.transaction_service.delete_transaction(transaction_dto)

        self.reset_buttons()
        self.render()
