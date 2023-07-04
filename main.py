import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

# Szimbólumok listája
szimbolumok = ["hetes", "csengo", "cseresznye", "gyemant", "eper", "arany", "narancs", "dinnye", "citrom", "medál"]

def jatek():
    # Három véletlenszerű szimbólum generálása
    szimbolum1 = random.choice(szimbolumok)
    szimbolum2 = random.choice(szimbolumok)
    szimbolum3 = random.choice(szimbolumok)

    # Szimbólum képek betöltése
    kep1 = Image.open(f"{szimbolum1}.png")
    kep2 = Image.open(f"{szimbolum2}.png")
    kep3 = Image.open(f"{szimbolum3}.png")

    # Képek méretezése
    kep1 = kep1.resize((100, 100))
    kep2 = kep2.resize((100, 100))
    kep3 = kep3.resize((100, 100))

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
        eredmeny_label.config(text="Nyertél!")
    elif szimbolum1 == szimbolum2 or szimbolum1 == szimbolum3 or szimbolum2 == szimbolum3:
        eredmeny_label.config(text="Szerencsés vagy!")
    else:
        eredmeny_label.config(text="Nem nyertél.")

def kilép():
    root.quit()

# Főablak létrehozása
root = tk.Tk()
root.title("Félkarú rabló")

# Tájékoztató szöveg
szoveg_label = tk.Label(root, text="Három azonos szimbólum nyer.")
szoveg_label.pack(pady=10)

# Képmező a három véletlenszerű szimbólum megjelenítésére
mezok = tk.Frame(root)
mezok.pack(pady=10)

kep1 = Image.open("arany.png")
kep2 = Image.open("arany.png")
kep3 = Image.open("arany.png")

kep1 = kep1.resize((100, 100))
kep2 = kep2.resize((100, 100))
kep3 = kep3.resize((100, 100))

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
eredmeny_label = tk.Label(root, text="")
eredmeny_label.pack(pady=10)

# Gombok
gombok_frame = tk.Frame(root)
gombok_frame.pack(pady=10)

jatek_gomb = tk.Button(gombok_frame, text="JÁTÉK", command=jatek)
jatek_gomb.pack(side=tk.LEFT, padx=10)

kilepes_gomb = tk.Button(gombok_frame, text="KILÉP", command=kilép)
kilepes_gomb.pack(side=tk.LEFT, padx=10)

# Ablak megjelenítése
root.mainloop()
