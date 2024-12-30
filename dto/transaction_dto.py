from dto.product_dto import ProductDTO


class TransactionDTO:

    def __init__(
        self,
        id_transaksi=None,
        id_produk=None,
        jumlah=None,
        total_harga=None,
        tanggal_transaksi=None,
        produk: ProductDTO = None,
    ):
        self.id_transaksi = id_transaksi
        self.id_produk = id_produk
        self.jumlah = jumlah
        self.total_harga = total_harga
        self.tanggal_transaksi = tanggal_transaksi
        self.produk = produk

    @staticmethod
    def table_name():
        return "transaksi"
