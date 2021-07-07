# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 20:12:18 2021

@author: ASUS
"""


lagi='y'

while lagi=='y':

    print("=====================================================================")
    print ("                     PROGRAM MENGHITUNG GAJI KARYAWAN CV. LOGOS    ")
    
    
    print ("")
    nama= input("Masukan nama \t\t:")
    golongan= input("Masukkan golongan \t:")
    jeniskelamin= input("Masukkan jenis kelamin {LAKI-LAKI/PEREMPUAN}:")
    statuskawin= input("masukkan status [KAWIN/BELUM]:")
    anak= input("punya anak [IYA/TIDAK]?:")
    if (golongan=="1"):
        gaji_pokok=2500000
        
    elif (golongan=="2"):
        gaji_pokok=4500000
        
    elif (golongan==""):
        gaji_pokok=6500000
        
        
    if (jeniskelamin=="LAKI-LAKI" and statuskawin=="KAWIN"):
        print ("Tunjangan Istri")
        
        if (golongan=="1"):
            Tunjangan_Istri=gaji_pokok*0.01
            
        elif (golongan=="2"):
            Tunjangan_Istri=gaji_pokok*0.03
            
        elif (golongan=="3"):
            Tunjangan_Istri=gaji_pokok*0.05
    
    
    if (statuskawin=="KAWIN" and anak=="IYA"):
        print ("Tunjangan Anak")
        
    Tunjangan_Anak= gaji_pokok*0.02
    
    Gaji_Bruto= gaji_pokok+Tunjangan_Anak+Tunjangan_Istri
    
    Biaya_Jabatan=Gaji_Bruto*0.005
    
    Iuran_Pensiun=15500
    
    Iuran_Organisasi=3500
    
    Gaji_Netto= Gaji_Bruto-Iuran_Pensiun-Iuran_Organisasi
    
    
    print ("============================================================")
    
    print ("SLIP GAJI")
    
    import datetime
    x = datetime.datetime.now()
    print(x.strftime("%x"))
    
    print ("Nama \t\t: ",nama)
    
    print ("Golongan \t: ",golongan)
    
    print ("Jenis Kelamin \t: ",jeniskelamin)
    
    print ("Status Kawin \t: ",statuskawin)
    
    print ("Gaji Pokok \t: ",gaji_pokok)
    
    print ("Tunjangan Istri \t: ",Tunjangan_Istri)
    
    print ("Tunjangan Anak \t: ",Tunjangan_Anak)
    
    print (">>Gaji Bruto \t: ",Gaji_Bruto)
    
    print ("Biaya Jabatan \t: ",Biaya_Jabatan)
    
    print ("Iuran Pensiun \t: ",Iuran_Pensiun)
    
    print ("Iuran Organisasi \t: ",Iuran_Organisasi)
    
    print (">>Gaji Netto \t: ",Gaji_Netto)
    
    lagi=input("Ambil Data Lagi [y/n]? : ")
    

  





    
    

    




    
    
    
    

    
