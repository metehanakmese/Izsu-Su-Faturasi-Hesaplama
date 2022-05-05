CTV_TON_BASINA_UCRET=0.39
KDV_ORANI=0.08
AYLIK_GUN=30
KATI_ATIK_BERTARAF_UCRETI_SABITI=2.54
BIRINCI_KADEME_TON_MIKTARI_SINIRI=13
IKINCI_KADEME_TON_MIKTARI_SINIRI=20
KATI_ATIK_UCRET_SABITI=13
ABONE_BIR_BIRINCI_KADEME_STBU=2.89   # STBU = Su Tüketim Birim Ücreti
ABONE_BIR_BIRINCI_KADEME_ASBU=1.44   # ASBU = Atık Su Birim Ücreti
ABONE_BIR_IKINCI_KADEME_STBU=3.13
ABONE_BIR_IKINCI_KADEME_ASBU=1.56
ABONE_BIR_UCUNCU_KADEME_STBU=6.43
ABONE_BIR_UCUNCU_KADEME_ASBU=3.22
ABONE_IKI_STBU=7.38
ABONE_IKI_ASBU=3.68
ABONE_UC_STBU=4.34
ABONE_UC_ASBU=2.16
ABONE_DORT_STBU=5
ABONE_DORT_ASBU=2.5
ABONE_BES_BIRINCI_KADEME_STBU=1.45
ABONE_BES_BIRINCI_KADEME_ASBU=0.72
ABONE_BES_IKINCI_KADEME_STBU=2.89
ABONE_BES_IKINCI_KADEME_ASBU=1.44
ABONE_BES_UCUNCU_KADEME_STBU=6.43
ABONE_BES_UCUNCU_KADEME_ASBU=3.22
def sayi_al(alt_sinir,ust_sinir):  # Kullanıcının girmesi gereken sayı aralığının kontrolünü sağlayan fonksiyon
    sayi=int(input())
    while sayi<alt_sinir  or sayi>ust_sinir:
        sayi=int(input("Hatalı giriş! Lütfen tekrar giriniz: "))
    return sayi
def ctv_hesaplama(kullanilan_ton):  # Çevre Temizlik Vergisini Hesaplayan Fonksiyon #
    return (kullanilan_ton*CTV_TON_BASINA_UCRET)
def kdv_hesaplama(ucret):  # KDV oranını hesaplar
    return (ucret*KDV_ORANI)
def kati_atik_toplama_bedeli_hesaplama(hane_sayisi): # Katı atık toplama bedelini hesaplar
    return (hane_sayisi*KATI_ATIK_UCRET_SABITI)
def kati_atik_bertaraf_ucreti_hesaplama(hane_sayisi): # Katı atık bertaraf ücretini hesaplar
    return (hane_sayisi*KATI_ATIK_BERTARAF_UCRETI_SABITI)
