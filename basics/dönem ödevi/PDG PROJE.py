import requests
import sqlite3
import json
import tkinter as tk
from tkinter import messagebox

import webbrowser   ## ARATTIĞIMIZ PLAYLİSTLERE WEBDEN ULAŞMAK İÇİN EKLEDİM




     ##  BU FONKSİYONU GPT'YE ARANAN SONUÇLARI VE FİLTREYİ TEMİZLEMEK İÇİN YAZDIRDIM
def temizle():
    liste.delete(0, tk.END)
    tum_playlistler.clear()
    artist_id_entry.delete(0, tk.END)


     ##  SANATÇILARIN TAKİPÇİ SAYILARINI STRİNG OLARAK ÇEKEBİLİYORDUM, SAKLAMA VE FİLTRELEME İÇİN İNTEGER TÜRÜNE DÖNÜŞTÜRMESİ İÇİN GPTYE YAZDIRDIM
def takipci_sayisini_int_yap(value):
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        value = value.strip().upper()
        if value.endswith('M'):
            try:
                return int(float(value[:-1]) * 1_000_000)
            except:
                return 0
        elif value.endswith('K'):
            try:
                return int(float(value[:-1]) * 1_000)
            except:
                return 0
        else:
            try:
                return int(value.replace(',', ''))
            except:
                return 0
    return 0



     ##   SAYIYA ÇEVİRMEDE BİR PROBLEM YAŞIYORDUM , GÜVENLİ BİR ŞEKİLDE ÇEVİRMEM İÇİN GPT'YE BU FONKSİYONU YAZDIRDIM
def safe_int(value):
    try:
        return int(value)
    except:
        return 0



     ##  TÜM PLAYLİSTLERİ SAKLAMAK İÇİN OLUŞTURDUĞUM DEPO 
tum_playlistler = []



     ##  SANATÇI VE PLAYLİSTLERLE İLGİLİ VERİLERE ULAŞMAK İÇİN SONGSTATS APİ'SİNİ KULLANDIM.
       
url = "https://songstats.p.rapidapi.com/artists/top_playlists"
headers = {
    "x-rapidapi-key": "071c9a6de6mshd578656e6bc0e09p18668djsn71c839470074",
    "x-rapidapi-host": "songstats.p.rapidapi.com"
}
querystring = {
    "limit": "20",
    "source": "all",
    "scope": "total"
}

     
     

baglanti = sqlite3.connect("playlist.db")
cursornesnesi = baglanti.cursor()
cursornesnesi.execute("""CREATE TABLE IF NOT EXISTS PlayLists(id TEXT PRIMARY KEY, isim TEXT, takipcisayisi TEXT, kaynak TEXT, artist_id TEXT)""")
baglanti.commit()
baglanti.close()




      ##  API ÇAĞIRMAK İÇİN BU FONKSİYONU KENDİM YAZMAYA BAŞLADIM

def apicagirma():
    global tum_playlistler
    artist_id = artist_id_entry.get().strip()
    if not artist_id:
        messagebox.showwarning("Uyarı", "Lütfen Spotify Artist ID girin.")
        return
    
         ## YENİ VERİLER İLE ESKİ VERİLERİN KARIŞMAMASI İÇİN GPT BU KISMI DÜZENLEDİ
    liste.delete(0, tk.END)
    tum_playlistler.clear()


        ## BU KISMI BAŞTA FONKSİYON DIŞINDA YAZMIŞTIM AMA GPT FONKSİYON İÇİNDE YAZMAMI SÖYLEDİ ÖYLE DÜZELTTİM

    with sqlite3.connect("playlist.db") as baglanti:
        cursor = baglanti.cursor()

          ## AYNI SANATÇI İÇİN DAHA ÖNCE VERİ ÇEKMİŞ MİYİM KONTROL AMAÇLI. ÇÜNKÜ APİ BANA GÜNLÜK SADECE 20 DEFA VERİ ÇEKMEME
          ## İZİN VERİYORDU, TEKRAR ÇEKMEMEK İÇİN GPT'DEN YARDIM ALDIM
        cursor.execute("SELECT isim, takipcisayisi, id FROM PlayLists WHERE artist_id = ?", (artist_id,))
        veriler = cursor.fetchall()

        if veriler:
            for ad, takipci, pid in veriler:
                tum_playlistler.append((ad, takipci, pid))
            filtrele()
            return

             ##  BU KISMI GPT PARAMETRELERİ AYARLAMAK İÇİN YAZDI
        params = querystring.copy()
        params["spotify_artist_id"] = artist_id
        print("API Parametreleri:", params) ####

        try:
            dönüt = requests.get(url, headers=headers, params=params)
            veri = dönüt.json()
            print(json.dumps(veri, indent=2, ensure_ascii=False))

             
             ##   BU KISIM CİDDEN ÇILDIRTTI, VERİLERİ ÇEKİP YAZDIRAMIYORDUM EN SONUNDA YAPTIM AMA.            
            if "top_playlists" in veri["data"][0]:
                for playlist in veri["data"][0]["top_playlists"]:
                    ad = playlist.get("playlist_name")
                    takipci = playlist.get("followers_total")
                    kaynak = playlist.get("source", "belirsiz")
                    pid = playlist.get("playlist_id")
                    tum_playlistler.append((ad, takipci, pid)) 
                    cursor.execute("INSERT OR REPLACE INTO PlayLists (id, isim, takipcisayisi, kaynak, artist_id) VALUES (?, ?, ?, ?, ?)", (pid, ad, takipci, kaynak, artist_id))

                baglanti.commit()
                filtrele()
            else:
                liste.insert(tk.END, "Top playlist bilgisi yok.")
        except Exception as e:
            liste.insert(tk.END, "Veri çekilemedi. Hata oluştu.")
            print("Hata:", e)

   
   ##  BU FONKSİYONU PLAYLİSTLERE ÇİFT TIKLAYARK WEBDEN AÇMAK İÇİN YAZDIRDIM, NASIL DAHA ZENGİNLEŞTİRİRİM DİYE DÜŞÜNÜYORDUM
