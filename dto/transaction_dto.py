class TransactionDTO:
    def __init__(
        self,
        id_transaksi=None,
        id_produk=None,
        total_harga=None,
        tanggal_transaksi=None,
    ):
        self.id_transaksi = id_transaksi
        self.id_produk = id_produk
        self.total_harga = total_harga
        self.tanggal_transaksi = tanggal_transaksi

    @staticmethod
    def table_name():
        return "transaksi"
