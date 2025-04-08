import webbrowser

print("")
print("OSİNT MASTER PROFESSİONAL TOOL's")
print("")
print("[01] >> TEST SİTESİNİ AÇ")
choice = input("Bir seçenek girin: ")

# 1. seçenek seçildiğinde YouTube'u aç
if choice == "1":
    webbrowser.open("https://www.youtube.com")
    print("YouTube açılıyor...")
else:
    print("Geçersiz seçenek.")
