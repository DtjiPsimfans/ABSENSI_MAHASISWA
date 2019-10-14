import sys
import random
import pickle


class Mahasiswa:
    """
    Class ini mengandung atribut seorang mahasiswa.
    """

    def __init__(self, nama, alamat):
        # type: (str) -> None
        self.id: str = "D00" + str(random.randint(1000000, 9999999))
        self.nama: str = nama
        self.alamat: str = alamat
        self.data_absensi: DataAbsensi = DataAbsensi()

    def __str__(self):
        # type: () -> str
        hasil: str = ""  # nilai semula
        hasil += "ID: " + str(self.id) + "\n"
        hasil += "Nama: " + str(self.nama) + "\n"
        hasil += "Alamat: " + str(self.alamat) + "\n"
        hasil += "Di bawah ini data absensi mahasiswa ini.\n"
        hasil += str(self.data_absensi) + "\n"
        return hasil


class DataAbsensi:
    """
    Class ini mengandung atribut data absensi mahasiswa.
    """

    def __init__(self):
        # type: () -> None
        self.__jumlah_hadir: int = 0  # nilai semula
        self.__jumlah_sakit: int = 0  # nilai semula
        self.__jumlah_ijin: int = 0  # nilai semula
        self.__jumlah_bolos: int = 0  # nilai semula

    def get_jumlah_hadir(self):
        # type: () -> int
        return self.__jumlah_hadir

    def get_jumlah_sakit(self):
        # type: () -> int
        return self.__jumlah_sakit

    def get_jumlah_ijin(self):
        # type: () -> int
        return self.__jumlah_ijin

    def get_jumlah_bolos(self):
        # type: () -> int
        return self.__jumlah_bolos

    def tambah_hadir(self):
        # type: () -> None
        self.__jumlah_hadir += 1

    def tambah_sakit(self):
        # type: () -> None
        self.__jumlah_sakit += 1

    def tambah_ijin(self):
        # type: () -> None
        self.__jumlah_ijin += 1

    def tambah_bolos(self):
        # type: () -> None
        self.__jumlah_bolos += 1

    def __str__(self):
        # type: () -> str
        hasil: str = ""  # nilai semula
        hasil += "Jumlah hadir: " + str(self.__jumlah_hadir) + "\n"
        hasil += "Jumlah sakit: " + str(self.__jumlah_sakit) + "\n"
        hasil += "Jumlah ijin: " + str(self.__jumlah_ijin) + "\n"
        hasil += "Jumlah bolos: " + str(self.__jumlah_bolos) + "\n"
        return hasil


def main():
    """
    Fungsi ini dipakai untuk run program.
    :return:
    """

    daftar_mahasiswa: list
    filename: str = "Data Absensi Mahasiswa"
    try:
        daftar_mahasiswa = pickle.load(open(filename, "rb"))
    except FileNotFoundError:
        daftar_mahasiswa = []

    print("Tekan 1 untuk menambah mahasiswa baru.")
    print("Tekan 2 untuk menghapus mahasiswa.")
    print("Tekan 3 untuk mengupdate data absensi seorang mahasiswa.")
    print("Tekan 4 untuk menyimpan data absensi lalu keluar.")
    opsi: int = int(input("Tolong masukkan angka: "))
    while opsi < 1 or opsi > 4:
        opsi: int = int(input("Maaf, input tidak sah! Tolong masukkan angka: "))

    while opsi != 4:
        if opsi == 1:
            print("Tolong masukkan informasi mengenai mahasiswa baru yang mau Anda tambahkan.")
            nama: str = input("Tolong masukkan nama mahasiswa: ")
            alamat: str = input("Tolong masukkan alamat mahasiswa: ")
            mahasiswa_baru: Mahasiswa = Mahasiswa(nama, alamat)
            daftar_mahasiswa.append(mahasiswa_baru)

        elif opsi == 2:
            print("Berikut data absensi para mahasiswa yang Anda punya: \n")
            for mahasiswa in daftar_mahasiswa:
                print(mahasiswa)

            daftar_id: list = [daftar_mahasiswa[i].id for i in range(len(daftar_mahasiswa))]
            id: str = input("Tolong masukkan ID dari mahasiswa yang mau Anda hapus: ")
            while id not in daftar_id:
                id: str = input("ID tidak tersedia! Tolong masukkan ID dari mahasiswa yang mau Anda hapus: ")

            curr_mahasiswa: Mahasiswa or None = None  # nilai semula
            for mahasiswa in daftar_mahasiswa:
                if mahasiswa.id == id:
                    curr_mahasiswa = mahasiswa
                    break

            daftar_mahasiswa.remove(curr_mahasiswa)

        elif opsi == 3:
            print("Berikut data absensi para mahasiswa yang Anda punya: \n")
            for mahasiswa in daftar_mahasiswa:
                print(mahasiswa)

            daftar_id: list = [daftar_mahasiswa[i].id for i in range(len(daftar_mahasiswa))]
            id: str = input("Tolong masukkan ID dari mahasiswa yang mau Anda update data absensinya: ")
            while id not in daftar_id:
                id: str = input("ID tidak tersedia! Tolong masukkan ID dari mahasiswa yang mau Anda update data "
                                "absensinya: ")

            curr_mahasiswa: Mahasiswa or None = None  # nilai semula
            for mahasiswa in daftar_mahasiswa:
                if mahasiswa.id == id:
                    curr_mahasiswa = mahasiswa
                    break

            daftar_pilihan: list = ["HADIR", "SAKIT", "IJIN", "BOLOS"]
            data_kehadiran: str = input("Apakah dia HADIR, SAKIT, IJIN, atau BOLOS? ")
            while data_kehadiran.upper() not in daftar_pilihan:
                data_kehadiran: str = input("Maaf, input tidak sah! Apakah dia HADIR, SAKIT, IJIN, atau BOLOS? ")

            fungsi = getattr(curr_mahasiswa.data_absensi, "tambah_" + str(data_kehadiran).lower())
            fungsi()

        opsi: int = int(input("Tolong masukkan angka: "))
        while opsi < 1 or opsi > 4:
            opsi: int = int(input("Maaf, input tidak sah! Tolong masukkan angka: "))

    print("Berikut data absensi para mahasiswa yang Anda punya: \n")
    for mahasiswa in daftar_mahasiswa:
        print(mahasiswa)

    pickle.dump(daftar_mahasiswa, open(filename, "wb"))
    sys.exit()


if __name__ == "__main__":
    main()
