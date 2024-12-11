import random

def paralel_gorev_simulasyonu(paralel_oran, islemci_sayisi, toplam_gorev=1000):
    
    if not (0 <= paralel_oran <= 1):
        raise ValueError("Paralel oran 0 ile 1 arasinda olmalidir.")
    if islemci_sayisi <= 0:
        raise ValueError("Islemci sayisi 0'dan buyuk olmalidir.")
    if toplam_gorev <= 0:
        raise ValueError("Toplam görev sayisi 0'dan buyuk olmalidir.")

    paralel_gorevler = int(toplam_gorev * paralel_oran)
    seri_gorevler = toplam_gorev - paralel_gorevler

    seri_sure = seri_gorevler  
    paralel_sure = (paralel_gorevler / islemci_sayisi)  

    toplam_sure = seri_sure + paralel_sure

    return {
        "Toplam Gorev": toplam_gorev,
        "Paralel Gorevler": paralel_gorevler,
        "Seri Gorevler": seri_gorevler,
        "Islemciler": islemci_sayisi,
        "Yurutme Suresi": toplam_sure,
    }

def ana_program():
    print("Amdahl Yasasina Dayali Gorev Yurutme Simulatoru")

    try:
        paralel_oran = float(input("Paralel hale getirilebilecek gorev oranini girin (0 ile 1 arasında): "))
        islemci_sayisi = int(input("İslemci sayisini girin: "))
        toplam_gorev = int(input("Toplam gorev sayisi girin: "))

        sonuc = paralel_gorev_simulasyonu(paralel_oran, islemci_sayisi, toplam_gorev)

        print("\nSimulasyon Sonuclari:")
        for anahtar, deger in sonuc.items():
            print(f"{anahtar}: {deger}")
    except ValueError as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    ana_program()
