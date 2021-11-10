import requests
from bs4 import BeautifulSoup


def ekstraksi_data() -> object:
    try:
        content = requests.get("https://www.bmkg.go.id/")
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")
        # tanggal = soup.find('span', {'class': 'waktu'})

        result = soup.find('div', {'class':'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        # print("\n")
        i = 0
        tanggal = None
        magnitudo = None
        kedalaman = None
        koordinat = None
        lokasi = None
        dirasakan = None

        for res in result:
            # print(i,res)
            if i == 0:
                tanggal_waktu = res.text.split(', ')
            elif i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(" - ")
            elif i == 4:
                lokasi = res.text
            elif i ==5:
                dirasakan = res.text

            i += 1
        # print(result)
        # print("\n")

        hasil = dict()
        hasil['tanggal'] = tanggal_waktu[0] #"24 Agustus 2021"
        hasil['waktu'] = tanggal_waktu[1] #"12:05:52 WIB"
        hasil['magnitudo'] = magnitudo #4.0
        hasil['kedalaman'] = kedalaman
        hasil['ls'] = koordinat[0]
        hasil['bt'] = koordinat[1]
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan

        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print("Tidak menemukan data gempa terkini")
        return
    print("Gempa terakhir berdasakan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat: Ls={result['ls']}, BT={result['bt']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"{result['dirasakan']}")

if __name__ == '__main__':
    result = ekstraksi_data()
    tampilkan_data(result)