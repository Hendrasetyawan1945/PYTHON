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

def jamanam():
    return("mencoba fungsi lain")

