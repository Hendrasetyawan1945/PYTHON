#latiahan fungsi
#penambahan if

from biasaaja import biasa
from langgananf import langganan


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
