class Dagangan:
  jumlah_barang = 0
  list_barang = []

  def __init__(self, nama, stok, harga):
      self.__nama = nama
      self.__stok = stok
      self.__harga = harga

      Dagangan.list_barang.append((self.__nama, self.__stok, self.__harga))
      Dagangan.jumlah_barang += 1

  @classmethod
  def lihat_barang(cls):
      print("Jumlah barang dagangan pada toko:", cls.jumlah_barang, "buah")
      for i, barang in enumerate(cls.list_barang, start=1):
          nama, stok, harga = barang
          print(f"{i}. {nama} seharga Rp {harga} (stok: {stok})")

  def __del__(self):
      Dagangan.list_barang = [(nama, stok, harga) for nama, stok, harga in Dagangan.list_barang if nama != self.__nama]
      Dagangan.jumlah_barang -= 1
      print(f"{self.__nama} dihapus dari toko!")


Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)

Dagangan.lihat_barang()
del Dagangan1
Dagangan.lihat_barang()