def su_tuketim_bedeli_hesaplama(abone_tipi_no,kullanilan_ton,tuketim_gun_sayisi,hane_sayisi): # Su tüketim bedeli,ücretini hesaplar
    if abone_tipi_no==1:
        if (kullanilan_ton/tuketim_gun_sayisi)*AYLIK_GUN<=BIRINCI_KADEME_TON_MIKTARI_SINIRI:
            ucret=kullanilan_ton*ABONE_BIR_BIRINCI_KADEME_STBU
        elif (kullanilan_ton/tuketim_gun_sayisi)*AYLIK_GUN<=IKINCI_KADEME_TON_MIKTARI_SINIRI:
            ucret=(BIRINCI_KADEME_TON_MIKTARI_SINIRI*ABONE_BIR_BIRINCI_KADEME_STBU)+(kullanilan_ton-BIRINCI_KADEME_TON_MIKTARI_SINIRI)*ABONE_BIR_IKINCI_KADEME_STBU
        else:
            ucret=(BIRINCI_KADEME_TON_MIKTARI_SINIRI*ABONE_BIR_BIRINCI_KADEME_STBU)+((IKINCI_KADEME_TON_MIKTARI_SINIRI-BIRINCI_KADEME_TON_MIKTARI_SINIRI)\
                                        *ABONE_BIR_IKINCI_KADEME_STBU)+((kullanilan_ton-IKINCI_KADEME_TON_MIKTARI_SINIRI)*ABONE_BIR_UCUNCU_KADEME_STBU)
    elif abone_tipi_no==2:
        ucret=ABONE_IKI_STBU*kullanilan_ton
    elif abone_tipi_no==3:
        ucret=ABONE_UC_STBU*kullanilan_ton
    elif abone_tipi_no==4:
        ucret=ABONE_DORT_STBU*kullanilan_ton
    else:
        if (kullanilan_ton/tuketim_gun_sayisi)*AYLIK_GUN<BIRINCI_KADEME_TON_MIKTARI_SINIRI:
            ucret=kullanilan_ton*ABONE_BES_BIRINCI_KADEME_STBU
        elif (kullanilan_ton/tuketim_gun_sayisi)*AYLIK_GUN<IKINCI_KADEME_TON_MIKTARI_SINIRI:
            ucret=(BIRINCI_KADEME_TON_MIKTARI_SINIRI*ABONE_BES_BIRINCI_KADEME_STBU)+(kullanilan_ton-BIRINCI_KADEME_TON_MIKTARI_SINIRI)*ABONE_BES_IKINCI_KADEME_STBU
        else:
            ucret=(BIRINCI_KADEME_TON_MIKTARI_SINIRI*ABONE_BES_BIRINCI_KADEME_STBU)+((IKINCI_KADEME_TON_MIKTARI_SINIRI-BIRINCI_KADEME_TON_MIKTARI_SINIRI)\
                                           *ABONE_BES_IKINCI_KADEME_STBU)+((kullanilan_ton-IKINCI_KADEME_TON_MIKTARI_SINIRI)*ABONE_BES_UCUNCU_KADEME_STBU)
    return (ucret*hane_sayisi)
def atik_su_bedeli_hesaplama(abone_tipi_no,kullanilan_ton,tuketim_gun_sayisi,hane_sayisi): # Atık su bedeli,ücretini hesaplar
    if abone_tipi_no==1:
        if (kullanilan_ton/tuketim_gun_sayisi)*AYLIK_GUN<=BIRINCI_KADEME_TON_MIKTARI_SINIRI:
            ucret=kullanilan_ton*ABONE_BIR_BIRINCI_KADEME_ASBU
        elif (kullanilan_ton/tuketim_gun_sayisi)*AYLIK_GUN<=IKINCI_KADEME_TON_MIKTARI_SINIRI:
            ucret=(BIRINCI_KADEME_TON_MIKTARI_SINIRI*ABONE_BIR_BIRINCI_KADEME_ASBU)+(kullanilan_ton-BIRINCI_KADEME_TON_MIKTARI_SINIRI)*ABONE_BIR_IKINCI_KADEME_ASBU
        else:
            ucret=(BIRINCI_KADEME_TON_MIKTARI_SINIRI*ABONE_BIR_BIRINCI_KADEME_ASBU)+((IKINCI_KADEME_TON_MIKTARI_SINIRI-BIRINCI_KADEME_TON_MIKTARI_SINIRI)\
                                    *ABONE_BIR_IKINCI_KADEME_ASBU)+((kullanilan_ton-IKINCI_KADEME_TON_MIKTARI_SINIRI)*ABONE_BIR_UCUNCU_KADEME_ASBU)
    elif abone_tipi_no==2:
        ucret=ABONE_IKI_ASBU*kullanilan_ton
    elif abone_tipi_no==3:
        ucret=ABONE_UC_ASBU*kullanilan_ton
    elif abone_tipi_no==4:
        ucret=ABONE_DORT_ASBU*kullanilan_ton
    else:
        if (kullanilan_ton/tuketim_gun_sayisi)*AYLIK_GUN<=BIRINCI_KADEME_TON_MIKTARI_SINIRI:
            ucret=kullanilan_ton*ABONE_BES_BIRINCI_KADEME_ASBU
        elif (kullanilan_ton/tuketim_gun_sayisi)*AYLIK_GUN<=IKINCI_KADEME_TON_MIKTARI_SINIRI:
            ucret=(BIRINCI_KADEME_TON_MIKTARI_SINIRI*ABONE_BES_BIRINCI_KADEME_ASBU)+(kullanilan_ton-BIRINCI_KADEME_TON_MIKTARI_SINIRI)*ABONE_BES_IKINCI_KADEME_ASBU
        else:
            ucret=(BIRINCI_KADEME_TON_MIKTARI_SINIRI*ABONE_BES_BIRINCI_KADEME_ASBU)+((IKINCI_KADEME_TON_MIKTARI_SINIRI-BIRINCI_KADEME_TON_MIKTARI_SINIRI)*\
                                            ABONE_BES_IKINCI_KADEME_ASBU)+((kullanilan_ton-IKINCI_KADEME_TON_MIKTARI_SINIRI)*ABONE_BES_UCUNCU_KADEME_ASBU)
    return (ucret*hane_sayisi)
