#latiahan fungsi
#penambahan if

def biasa(tipe, jam='1'):  # argumen  || catatan dalam pemberian nilai default ditaruh sebelah kanan agar tidak terjadi error
    c = 0
    jami = int(jam)
    if tipe == 'mobil':
        c = jami * 2000
    elif tipe == 'motor':
        c = jami * 1000
    else:
        c = 7500
    return c


def langganan(saldo):
    sisa = saldo - 5000
    return sisa


gol = input("masukan gologan : ")
gol1 = gol.strip().replace(" ", "").lower()

if gol1 == 'biasa':

    tipenya = gol = input("masukan tipe kendaraan : ")  # input tipe mobil
    tipe1 = tipenya.strip().replace(" ", "").lower()
    jamnya = input("masukan jam : ")  # input jam || parameter
    if jamnya:
      ongkos = biasa(jamnya, tipe1)
    else:
        ongkos = biasa(tipe1)

    #ongkos = biasa(jam=jamnya, tipe=tipe1)
    #ongkos = biasa(jamnya,tipe1)             #untuk melakukan pembalik parameter || ongkos = biasa(argumen : parameter,agumen)

    print("jenis kendaraan {}".format(tipe1))
    print("total bayar anda : {}".format(ongkos))


elif gol1 == 'langganan':
    saldo = 50000
    salahir = langganan(saldo)
    print("saldo anda {}".format(salahir))
