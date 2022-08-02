import sys
sys.path.insert(0, 'D:\hasmicro\hari 5\tugas01')
from pesertadidik import Mahasiswa 

class MahasiswaS1(Mahasiswa):
    def __init__(self, nama, alamat, nim,semester,skripsi):
        self.skripsi = skripsi
        super().__init__(nama, alamat,nim,semester)
       

    def __str__(self):
        return '{} || {} || {} || {} || {}'.format(self.nama, self.alamat, self.nim,self.semester,self.skripsi)

alfida = MahasiswaS1('Alfida','Magelang','2021075','Sistem Gis')    
print(alfida)