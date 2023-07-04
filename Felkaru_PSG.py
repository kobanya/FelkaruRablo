import PySimpleGUI as sg
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

# Képmezők mérete
kepmeret = (80, 80)


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
        kep1 = kep1.resize(kepmeret)
        kep2 = kep2.resize(kepmeret)
        kep3 = kep3.resize(kepmeret)

        # Képek megjelenítése az eredeti helyén
        window["-KEP1-"].update(data=ImageTk.PhotoImage(kep1))
        window["-KEP2-"].update(data=ImageTk.PhotoImage(kep2))
        window["-KEP3-"].update(data=ImageTk.PhotoImage(kep3))

        # A győzelem ellenőrzése
        if szimbolum1 == szimbolum2 == szimbolum3:
            nyeremeny = 1000
            window["-EREDMENY-"].update(f"Nyertél {nyeremeny} kreditet!", text_color="green", font=("Arial", 15, "bold"))
            kreditek += nyeremeny
        elif szimbolum1 == szimbolum2 or szimbolum1 == szimbolum3 or szimbolum2 == szimbolum3:
            nyeremeny = nyeremenyek.get(szimbolum1, 0)  # Vagy nyeremenyek.get(szimbolum2) vagy nyeremenyek.get(szimbolum3)
            window["-EREDMENY-"].update(f"Nyertél {nyeremeny} kreditet!", text_color="orange", font=("Arial", 15, "bold"))
            kreditek += nyeremeny
        else:
            window["-EREDMENY-"].update("Nem nyertél.", text_color="red", font=("Arial", 15, "bold"))

        window["-KREDITEK-"].update(f"Kreditek: {kreditek}")

        # Kreditek ellenőrzése
        if kreditek < 10:
            window["-JATEK-"].update(disabled=True)
            window["-EREDMENY-"].update("Nincs elég kredit a játékhoz.", text_color="red")
    else:
        window["-EREDMENY-"].update("Nincs elég kredit a játékhoz.", text_color="red")


def kilep():
    window.close()


# Elrendezés
layout = [
    [sg.Text("Kettő vagy Három azonos szimbólum nyer.", font=("Arial", 15))],
    [
        sg.Image(filename="arany.png", key="-KEP1-"),
        sg.Image(filename="arany.png", key="-KEP2-"),
        sg.Image(filename="arany.png", key="-KEP3-")
    ],
    [sg.Text("", key="-EREDMENY-", size=(40, 1), font=("Arial", 15, "bold"))],
    [sg.Text(f"Kreditek: {kreditek}", key="-KREDITEK-", font=("Arial", 15))],
    [
        sg.Button("JÁTÉK", key="-JATEK-", size=(30, 2), button_color=("white", "#008000"), disabled=False),
        sg.Button("KILÉP", key="-KILEP-", size=(30, 2), button_color=("white", "#8B0000"))
    ]
]

# Ablak létrehozása
window = sg.Window("Félkarú rabló", layout)

# Eseménykezelés
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "-KILEP-":
        break
    if event == "-JATEK-":
        jatek()

# Ablak bezárása
window.close()
