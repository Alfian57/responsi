from repository.transaction_repository import TransactionRepository
from repository.product_repository import ProductRepository
from dto.transaction_dto import TransactionDTO
from helper.show_message import display_message
from helper.validator import Validator
from datetime import datetime
from decimal import Decimal
import xlsxwriter


class TransactionService:
    def __init__(self):
        self.transaction_repository = TransactionRepository()
        self.product_repository = ProductRepository()

    def get_all_products(self):
        return self.product_repository.get_all()

    def get_product(self, product_id):
        return self.product_repository.get_by_id(product_id)

    def get_all_transactions(self):
        return self.transaction_repository.get_all_with_product()

    def add_transaction(self, transaction_dto: TransactionDTO):
        error_message = Validator.validate(
            transaction_dto.__dict__,
            {
                "id_produk": [Validator.required, Validator.numeric],
                "jumlah": [
                    Validator.required,
                    Validator.numeric,
                    Validator.positive_integer,
                ],
            },
            {
                "id_produk": "ID Produk",
                "jumlah": "Jumlah",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        transaction_dto.total_harga = transaction_dto.produk.harga * Decimal(
            transaction_dto.jumlah
        )
        transaction_dto.tanggal_transaksi = datetime.now().strftime("%Y-%m-%d")

        self.transaction_repository.add(transaction_dto)
        display_message("Transaksi berhasil ditambahkan!", "info")

    def delete_transaction(self, transaction_dto: TransactionDTO):
        error_message = Validator.validate(
            transaction_dto.__dict__,
            {
                "id_transaksi": [Validator.required],
            },
            {
                "id_transaksi": "ID Transaksi",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        confirm = display_message(
            "Apakah Anda yakin ingin menghapus transaksi ini?", "question"
        )
        if not confirm:
            return

        self.transaction_repository.delete(transaction_dto.id_produk)
        display_message("Transaksi berhasil dihapus!", "info")

    def export_transactions(self):

        transactions = self.transaction_repository.get_all_with_product()
        if not transactions:
            display_message("Tidak ada data transaksi yang dapat diekspor!", "error")
            return

        workbook = xlsxwriter.Workbook("transactions.xlsx")
        worksheet = workbook.add_worksheet()

        headers = ["Nama Produk", "Jumlah", "Total Harga", "Tanggal Transaksi"]
        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header)

        for row_num, transaction in enumerate(transactions, start=1):
            worksheet.write(row_num, 0, transaction.produk.nama_produk)
            worksheet.write(row_num, 1, transaction.jumlah)
            worksheet.write(row_num, 2, str(transaction.total_harga))
            worksheet.write(row_num, 3, transaction.tanggal_transaksi)

        workbook.close()
        display_message(
            "Data transaksi berhasil diekspor ke transactions.xlsx!", "info"
        )
