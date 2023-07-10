import tkinter as tk
from tkinter import ttk, END
from PIL import ImageTk, Image

def sabit_faiz(anapara, oran, sure):
    faiz = anapara * oran * sure
    toplam = anapara + faiz
    return toplam

def hesapla():
    if not ana_para_entry.get() or not faiz_orani_entry.get() or not yatirim_suresi_entry.get():
        sonuc_label.config(text="Lütfen tüm alanları doldurun.", foreground="red")
        return

    try:
        anapara = float(ana_para_entry.get())
        oran = float(faiz_orani_entry.get()) / 100
        sure = int(yatirim_suresi_entry.get())
    except ValueError:
        sonuc_label.config(text="Lütfen geçerli sayısal değerler girin.", foreground="red")
        return

    secim = int(yatirim_secim.get())

    if secim == 1:
        toplam = sabit_faiz(anapara, oran, sure)
        sonuc_label.config(text=f"Toplam miktar: {toplam}TL")
    elif secim == 2:
        birikim = faizli_birikim(anapara, oran, sure)
        sonuc_label.config(text=f"Birikim miktarı: {birikim}")
    else:
        sonuc_label.config(text="Geçersiz seçim!")


def Temizle():
    ana_para_entry.delete(0, END)
    faiz_orani_entry.delete(0, END)
    yatirim_suresi_entry.delete(0, END)
    sonuc_label.config(text="")


pencere = tk.Tk()
pencere.title("Yatırım Karşılaştırma Arayüzü")
pencere.geometry("400x450")
pencere.config(bg="#FFFFFF")

arka_plan_resim = ImageTk.PhotoImage(Image.open("Yatirim.png"))
arka_plan_label = tk.Label(pencere, image=arka_plan_resim)
arka_plan_label.place(x=0, y=0, relwidth=1, relheight=1)

yatirim_secim_label = ttk.Label(pencere, text="Yatırım Aracı Seçin:", background="#FFFFFF", foreground="#000000", font=("Arial", 12, "bold"))
yatirim_secim_label.pack(pady=10)

yatirim_secim = tk.StringVar()
yatirim_secim.set("1")

radio_button_frame = ttk.Frame(pencere)
radio_button_frame.pack()

radio_button1 = ttk.Radiobutton(radio_button_frame, text="Sabit Faizli Yatırım", variable=yatirim_secim, value="1", style="TRadiobutton")
radio_button1.pack(anchor=tk.W, pady=5)

radio_button2 = ttk.Radiobutton(radio_button_frame, text="Faizli Birikim", variable=yatirim_secim, value="2", style="TRadiobutton")
radio_button2.pack(anchor=tk.W, pady=5)

ana_para_label = ttk.Label(pencere, text="Ana Para:", background="#FFFFFF", foreground="#000000", font=("Arial", 12, "bold"))
ana_para_label.pack(pady=10)

ana_para_entry = ttk.Entry(pencere, font=("Arial", 12))
ana_para_entry.pack()

faiz_orani_label = ttk.Label(pencere, text="Faiz Oranı (%):", background="#FFFFFF", foreground="#000000", font=("Arial", 12, "bold"))
faiz_orani_label.pack(pady=10)

faiz_orani_entry = ttk.Entry(pencere, font=("Arial", 12))
faiz_orani_entry.pack()

yatirim_suresi_label = ttk.Label(pencere, text="Yatırım Süresi (yıl):", background="#FFFFFF", foreground="#000000", font=("Arial", 12, "bold"))
yatirim_suresi_label.pack(pady=10)

yatirim_suresi_entry = ttk.Entry(pencere, font=("Arial", 12))
yatirim_suresi_entry.pack()

hesapla_button = ttk.Button(pencere, text="Hesapla", command=hesapla, style="TButton")
hesapla_button.pack(pady=10)

temizle_button = ttk.Button(pencere, text="Temizle", command=Temizle, style="TButton")
temizle_button.pack(pady=10)

sonuc_label = ttk.Label(pencere, text="", background="#FFFFFF", foreground="#000000", font=("Arial", 12, "bold"))
sonuc_label.pack(pady=10)

pencere.mainloop()
