daftar_semua_kursus = [
    {
        "nama": "Pemrograman Python",
        "kuota": 10
    },
    {
        "nama": "Pemrograman Java",
        "kuota": 0
    },
    {
        "nama": "Pemrograman C++",
        "kuota": 15
    },
    {
        "nama": "Pemrograman C",
        "kuota": 6
    },
]
kursus_pengguna = []
maks_kursus = 3
lanjut = True


print(f"\n=== Pendaftaran Kursus Coding ===\n")

while len(kursus_pengguna) < maks_kursus and lanjut == True: 
    print("--- Silahkan pilih kursus yang tersedia ---")
    for nomor, kursus in enumerate(daftar_semua_kursus):
        nama_kursus = kursus["nama"]
        kuota_kursus = kursus["kuota"]

        if kuota_kursus > 0:
            print(f'{nomor + 1}. {nama_kursus}, (sisa kuota: {kuota_kursus})')
        else:
            print(f'{nomor + 1}. {nama_kursus}, (kuota penuh❌)')

    while True:
        try:
            kursus_yang_diminati = int(input("\nPilihan anda (cukup ketik nomornya saja): "))
            nomor = kursus_yang_diminati
            if nomor < 1 or nomor > len(daftar_semua_kursus):
                print(f'Nomor harus diantara 1 dan {len(daftar_semua_kursus)}')
                continue
            else:
                break
        except:
            print("Input harus berupa angka!")
            continue

    if kursus_yang_diminati == 1:
        if (daftar_semua_kursus[0]["kuota"]) > 0 and (daftar_semua_kursus[0]) not in kursus_pengguna:
            kursus_pengguna.append(daftar_semua_kursus[0])
            daftar_semua_kursus[0]["kuota"] -= 1
            print(f"Selamat! Pendaftaran untuk {daftar_semua_kursus[0]["nama"]} berhasil. ✅")
        else:
            if (daftar_semua_kursus[0]["kuota"]) <= 0:
                print("Kuota telah penuh❌")
            else:
                print("Anda sudah masuk ke kursus ini")
    if kursus_yang_diminati == 2:
        if (daftar_semua_kursus[1]["kuota"]) > 0 and (daftar_semua_kursus[1]) not in kursus_pengguna:
            kursus_pengguna.append(daftar_semua_kursus[1])
            daftar_semua_kursus[1]["kuota"] -= 1
            print(f"Selamat! Pendaftaran untuk {daftar_semua_kursus[1]["nama"]} berhasil. ✅")
        else:
            if (daftar_semua_kursus[1]["kuota"]) <= 0:
                print("Kuota telah penuh❌")
            else:
                print("Anda sudah masuk ke kursus ini")
    if kursus_yang_diminati == 3:
        if (daftar_semua_kursus[2]["kuota"]) > 0 and (daftar_semua_kursus[2]) not in kursus_pengguna:
            kursus_pengguna.append(daftar_semua_kursus[2])
            daftar_semua_kursus[2]["kuota"] -= 1
            print(f"Selamat! Pendaftaran untuk {daftar_semua_kursus[2]["nama"]} berhasil. ✅")
        else:
            if (daftar_semua_kursus[2]["kuota"]) <= 0:
                print("Kuota telah penuh❌")
            else:
                print("Anda sudah masuk ke kursus ini")
    if kursus_yang_diminati == 4:
        if (daftar_semua_kursus[3]["kuota"]) > 0 and (daftar_semua_kursus[3]) not in kursus_pengguna:
            kursus_pengguna.append(daftar_semua_kursus[3])
            daftar_semua_kursus[3]["kuota"] -= 1
            print(f"Selamat! Pendaftaran untuk {daftar_semua_kursus[3]["nama"]} berhasil. ✅")
        else:
            if (daftar_semua_kursus[3]["kuota"]) <= 0:
                print("Kuota telah penuh❌")
            else:
                print("Anda sudah masuk ke kursus ini")
    
    while True:
        if len(kursus_pengguna) < maks_kursus:
            daftar_lagi = input("apakah ingin daftar kursus lain?(y/n): ")
            if daftar_lagi == 'y':
                lanjut = True
                break
            elif daftar_lagi == 'n':
                lanjut = False
                break
            else:
                print("WARNING! Input harus y/n")
        else:
            break

print('--- Proses Pendaftaran Selesai ---')

if len(kursus_pengguna) >= maks_kursus:
    print("NOTE : Anda telah mencapai batas maksimal kursus yang boleh diikuti")

print(f"Kursus yang anda ambil: ")

for i, kursus in enumerate(kursus_pengguna):
    nama_kursus = kursus["nama"]
    print(f'{i + 1}. {nama_kursus}')
    
print('---Terima kasih telah mendaftar kursus kami ---')