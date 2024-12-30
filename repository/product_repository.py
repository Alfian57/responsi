from app.db import DB
from dto.product_dto import ProductDTO


class ProductRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance().get_instance()

    def add(self, product_dto: ProductDTO) -> None:
        sql = f"INSERT INTO {ProductDTO.table_name()} (nama_produk, harga) VALUES (%s, %s)"
        self.db.execute(sql, (product_dto.nama_produk, product_dto.harga))

    def get_all(self) -> list[ProductDTO]:
        sql = f"SELECT id_produk, nama_produk, harga FROM {ProductDTO.table_name()}"
        result = self.db.fetch_all(sql)
        return [
            ProductDTO(
                id_produk=row[0],
                nama_produk=row[1],
                harga=row[2],
            )
            for row in result
        ]

    def get_by_id(self, id: int) -> ProductDTO:
        sql = f"SELECT id_produk, nama_produk, harga FROM {ProductDTO.table_name()} WHERE id_produk = %s"
        result = self.db.fetch_one(sql, (id,))
        return (
            ProductDTO(
                id_produk=result[0],
                nama_produk=result[1],
                harga=result[2],
            )
            if result
            else None
        )

    def update(self, product_dto: ProductDTO) -> None:
        sql = f"UPDATE {ProductDTO.table_name()} SET nama_produk = %s, harga = %s WHERE id_produk = %s"
        self.db.execute(
            sql, (product_dto.nama_produk, product_dto.harga, product_dto.id_produk)
        )

    def delete(self, id: int) -> None:
        sql = f"DELETE FROM {ProductDTO.table_name()} WHERE id_produk = %s"
        self.db.execute(sql, (id,))
