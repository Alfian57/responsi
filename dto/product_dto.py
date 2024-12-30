class ProductDTO:

    def __init__(self, id_produk=None, nama_produk=None, harga=None):
        self.id_produk = id_produk
        self.nama_produk = nama_produk
        self.harga = harga

    @staticmethod
    def table_name():
        return "produk"
