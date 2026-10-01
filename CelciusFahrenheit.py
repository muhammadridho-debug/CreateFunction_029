def konversi (nilai, unit):
    if unit == "C":
        return (nilai * 9/5) + 32
    elif unit == "F":    
        return (nilai - 32) * 5/9
    else:
        return "Unit tidak valid"

nilai = float(input("Masukkan nilai: "))
unit = input("Masukkan unit (C/F): ")
print(konversi(nilai, unit))


jarilingkaran = lambda r: 3.14 * r * r
print ("Luas lingkaran adalah: ", jarilingkaran(8))
print ("Luas lingkaran adalah: ", jarilingkaran(4))
