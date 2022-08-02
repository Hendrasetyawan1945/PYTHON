class Staff:
    def __init__(self,nama,alamat):
        self.nama = nama
        self.alamat = alamat
       #self.nip = nip
        
    def __str__(self):
        return '{} || {} || {}'.format(self.nama,self.alamat)
    
if __name__ == '__main__':
    jons = Staff ('Jons','Bandung')
    print(jons)
    