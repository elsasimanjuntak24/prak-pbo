class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        # Atribut instance
        self._nama = nama
        self._stok = stok
        self._harga = harga

        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((self._nama, self._stok, self._harga))

    def lihat_barang(self):
        print(f"Jumlah barang dagangan pada toko: {Dagangan.jumlah_barang} buah")
        for i in range(Dagangan.jumlah_barang):
            print(f"{i + 1}. {Dagangan.list_barang[i][0]} seharga Rp {Dagangan.list_barang[i][2]} (stok: {Dagangan.list_barang[i][1]})")

    def __del__(self):
        print(f"\n{self._nama} dihapus dari toko!")
        Dagangan.jumlah_barang -= 1
        Dagangan.list_barang.remove((self._nama, self._stok, self._harga))

Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)

Dagangan1.lihat_barang()

del Dagangan1
Dagangan2.lihat_barang()
del Dagangan2
del Dagangan3