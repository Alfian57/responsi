from app.db import DB
from dto.transaction_dto import TransactionDTO
from dto.product_dto import ProductDTO


class TransactionRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance().get_instance()

    def add(self, transaction_dto: TransactionDTO) -> None:
        sql = f"INSERT INTO {TransactionDTO.table_name()} (id_produk, jumlah, total_harga, tanggal_transaksi) VALUES (%s, %s, %s, %s)"
        self.db.execute(
            sql,
            (
                transaction_dto.id_produk,
                transaction_dto.jumlah,
                transaction_dto.total_harga,
                transaction_dto.tanggal_transaksi,
            ),
        )

    def get_all(self) -> list[TransactionDTO]:
        sql = f"SELECT id_transaksi, id_produk, jumlah, total_harga, tanggal_transaksi FROM {TransactionDTO.table_name()}"
        result = self.db.fetch_all(sql)
        return [
            TransactionDTO(
                id_produk=row[0],
                jumlah=row[1],
                total_harga=row[2],
                tanggal_transaksi=row[3],
            )
            for row in result
        ]

    def get_all_with_product(self) -> list[TransactionDTO]:
        sql = f"SELECT t.id_transaksi, t.id_produk, t.jumlah, t.total_harga, t.tanggal_transaksi, p.nama_produk, p.harga FROM {TransactionDTO.table_name()} t JOIN produk p ON t.id_produk = p.id_produk"
        result = self.db.fetch_all(sql)
        return [
            TransactionDTO(
                id_transaksi=row[0],
                id_produk=row[1],
                jumlah=row[2],
                total_harga=row[3],
                tanggal_transaksi=row[4],
                produk=ProductDTO(
                    id_produk=row[1],
                    nama_produk=row[5],
                    harga=row[6],
                ),
            )
            for row in result
        ]

    def get_by_id(self, id: int) -> TransactionDTO:
        sql = f"SELECT id_transaksi, id_produk, jumlah, total_harga, tanggal_transaksi FROM {TransactionDTO.table_name()} WHERE id_transaksi = %s"
        result = self.db.fetch_one(sql, (id,))
        return (
            TransactionDTO(
                id_transaksi=result[0],
                id_produk=result[1],
                jumlah=result[2],
                total_harga=result[3],
                tanggal_transaksi=result[4],
            )
            if result
            else None
        )

    def update(self, transaction_dto: TransactionDTO) -> None:
        sql = f"UPDATE {TransactionDTO.table_name()} SET id_produk = %s, jumlah = %s, total_harga = %s, tanggal_transaksi = %s WHERE id_transaksi = %s"
        self.db.execute(
            sql,
            (
                transaction_dto.id_produk,
                transaction_dto.jumlah,
                transaction_dto.total_harga,
                transaction_dto.tanggal_transaksi,
                transaction_dto.id_transaksi,
            ),
        )

    def delete(self, id: int) -> None:
        sql = f"DELETE FROM {TransactionDTO.table_name()} WHERE id_transaksi = %s"
        self.db.execute(sql, (id,))
