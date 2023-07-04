import tkinter as tk
import random
from PIL import Image, ImageTk

# Szimbólumok listája
szimbolumok = ["hetes", "csengo", "cseresznye", "gyemant", "eper", "arany", "narancs", "dinnye", "citrom", "medal"]

# Nyeremények
nyeremenyek = {
    "hetes": 100,
    "csengo": 50,
    "cseresznye": 20,
    "gyemant": 60,
    "eper": 10,
    "arany": 90,
    "narancs": 30,
    "dinnye": 40,
    "citrom": 10,
    "medal": 70
}

# Kezdő kreditek
kreditek = 100


def jatek():
    global kreditek

    if kreditek >= 10:
        kreditek -= 10

        # Három véletlenszerű szimbólum generálása
        szimbolum1 = random.choice(szimbolumok)
        szimbolum2 = random.choice(szimbolumok)
        szimbolum3 = random.choice(szimbolumok)

        # Szimbólum képek betöltése
        kep1 = Image.open(f"{szimbolum1}.png")
        kep2 = Image.open(f"{szimbolum2}.png")
        kep3 = Image.open(f"{szimbolum3}.png")

        # Képek méretezése
        kep1 = kep1.resize((150, 150))
        kep2 = kep2.resize((150, 150))
        kep3 = kep3.resize((150, 150))

        # Képek megjelenítése az eredeti helyén
        kep1_tk = ImageTk.PhotoImage(kep1)
        kep2_tk = ImageTk.PhotoImage(kep2)
        kep3_tk = ImageTk.PhotoImage(kep3)

        lbl1.configure(image=kep1_tk)
        lbl2.configure(image=kep2_tk)
        lbl3.configure(image=kep3_tk)

        lbl1.image = kep1_tk
        lbl2.image = kep2_tk
        lbl3.image = kep3_tk

        # A győzelem ellenőrzése
        if szimbolum1 == szimbolum2 == szimbolum3:
            nyeremeny = 1000
            eredmeny_label.config(text=f"Nyertél {nyeremeny} kreditet!", fg="green", font=("Arial", 15, "bold"))
            kreditek += nyeremeny
        elif szimbolum1 == szimbolum2 or szimbolum1 == szimbolum3 or szimbolum2 == szimbolum3:
            nyeremeny = nyeremenyek.get(szimbolum1, 0)  # Vagy nyeremenyek.get(szimbolum2) vagy nyeremenyek.get(szimbolum3)
            eredmeny_label.config(text=f"Nyertél {nyeremeny} kreditet!", fg="orange", font=("Arial", 15, "bold"))

            kreditek += nyeremeny
        else:
            eredmeny_label.config(text="Nem nyertél.", fg="red",font=("Arial", 15, "bold"))

        kreditek_label.config(text=f"Kreditek: {kreditek}")

        # Kreditek ellenőrzése
        if kreditek < 10:
            jatek_gomb.config(state=tk.DISABLED,bg='grey')
            eredmeny_label.config(text="Nincs elég kredit a játékhoz.", fg="red")
    else:
        eredmeny_label.config(text="Nincs elég kredit a játékhoz.", fg="red")


def kilep():
    ablak.quit()


# Főablak létrehozása
ablak = tk.Tk()
ablak.title("Félkarú rabló")
ablak.minsize(width=700, height=300)

# Tájékoztató szöveg
szoveg_label = tk.Label(ablak, text="Kettő vagy Három azonos szimbólum nyer.")
szoveg_label.pack(pady=10)

# Képmező a három véletlenszerű szimbólum megjelenítésére
mezok = tk.Frame(ablak)
mezok.pack(pady=10)

kep1 = Image.open("arany.png")
kep2 = Image.open("arany.png")
kep3 = Image.open("arany.png")

kep1 = kep1.resize((150, 150))
kep2 = kep2.resize((120, 150))
kep3 = kep3.resize((150, 150))

kep1_tk = ImageTk.PhotoImage(kep1)
kep2_tk = ImageTk.PhotoImage(kep2)
kep3_tk = ImageTk.PhotoImage(kep3)

lbl1 = tk.Label(mezok, image=kep1_tk)
lbl1.pack(side=tk.LEFT, padx=10)

lbl2 = tk.Label(mezok, image=kep2_tk)
lbl2.pack(side=tk.LEFT, padx=10)

lbl3 = tk.Label(mezok, image=kep3_tk)
lbl3.pack(side=tk.LEFT, padx=10)

# Nyertél / Nem nyertél felirat
eredmeny_label = tk.Label(ablak, text="")
eredmeny_label.pack(pady=10)

# Kreditek számláló
kreditek_label = tk.Label(ablak, text=f"Kreditek: {kreditek}")
kreditek_label.pack(pady=10)

# Gombok
gombok_frame = tk.Frame(ablak)
gombok_frame.pack(pady=10)

jatek_gomb = tk.Button(gombok_frame, text="JÁTÉK", command=jatek, bg="green", width=40, height=4, activebackground="yellow")
kilepes_gomb = tk.Button(gombok_frame, text="KILÉP", command=kilep, bg="#8B0000", height=4, activebackground="red")
kilepes_gomb.pack(side=tk.LEFT, padx=10)

if kreditek >= 10:
    jatek_gomb.pack(side=tk.LEFT, padx=10)

# Ablak megjelenítése
ablak.mainloop()
