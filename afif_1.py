import mysql.connector
from prettytable import PrettyTable
import random
import time

class DataVaksin:

    def __init__(self):
        self.db = mysql.connector.connect (
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'vaksin'
        )

    def DataPenerima(self,val):
        cursor = self.db.cursor()
        sql = "INSERT INTO datavaksin (nama,umur,gender,kota) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql,val)
        self.db.commit()
        print("Data Berhasil Dimasukan! ")

    def DataVakman(self,val):
        cursor = self.db.cursor()
        sql = "INSERT INTO vakman (instansi,nama,umur,gender,kota,vaksin) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,val)
        self.db.commit()
        print("Data Berhasil Dimasukan! ")

    def Info(self):
        table = PrettyTable()

        table.field_names = ['Nama','Efektivitas di Indonesia','Jumlah']
        table.add_rows(
            [
            ["Astrazeneca", "76%","8.000.000"],
            ["Moderna","69.5%","30.000.00"],
            ["Sinopharm", "79.84%","7.500.000"],
            ["Sinovac", "64%","40.000.000"],
            ]
            
        )
        print(table)

    def showPenerima(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM datavaksin"
        cursor.execute(sql)
        result = cursor.fetchall()
        
        table = PrettyTable()

        table.field_names = ['ID', 'NAMA', 'UMUR', 'GENDER', 'KOTA']

        for x in result:
            table.add_row(list(x))
        print(table)

    def showVakman(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM vakman"
        cursor.execute(sql)
        result = cursor.fetchall()
        
        table = PrettyTable()

        table.field_names = ['ID', 'INSTANSI', 'NAMA', 'UMUR', 'GENDER', 'KOTA', 'VAKSIN']

        for x in result:
            table.add_row(list(x))
        print(table)

class Penerima:

    def __init__(self):
        self.dv = DataVaksin()
        self.cursor = self.dv.db.cursor()
    
    def Person0(self):
        while True:
            try:
                pertanyaan1 = input("Apakah Anda Pernah Terkena Covid-19 Dalam 3 Bulan Terakhir ? (Y/N) : ")
                assert pertanyaan1 == "Y" or pertanyaan1 == "N"
                if pertanyaan1 == "Y":
                    exit("Tidak Dapat Melanjutkan Vaksinasi Covid-19")
                elif pertanyaan1 == "N":
                    pertanyaan2 = input("Apakah Anda Bertekanan Darah 180/110 atau lebih ? (Y/N) : ")
                    assert pertanyaan2 == "Y" or pertanyaan2 == "N"
                    if pertanyaan2 == "Y":
                        exit("Tidak Dapat Melanjutkan Vaksinasi Covid-19")
                    elif pertanyaan2 == "N":
                        pertanyaan3 = input("Apakah Anda Sedang Hamil ? (Y/N) : ")
                        assert pertanyaan3 == "Y" or pertanyaan3 == "N"
                        if pertanyaan3 == "Y":
                            exit("Tidak Dapat Melanjutkan Vaksinasi Covid-19")
                        elif pertanyaan3 == "N":
                            pertanyaan4 = input("Apakah Anda Mengalami Gejala ISPA, seperti batuk/pilek/sesak napas dalam 7 hari terakhir ? (Y/N) : ")
                            assert pertanyaan4 == "Y" or pertanyaan4 == "N"
                            if pertanyaan4 =="Y":
                                exit("Tidak Dapat Melanjutkan Vaksinasi Covid-19")
                            elif pertanyaan4 == "N":
                                pertanyaan5 = input("Apakah Anda Aktif Terapi Jangka Panjang Terhadap Penyakit Darah ? (Y/N) : ")
                                assert pertanyaan5 == "Y" or pertanyaan5 == "N"
                                if pertanyaan5 == "Y":
                                    exit("Tidak Dapat Melanjutkan Vaksinasi Covid-19")
                                elif pertanyaan5 == "N":
                                    pertanyaan6 = input("Apakah Ada Anggota Keluarga Yang Memiliki Kontak Erat/Suspek/Terkonfirmasi Sedang Dalam Perawatan Covid-19 ? (Y/N) : ")
                                    assert pertanyaan6 == "Y" or pertanyaan6 == "N"
                                    if pertanyaan6 == "Y":
                                        exit("Tidak Dapat Melanjutkan Vaksinasi Covid-19")
                                    elif pertanyaan6 == "N":
                                        pertanyaan7 = input("Apakah Anda Menderita Penyakit Autoimun Sistemik (SLE/Lupus,Sjorgen,Vaskultis) akut ? (Y/N) : ")
                                        assert pertanyaan7 == "Y" or pertanyaan7 == "N"
                                        if pertanyaan7 == "Y":
                                            exit("Tidak Dapat Melanjutkan Vaksinasi Covid-19")
                                        elif pertanyaan7 == "N":
                                            pertanyaan8 = input("Apakah Anda Menderita Penyakit Saluran Pencernaan Kronis ? (Y/N) : ")
                                            assert pertanyaan8 == "Y" or pertanyaan8 == "N"
                                            if pertanyaan8 == "Y":
                                                exit("Tidak Dapat Melanjutkan Vaksinasi Covid-19")
                                            elif pertanyaan8 == "N":
                                                pertanyaan9 = input("Apakah Anda Menderita HIV Dengan Angka CD4 kurang dari 200 atau Tidak Diketahui ? (Y/N) : ")
                                                if pertanyaan9 == "Y":
                                                    exit("Tidak Dapat Melanjutkan Vaksinasi Covid-19")
                                                elif pertanyaan9 == "N":
                                                    pertanyaan10 = input("Apakah Anda Menderita Penyakit Hiperteroid atau Hiperteroid Karena Imun ? (Y/N) : ")
                                                    assert pertanyaan10 == "Y" or pertanyaan10 == "N"
                                                    if pertanyaan10 == "Y":
                                                        exit("Tidak Dapat Melanjutkan Vaksinasi Covid-19")
                                                    elif pertanyaan10 == "N":
                                                        pertanyaan11 = input("Apakah Anda Menderita Penyakit Reumatik Autoimun atau Rhematoid Arthritis Akut ? (Y/N) : ")
                                                        assert pertanyaan11 == "Y" or pertanyaan11 == "N"
                                                        if pertanyaan11 == "Y":
                                                            exit("Tidak Dapat Melanjutkan Vaksinasi Covid-19")
                                                        elif pertanyaan11 == "N":
                                                            print("\nSilahkan Untuk Melanjutkan Proses Pendaftaran Vaksinasi Covid-19")
                                                            break

            except AssertionError:
                print("Harus Memasukkan Inputan Yang Sesuai")
            
    def Person(self):
        print("")
        nama = input("Masukkan Nama: ")
        umur = int(input("Masukkan Umur: "))
        gender = input("Masukkan Gender: ")
        kota = input("Masukkan Kota: ")

        val = (nama,umur,gender,kota)
        self.dv.DataPenerima(val)

    def PersonVaksinMandiri(self):
        print("")
        tanya1 = input("Apakah Instansi / Perusahaan Anda Sekarang Mengikuti Kerja Sama Program Vaksin Mandiri ? (Y/N)")
        if tanya1 == "Y":
            print("\nSilahkan Untuk Melanjutkan Proses Pendaftaran Vaksinasi Covid-19 Mandiri")
        elif tanya1 == "N":
            print("Tidak Dapat Melanjutkan Pendaftaran Vaksinasi Covid-19 Mandiri")
        else:
            print("Harus Memasukkan Inputan Yang Sesuai")
                    
        instansi = input("Masukkan Nama Instansi Anda : ")
        nama = input("Masukkan Nama : ")
        umur = int(input("Masukkan Umur : "))
        gender = input("Masukkan Gender : ")
        kota = input("Masukkan Kota : ")
        vaksin = input("Pilih Vaksin : ")
            
        val = (instansi,nama,umur,gender,kota,vaksin)
        self.dv.DataVakman(val)

        hari = ["Senin (03/01/2022)","Selasa(04/01/2022)","Rabu(05/01/2022)","Kamis(06/01/2022)"]
        hari2 = ["Senin(31/01/2022)","Selasa(01/02/2022)","Rabu(02/02/2022)","Kamis(03/02/2022)"]
        jam = ["07:30","08:00","09:00"]
        jam2 = ["07:30","08:00","09:00"]
        print(f"Anda Akan Divaksin Tahap 1 Pada Hari {random.choice(hari)} pada jam {random.choice(jam)}")
        print(f"Anda Akan Divaksin Tahap 2 Pada Hari {random.choice(hari2)} pada jam {random.choice(jam2)}")
    
    def payment(self,total):
        print("Pilih Metode Pembayaran")
        print("1.Gopay")
        print("2.BPJS")
        print("3.Bank (Virtual Account)")
        payment = int(input("Masukkan Pilihan Payment: "))
        if payment == 1:
            saldo = int(input("Masukkan Saldo:"))
            if saldo < total:
                print("Maaf Saldo Anda Tidak Mencukupi")
            else:
                time.sleep(2)
                print(f"Pembayaran Sukses Dengan Gopay Sisa Saldo {saldo - total}")
        elif payment == 2:
            fotokopi = input("Apakah Anda Membawa Fotokopi BPJS 3 Rangkap (Y/N): ")
            if fotokopi == "Y":
                if total > 500000:
                    time.sleep(4)
                    print("Mohon Maaf Untuk klaim diatas 500 ribu tidak ditanggung oleh BPJS :)")
                    print(f"Harga Vaksin Anda senilai {total}")
                    print(f"Silahkan Bayar dengan metode lain. Terima Kasih")
                else:
                    print("Klaim BPJS Sedang Di Proses Harap Menunggu ...")
                    time.sleep(10)
                    print(f"Pembayaran Vaksin Akan Ditanggung Oleh BPJS Keternagakerjaan senilai {total}")
            elif fotokopi == "N":
                print("Silahkan Fotokopi BPJS di fotokopi terdekat! ")
        elif payment == 3:
            bank = input("Masukkan bank: ")
            saldo = int(input("Masukkan Saldo:"))
            if saldo < total:
                print("Maaf Saldo Anda Tidak Mencukupi")
            else:
                time.sleep(2)
                print(f"Pembayaran Sukses Dengan {bank} Sisa Saldo {saldo - total}")
    
    def TagihanVaksinMandiri(self):
        Astrazeneca = 1100000
        Moderna = 900000
        Sinopharm = 750000
        Sinovac = 600000

        nama = input("Masukkan Nama Anda : ")
        self.cursor.execute("SELECT nama,vaksin FROM vakman WHERE nama = %s LIMIT 1",(nama,))
        result = self.cursor.fetchone()

        if result is None:
            print("Nama peserta tidak ada! ")
        elif nama in result:
            if result[1] == "Astrazeneca":
                total = Astrazeneca
                print(f"Total Tagihan Vaksin Anda sebanyak {total}")
                self.payment(total)
            elif result[1] == "Moderna":
                total = Moderna
                print(f"Total Tagihan Vaksin Anda sebanyak {total}")
                self.payment(total)
            elif result[1] == "Sinopharm":
                total = Sinopharm
                print(f"Total Tagihan Vaksin Anda sebanyak {total}")
                self.payment(total)
            elif result[1] == "Sinovac":
                total = Sinovac
                print(f"Total Tagihan Vaksin Anda sebanyak {total}")
                self.payment(total)

    def KuotaVaksin1(self):
        hari = ["Senin (03/01/2022)","Selasa(04/01/2022)","Rabu(05/01/2022)","Kamis(06/01/2022)"]
        jam = ["10:00","13:00","15:00"]
        vaksint =["Astrazeneca","Sinopharm","Sinovac"] 
        nama = input("Masukkan Nama: ")
        self.cursor.execute("SELECT nama FROM datavaksin WHERE nama = %s LIMIT 1",(nama,))
        result = self.cursor.fetchone()

        if result is None:
            print("Peserta Vaksin Tidak Terdaftar!")
        elif result:
            print(f"{nama} Terdaftar Sebagai Penerima ")
            agreement = input("Apakah Anda Bersedia di Vaksinasi Tahap 1? (Y/N)")
            if agreement == "Y":
                print(f"Anda Akan Divaksin Pada Hari {random.choice(hari)} pada jam {random.choice(jam)}")
                print(f"Anda Akan Divaksin Dengan {random.choice(vaksint)}")
            elif agreement == "N":
                print("Anda Tidak Di Vaksin Tahap 1")
                
    def KuotaVaksin2(self):
        hari = ["Senin(31/01/2022)","Selasa(01/02/2022)","Rabu(02/02/2022)","Kamis(03/02/2022)"]
        jam = ["10:00","13:00","15:00"]
        nama = input("Masukkan Nama: ")
        self.cursor.execute("SELECT nama FROM datavaksin WHERE nama = %s LIMIT 1",(nama,))
        result = self.cursor.fetchone()

        if result is None:
            print("Peserta Vaksin Tidak Terdaftar!")
        elif result:
            print(f"{nama} Terdaftar Sebagai Penerima Vaksin Tahap 2 ")  
            print("Anda Telah Di Vaksin tahap 1")
            print(f"Anda Akan Divaksin Pada Hari {random.choice(hari)} pada jam {random.choice(jam)}")

    def infovaksinsasi(self):
        baca = open("Info Vaksinasi Covid-19.txt","r")

        baca2 = baca.read()
        print(baca2)
        baca.close()

    def infovaksinmandiri(self):
        baca2 = open("Vaksin Mandiri.txt","r")

        baca3 = baca2.read()
        print(baca3)
        baca2.close()

        
    def main(self):
        print("\tSELAMAT DATANG DI PROGRAM VAKSINASI COVID-19")
        while True:
            print("""
            1.Daftar Program Vaksin Pemerintah
            2.Lihat Data Vaksin
            3.Lihat Data Penerima Vaksin
            4.Vaksin Tahap 1
            5.Vaksin Tahap 2
            6.Pendaftaran Vaksin Mandiri
            7.Tagihan Vaksin Mandiri
            8.Database Vaksin Mandiri
            9.Info Umum Seputar Vaksinasi Covid-19
            10.Info Seputar Vaksinasi Covid-19 Mandiri (Khusus Instansi / Perusahaan Tertentu)
            0.Exit
            """)

            menu = int(input("Masukkan Menu : "))

            if menu == 1:
                self.Person0()
                self.Person()
            elif menu == 2:
                self.dv.Info()
            elif menu == 3:
                self.dv.showPenerima()
            elif menu == 4:
                self.KuotaVaksin1()
            elif menu == 5:
                self.KuotaVaksin2()
            elif menu == 6:
                self.Person0()
                self.PersonVaksinMandiri()
            elif menu == 7:
                self.TagihanVaksinMandiri()
            elif menu == 8:
                self.dv.showVakman()
            elif menu == 9:
                self.infovaksinsasi()
            elif menu == 10:
                self.infovaksinmandiri()
            elif menu == 0:
                print("Terima Kasih Sudah Menggunakan Program Vaksinasi Covid-19")
                break
            else:
                print("Tolong Input Sesuai Angka Yang Tersedia !")

if __name__ == "__main__":
    p1 = Penerima()
    p1.main()