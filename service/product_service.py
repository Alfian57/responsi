from repository.product_repository import ProductRepository
from dto.product_dto import ProductDTO
from helper.show_message import display_message
from helper.validator import Validator


class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def get_all_products(self):
        return self.product_repository.get_all()

    def add_product(self, product_dto: ProductDTO):
        error_message = Validator.validate(
            product_dto.__dict__,
            {
                "nama_produk": [Validator.required, Validator.max_length(255)],
                "harga": [
                    Validator.required,
                    Validator.decimal,
                    Validator.positive_integer,
                ],
            },
            {
                "nama_produk": "Nama Produk",
                "harga": "Harga",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        self.product_repository.add(product_dto)
        display_message("Produk berhasil ditambahkan!", "info")

    def update_product(self, product_dto: ProductDTO):
        error_message = Validator.validate(
            product_dto.__dict__,
            {
                "id_produk": [Validator.required],
                "nama_produk": [Validator.required, Validator.max_length(255)],
                "harga": [
                    Validator.required,
                    Validator.decimal,
                    Validator.positive_integer,
                ],
            },
            {
                "id_produk": "ID Produk",
                "nama_produk": "Nama Produk",
                "harga": "Harga",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        self.product_repository.update(product_dto)
        display_message("Produk berhasil diperbarui!", "info")

    def delete_product(self, product_dto: ProductDTO):
        error_message = Validator.validate(
            product_dto.__dict__,
            {
                "id_produk": [Validator.required],
            },
            {
                "id_produk": "ID Produk",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        confirm = display_message(
            "Apakah Anda yakin ingin menghapus produk ini?", "question"
        )
        if not confirm:
            return

        self.product_repository.delete(product_dto.id_produk)
        display_message("Produk berhasil dihapus!", "info")