def engelli_indiririmi_hesaplama(kullanilan_ton,gun_sayisi,hane_sayisi,ucret): # Engelli indirimini hesaplar
    if ((kullanilan_ton/hane_sayisi)/gun_sayisi)*AYLIK_GUN<=IKINCI_KADEME_TON_MIKTARI_SINIRI:
        return ((ucret/hane_sayisi)/2)
    else:
        if ucret==indirimsiz_stb:
            return (BIRINCI_KADEME_TON_MIKTARI_SINIRI*ABONE_BIR_BIRINCI_KADEME_STBU+(IKINCI_KADEME_TON_MIKTARI_SINIRI-BIRINCI_KADEME_TON_MIKTARI_SINIRI)*\
                                                                                                        ABONE_BIR_IKINCI_KADEME_STBU)/2
        else:
            return (BIRINCI_KADEME_TON_MIKTARI_SINIRI*ABONE_BIR_BIRINCI_KADEME_ASBU+(IKINCI_KADEME_TON_MIKTARI_SINIRI-BIRINCI_KADEME_TON_MIKTARI_SINIRI)*\
                                                                                                        ABONE_BIR_IKINCI_KADEME_ASBU)/2
def main():
    abone_iki,abone_uc,abone_dort,abone_bes=0,0,0,0 # Akümülatörler
    abone_bir_su_miktari,abone_iki_su_miktari,abone_uc_su_miktari,abone_dort_su_miktari,abone_bes_su_miktari=0,0,0,0,0
    abone_bir_gun_sayisi,abone_iki_gun_sayisi,abone_uc_gun_sayisi,abone_dort_gun_sayisi,abone_bes_gun_sayisi=0,0,0,0,0
    kademe_bir_abone,kademe_iki_abone,kademe_uc_abone=0,0,0
    abone_bir=kademe_bir_abone+kademe_iki_abone+kademe_uc_abone
    kademe_bir_abone_su_miktari,kademe_iki_abone_su_miktari,kademe_uc_abone_su_miktari=0,0,0
    kademe_bir_abone_gun_sayisi,kademe_iki_abone_gun_sayisi,kademe_uc_abone_gun_sayisi=0,0,0
    elliden_fazla,elli_ton_veya_500_tl=0,0
    toplam_sehit_gazi_sporcu_sayisi,toplam_engelli_sayisi=0,0
    max_su_tuketim_abone_uc,max_su_tuketim_abone_uc_gun_sayisi=0,0
    max_su_tuketim_abone_uc_no=""
    max_su_tuketim_gun_sayisi=0
    max_stu,max_su_harcamasi=0,0 # stu=su tüketim ücreti
    abone_bir_toplam_stu,abone_iki_toplam_stu,abone_uc_toplam_stu,abone_dort_toplam_stu,abone_bes_toplam_stu=0,0,0,0,0
    toplam_izsu_miktari,toplam_buyuksehir_miktari,toplam_ilce_miktari,toplam_kdv=0,0,0,0
    max_stu_abone_tipi=""
    max_stu_no=""
    devam="e"
    while devam=="e" or devam=="E":
        abone_numarasi=input("Abone numaranızı giriniz: ")
        print("Abone tipini kodunu giriniz [1-5]: ",end="")
        abone_tipi=sayi_al(1,5)
        if abone_tipi==1:
            print("Hane sayısını giriniz [1 veya 1'den büyük]: ",end="")
            abone_bir_hane_sayisi=sayi_al(1,999999999999999)
            if abone_bir_hane_sayisi==1:
                indirim_durumu=input("Yok/Şehit/Gazi/Sporcu/Engelli: (Y/y/Ş/ş/G/g/S/s/E/e karakterleri)")
                while indirim_durumu not in ["y","Y","ş","Ş","g","G","s","S","e","E"]:
                    indirim_durumu=input("Hatalı giriş! Lütfen tekrar giriniz: ")
                if indirim_durumu=="e" or indirim_durumu=="E":
                    engelli_sayisi=1
                    sehit_gazi_sporcu_sayisi=0
                elif indirim_durumu in ["Ş","ş","G","g","S","s"]:
                    sehit_gazi_sporcu_sayisi=1
                    engelli_sayisi=0
                else:
                    engelli_sayisi=0
                    sehit_gazi_sporcu_sayisi=0
            else:
                print("Şehit, gazi veya sporcu sayısı [(tamsayı) 0-hane sayısı arasında]: ",end="")
                sehit_gazi_sporcu_sayisi=sayi_al(0,abone_bir_hane_sayisi)
                print("Engelli sayısı [(tamsayı) 0-hane sayısı arasında]: ",end="")
                engelli_sayisi=sayi_al(0,abone_bir_hane_sayisi-sehit_gazi_sporcu_sayisi)
        else:
            diger_hane_sayisi=1
        print("Önceki sayaç değerini giriniz [(tamsayı) 0 veya daha büyük bir sayı]: ", end="")
        onceki_sayac_degeri=sayi_al(0,9999999999999999)
        print("Şimdiki sayaç değerini giriniz [(tamsayı) önceki sayaç değerine eşit ya da daha büyük]: ", end="")
        simdiki_sayac_degeri=sayi_al(onceki_sayac_degeri,99999999999999999999999999)
        print("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını giriniz [(tamsayı) (0’dan büyük)]: ",end="")
        gun_sayisi=sayi_al(1,99999999999999999)
        stm=simdiki_sayac_degeri-onceki_sayac_degeri # stm=su tüketim miktarı
        ctv=ctv_hesaplama(stm)
        if abone_tipi!=1:
            stb=su_tuketim_bedeli_hesaplama(abone_tipi,stm,gun_sayisi,diger_hane_sayisi) # stb=su tüketim bedeli
            asb=atik_su_bedeli_hesaplama(abone_tipi,stm,gun_sayisi,diger_hane_sayisi) # asb=atık su bedeli
            toplam_stb_asb=stb+asb
            katu=kati_atik_toplama_bedeli_hesaplama(diger_hane_sayisi) # katu=katı atık toplama ücreti
            kabu=kati_atik_bertaraf_ucreti_hesaplama(diger_hane_sayisi) # kabu=katı atık bertaraf ücreti
            kdv=kdv_hesaplama(stb+asb+katu+kabu)
            toplam_fatura=toplam_stb_asb+ctv+kabu+katu+kdv
            ilce_miktari=kabu
            buyuksehir_miktari=ctv+katu
            izsu_miktari=toplam_stb_asb
        else:
            indirimsiz_stb=su_tuketim_bedeli_hesaplama(abone_tipi,stm/abone_bir_hane_sayisi,gun_sayisi,abone_bir_hane_sayisi)
            stb=indirimsiz_stb-engelli_sayisi*engelli_indiririmi_hesaplama(stm,gun_sayisi,abone_bir_hane_sayisi,indirimsiz_stb)-sehit_gazi_sporcu_sayisi*\
                (indirimsiz_stb/(abone_bir_hane_sayisi*2))
            indirimsiz_asb=atik_su_bedeli_hesaplama(abone_tipi,stm/abone_bir_hane_sayisi,gun_sayisi,abone_bir_hane_sayisi)
            asb=indirimsiz_asb-engelli_sayisi*engelli_indiririmi_hesaplama(stm,gun_sayisi,abone_bir_hane_sayisi,indirimsiz_asb)-sehit_gazi_sporcu_sayisi*\
                (indirimsiz_asb/(abone_bir_hane_sayisi*2))
            toplam_stb_asb=stb+asb
            katu=kati_atik_toplama_bedeli_hesaplama(abone_bir_hane_sayisi)
            kabu=kati_atik_bertaraf_ucreti_hesaplama(abone_bir_hane_sayisi)
            kdv=kdv_hesaplama(stb+asb+katu+kabu)
            toplam_fatura=toplam_stb_asb+ctv+kabu+katu+kdv
            ilce_miktari=kabu
            buyuksehir_miktari=ctv+katu
            izsu_miktari=toplam_stb_asb
        print("Abone numarası: ",abone_numarasi)
        if abone_tipi==1:
            print("Abone tipi: Konut")
            if ((stm/abone_bir_hane_sayisi)/gun_sayisi)*AYLIK_GUN<BIRINCI_KADEME_TON_MIKTARI_SINIRI:
                print("1. Kademe")
            elif ((stm/abone_bir_hane_sayisi)/gun_sayisi)*AYLIK_GUN<IKINCI_KADEME_TON_MIKTARI_SINIRI:
                print("2.Kademe")
            else:
                print("3. Kademe")
        elif abone_tipi==2:
            print("İşyeri")
        elif abone_tipi==3:
            print("Resmi Daire")
        elif abone_tipi==4:
            print("Organize Sanayi")
        else:
            print("İlçe Tarımsal ve Hayvan Sulama")
        print("Dönemlik su tüketim miktarı: ",format(stm,".2f"),"M3")
        print("Dönemlik su tüketim ücreti: ",format(stb,".2f")," TL")
        print("Dönemlik atık su ücreti: ",format(asb,".2f")," TL")
        print("Dönemlik toplam su tüketim ve atık su ücreti: ",format(toplam_stb_asb,".2f")," TL")
        print("Dönemlik ÇTV tutarı: ",format(ctv,".2f")," TL")
        print("Dönemlik katı atık toplama ücreti: ",format(katu,".2f")," TL")
        print("Dönemlik katı atık bertaraf ücreti: ",kabu," TL")
        print("Dönemlik toplam fatura tutarı: ",format(toplam_fatura,".2f")," TL")
        print("Dönemlik devlete aktarılacak KDV tutarı (%8): ",format(kdv,".2f")," TL")
        print("Dönemlik ilçe belediyesine aktarılacak tutar: ",format(ilce_miktari,".2f")," TL")
        print("Dönemlik büyükşehir belediyesine aktarılacak tutar: ",format(buyuksehir_miktari,".2f")," TL")
        print("Dönemlik İZSU payı: ",format(izsu_miktari,".2f")," TL")
        if abone_tipi==1:
            abone_bir_su_miktari+=stm
            abone_bir_toplam_stu+=stb
            toplam_sehit_gazi_sporcu_sayisi+=sehit_gazi_sporcu_sayisi
            toplam_engelli_sayisi+=engelli_sayisi
            abone_bir_gun_sayisi+=gun_sayisi
            if ((stm/abone_bir_hane_sayisi)/gun_sayisi)*AYLIK_GUN<=BIRINCI_KADEME_TON_MIKTARI_SINIRI:
                kademe_bir_abone+=abone_bir_hane_sayisi
                kademe_bir_abone_su_miktari+=stm
                kademe_bir_abone_gun_sayisi+=gun_sayisi
            elif ((stm/abone_bir_hane_sayisi)/gun_sayisi)*AYLIK_GUN<=IKINCI_KADEME_TON_MIKTARI_SINIRI:
                kademe_iki_abone+=abone_bir_hane_sayisi
                kademe_iki_abone_su_miktari+=stm
                kademe_iki_abone_gun_sayisi+=gun_sayisi
            else:
                kademe_uc_abone+=abone_bir_hane_sayisi
                kademe_uc_abone_su_miktari+=stm
                kademe_uc_abone_gun_sayisi+=gun_sayisi
        elif abone_tipi==2:
            abone_iki+=1
            abone_iki_su_miktari=stm
            abone_iki_toplam_stu+=stb
            abone_iki_gun_sayisi+=gun_sayisi
        elif abone_tipi==3:
            if stm/gun_sayisi>max_su_tuketim_abone_uc:
                max_su_tuketim_abone_uc=stm
                max_su_tuketim_abone_uc_no=abone_numarasi
                max_su_tuketim_abone_uc_gun_sayisi=gun_sayisi
            abone_uc+= 1
            abone_uc_su_miktari=stm
            abone_uc_toplam_stu+=stb
            abone_uc_gun_sayisi+=gun_sayisi
        elif abone_tipi==4:
            abone_dort+=1
            abone_dort_su_miktari=stm
            abone_dort_toplam_stu+=stb
            abone_dort_gun_sayisi+=gun_sayisi
        else:
            if ((stm/diger_hane_sayisi)/gun_sayisi)*AYLIK_GUN<50:
                elliden_fazla+=1
            abone_bes+=1
            abone_bes_su_miktari=simdiki_sayac_degeri-onceki_sayac_degeri
            abone_bes_toplam_stu+=stb
            abone_bes_gun_sayisi+=gun_sayisi
        if abone_tipi!=1:
            if stb>max_stu:
                max_stu=stb
                max_su_harcamasi=stm
                max_stu_no=abone_numarasi
                max_su_tuketim_gun_sayisi=gun_sayisi
                if abone_tipi==2:
                    max_stu_abone_tipi="İşyeri"
                elif abone_tipi==3:
                    max_stu_abone_tipi="Resmi Daire"
                elif abone_tipi==4:
                    max_stu_abone_tipi="Organize Sanayi"
                else:
                    max_stu_abone_tipi="İlçe Tarımsal ve Hayvan Sulama"
        if abone_tipi==1:
            if ((stm/abone_bir_hane_sayisi)/gun_sayisi)*AYLIK_GUN>100 or ((stb/abone_bir_hane_sayisi)/gun_sayisi)*AYLIK_GUN>500:
                elli_ton_veya_500_tl += abone_bir_hane_sayisi
        else:
            if ((stm/diger_hane_sayisi)/gun_sayisi)*AYLIK_GUN>100 or ((stb/abone_bir_hane_sayisi)/gun_sayisi)*AYLIK_GUN>500:
                elli_ton_veya_500_tl += diger_hane_sayisi
        toplam_izsu_miktari+=izsu_miktari
        toplam_buyuksehir_miktari+=buyuksehir_miktari
        toplam_kdv+=kdv
        toplam_ilce_miktari+=ilce_miktari
        devam = input("Başka bir abone var mı?(e/E/h/H karakterleri): ")
        while devam not in ["e", "E", "h", "H"]:
            devam = input("Hatalı giriş! Lütfen tekrar giriniz: ")
    toplam_abone_sayisi=abone_bir+abone_iki+abone_uc+abone_dort+abone_bes
    abone_bir_aylik_stm=((abone_bir_su_miktari/abone_bir_gun_sayisi)*AYLIK_GUN)
    abone_iki_aylik_stm=((abone_iki_su_miktari/abone_iki_gun_sayisi)*AYLIK_GUN)
    abone_uc_aylik_stm=((abone_uc_su_miktari/abone_uc_gun_sayisi)*AYLIK_GUN)
    abone_dort_aylik_stm=((abone_dort_su_miktari/abone_dort_gun_sayisi)*AYLIK_GUN)
    abone_bes_aylik_stm=((abone_bes_su_miktari/abone_bes_gun_sayisi)*AYLIK_GUN)
    toplam_aylik_stm=abone_bir_aylik_stm+abone_iki_aylik_stm+abone_uc_aylik_stm+abone_dort_aylik_stm+abone_bes_aylik_stm
    abone_bir_aylik_stu=(abone_bir_toplam_stu/abone_bir_gun_sayisi)*AYLIK_GUN
    abone_iki_aylik_stu=(abone_iki_toplam_stu/abone_iki_gun_sayisi)*AYLIK_GUN
    abone_uc_aylik_stu=(abone_uc_toplam_stu/abone_uc_gun_sayisi)*AYLIK_GUN
    abone_dort_aylik_stu=(abone_dort_toplam_stu/abone_dort_gun_sayisi)*AYLIK_GUN
    abone_bes_aylik_stu=(abone_bes_toplam_stu/abone_bes_gun_sayisi)*AYLIK_GUN
    toplam_aylik_stu=abone_bir_aylik_stu+abone_iki_aylik_stu+abone_uc_aylik_stu+abone_dort_aylik_stu+abone_bes_aylik_stu
    print("Konut tipi için abone sayısı: ",abone_bir,"yüzdesi:%",format((abone_bir/toplam_abone_sayisi)*100,".2f"),"aylık ortalama su tüketim miktarı: ",format(((abone_bir_su_miktari/abone_bir_gun_sayisi)*AYLIK_GUN)/abone_bir,".2f"))
    print("İşyeri tipi için abone sayısı: ",abone_iki,"yüzdesi:%",format(((abone_iki/toplam_abone_sayisi)*100),".2f"),"aylık ortalama su tüketim miktarı: ",format(((abone_iki_su_miktari/abone_iki_gun_sayisi)*AYLIK_GUN)/abone_iki,".2f"))
    print("Resmi Daire için abone sayısı: ",abone_uc,"yüzdesi:%",format(((abone_uc/toplam_abone_sayisi)*100),".2f"),"aylık ortalama su tüketim miktarı: ",format(((abone_uc_su_miktari/abone_uc_gun_sayisi)*AYLIK_GUN)/abone_uc,".2f"))
    print("Organize Sanayi için abone sayısı: ",abone_dort,"yüzdesi:%",format(((abone_dort/toplam_abone_sayisi)*100),".2f"),"aylık ortalama su tüketim miktarı: ",format(((abone_dort_su_miktari/abone_dort_gun_sayisi)*AYLIK_GUN)/abone_dort,".2f"))
    print("İlçe Tarımsal ve Hayvan Sulama için abone sayısı: ",abone_bes,"yüzdesi:%",format(((abone_bes/toplam_abone_sayisi)*100),".2f"),"aylık ortalama su tüketim miktarı: ",format(((abone_bes_su_miktari/abone_bes_gun_sayisi)*AYLIK_GUN)/abone_bes,".2f"))
    print("Kademe 1 Konut tipi abone sayısı: ",kademe_bir_abone,"yüzdesi :%",format((kademe_bir_abone/abone_bir)*100,".2f"),"aylık ortalama su tüketim miktarı: ",format((kademe_bir_abone_su_miktari/kademe_bir_abone_gun_sayisi)*AYLIK_GUN/kademe_bir_abone,".2f"))
    print("Kademe 2 Konut tipi abone sayısı: ",kademe_iki_abone,"yüzdesi :%",format((kademe_iki_abone/abone_bir)*100,".2f"),"aylık ortalama su tüketim miktarı: ",format((kademe_iki_abone_su_miktari/kademe_iki_abone_gun_sayisi)*AYLIK_GUN/kademe_iki_abone,".2f"))
    print("Kademe 3 Konut tipi abone sayısı: ",kademe_uc_abone,"yüzdesi :%",format((kademe_uc_abone/abone_bir)*100,".2f"),"aylık ortalama su tüketim miktarı: ",format((kademe_uc_abone_su_miktari/kademe_uc_abone_gun_sayisi)*AYLIK_GUN/kademe_uc_abone,".2f"))
    print("Aylık su tüketim miktarı 50 tondan fazla olan ilçe tarımsal ve hayvan sulama tipi abonelerin sayısı: ",elliden_fazla,"yüzdesi:%",format((elliden_fazla/abone_bes)*100,".2f"))
    print("Aylık su tüketim miktarı 100 tondan yüksek veya aylık su tüketim ücreti 500 TL’den yüksek olan abonelerin (hanelerin) sayısı: ",elli_ton_veya_500_tl)
    print("Şehit, gazi veya devlet sporcusu olan konut tipi abonelerin sayısı: ",toplam_sehit_gazi_sporcu_sayisi,"yüzdesi:%",format((toplam_sehit_gazi_sporcu_sayisi/abone_bir)*100,".2f"))
    print("Engelli olan konut tipi abonelerin sayısı: ",toplam_engelli_sayisi,"yüzdesi:%",format((toplam_engelli_sayisi/abone_bir)*100,".2f"))
    print("Aylık su tüketim miktarı en yüksek olan resmi daire tipi abonenin abone numarası: ",max_su_tuketim_abone_uc_no,"ve aylık su tüketim miktarı: ",format((max_su_tuketim_abone_uc/max_su_tuketim_abone_uc_gun_sayisi)*AYLIK_GUN,".2f"))
    print("Aylık su tüketim ücreti en yüksek olan konut tipi dışındaki abonenin abone numarası: ",max_stu_no,"abone tipi adı: ",max_stu_abone_tipi)
    print("Aylık su tüketim miktarı: ",format((max_su_harcamasi/max_su_tuketim_gun_sayisi)*AYLIK_GUN,".2f"),"aylık su tüketim ücreti: ",format((max_stu/max_su_tuketim_gun_sayisi)*AYLIK_GUN,".2f"))
    print("Konut tipi için aylık toplam su tüketim miktarı: ",format(abone_bir_aylik_stm,".2f"),"Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi:%",format((abone_bir_aylik_stm/toplam_aylik_stm)*100,".2f"))
    print("İşyeri tipi için aylık toplam su tüketim miktarı: ",format(abone_iki_aylik_stm,".2f"),"Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi:%",format((abone_iki_aylik_stm/toplam_aylik_stm)*100,".2f"))
    print("Resmi Daire tipi için aylık toplam su tüketim miktarı: ",format(abone_uc_aylik_stm,".2f"),"Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi:%",format((abone_uc_aylik_stm/toplam_aylik_stm)*100,".2f"))
    print("Organize Sanayi tipi için aylık toplam su tüketim miktarı: ",format(abone_dort_aylik_stm,".2f"),"Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi:%",format((abone_dort_aylik_stm/toplam_aylik_stm)*100,".2f"))
    print("İlçe Tarımsal ve Hayvan Sulama tipi için aylık toplam su tüketim miktarı: ",format(abone_bes_aylik_stm,".2f"),"Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi:%",format((abone_bes_aylik_stm/toplam_aylik_stm)*100,".2f"))
    print("Bornova’nın aylık toplam su tüketim miktarı",format(toplam_aylik_stm,".2f"))
    print("Konut tipi için aylık toplam su tüketim ücreti: ",format(abone_bir_aylik_stu,".2f"))
    print("İşyeri tipi için aylık toplam su tüketim ücreti: ",format(abone_iki_aylik_stu,".2f"))
    print("Resmi Daire tipi için aylık toplam su tüketim ücreti: ",format(abone_uc_aylik_stu,".2f"))
    print("Organize Sanayi tipi için aylık toplam su tüketim ücreti: ",format(abone_dort_aylik_stu,".2f"))
    print("İlçe Tarımsal ve Hayvan Sulama tipi için aylık toplam su tüketim ücreti: ",format(abone_bes_aylik_stu,".2f"))
    print("Tüm abonelerden elde edilen aylık toplam su tüketim ücreti: ",format(toplam_aylik_stu,".2f"))
    print("İZSU’nun elde ettiği gelir tutarı: ",format(toplam_izsu_miktari,".2f"))
    print("İlçe belediyesinin elde ettiği gelir tutarı: ",format(toplam_ilce_miktari,".2f"))
    print("Büyükşehir belediyesinin elde ettiği gelir tutarı: ",format(toplam_buyuksehir_miktari,".2f"))
    print("Devletin (kdv) elde ettiği gelir tutarı: ",format(toplam_kdv,".2f"))
main()
# The end