def detay_goster(event):
    secilen = liste.curselection()
    if secilen:
        i = secilen[0]
        ad, takipci, pid = tum_playlistler[i]
        cevap = messagebox.askyesno("Playlist Detayı", f"Ad: {ad}\nTakipçi: {takipci}\nSpotify’da açmak ister misiniz?")
        if cevap:
            webbrowser.open(f"https://open.spotify.com/playlist/{pid}")



     ## PLAYLİSTLERİ ARATMAK İÇİN BU FONKSİYONU YAZDIRDIM.
def filtrele():
    filtre = filtregirdisi.get().lower()
    liste.delete(0, tk.END)
    sirali = sorted(tum_playlistler, key=lambda x: takipci_sayisini_int_yap(x[1]), reverse=True)


    for i, (ad, takipci,pid) in enumerate(sirali, start=1):
        if filtre in ad.lower():
            liste.insert(tk.END, f"{i}. {ad} - {takipci} takipçi")


     
     ##  ARAYÜZÜ BİLDİĞİM KADAR YAZDIM, GÖRÜNÜMÜ ZENGİNLEŞTİRMEK İÇİN YARDIM ALDIM
     ##  KODLARI ARAYÜZE DÖKERKEN BAZI SORUNLAR YAŞADIM ONLARI DÜZELTMESİ İÇİN GPT'DEN YARDIM ALDIM

  ##  BUTONA EFEKT EKLEMEK İÇİN BUNU YAPTIM
def on_enter(e):
    buton.config(bg='#4CAF50', fg='white')

def on_leave(e):
    buton.config(bg='SystemButtonFace', fg='black')

pencere = tk.Tk()
temizletuşu = tk.Button(pencere, text="Temizle", command=temizle, bg="#c0392b", fg="white")
temizletuşu.pack(pady=(5, 0))
pencere.title("Playlist Sayfası")
pencere.geometry("650x500")
pencere.configure(bg='#2c3e50')

başlık = tk.Label(pencere, text="Spotify Artist ID'sini girin:", font=("Helvetica", 12), bg='#2c3e50', fg='white')
başlık.pack(pady=(20, 5))

artist_id_entry = tk.Entry(pencere, width=40, font=("Helvetica", 12))
artist_id_entry.pack(pady=5)

buton = tk.Button(pencere, text="Playlistleri Göster", command=apicagirma,font=("Helvetica", 12, "bold"), bg="#27ae60", fg="white", padx=10, pady=5)
buton.pack(pady=10)
buton.bind("<Enter>", on_enter)
buton.bind("<Leave>", on_leave)

filtrebaslik = tk.Label(pencere, text="Playlistleri filtrele:", font=("Helvetica", 12), bg='#2c3e50', fg='white')
filtrebaslik.pack(pady=(15, 0))

filtregirdisi = tk.Entry(pencere, width=40, font=("Helvetica", 12))
filtregirdisi.pack(pady=5)

aramabutonu = tk.Button(pencere, text="Ara", command=filtrele, font=("Helvetica", 11))
aramabutonu.pack(pady=5)

liste = tk.Listbox(pencere, width=80, height=15, font=("Helvetica", 10))
liste.pack(pady=10)
liste.bind("<Double-Button-1>", detay_goster)

pencere.mainloop()

print(veri)