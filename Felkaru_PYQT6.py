import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap, QPainter, QPen, QImage
from PyQt6.QtCore import Qt, QRect
import random

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


class FelkaruRabloApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Félkarú rabló")
        self.setMinimumSize(600, 250)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Tájékoztató szöveg
        self.szoveg_label = QLabel("Kettő vagy Három azonos szimbólum nyer.")
        self.layout.addWidget(self.szoveg_label)

        # Képmező a három véletlenszerű szimbólum megjelenítésére
        self.mezok_widget = QWidget()
        self.layout.addWidget(self.mezok_widget)

        self.mezok_layout = QHBoxLayout(self.mezok_widget)

        kep1 = QPixmap("arany.png").scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
        kep2 = QPixmap("arany.png").scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
        kep3 = QPixmap("arany.png").scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)

        self.lbl1 = SquareImageLabel(kep1)
        self.mezok_layout.addWidget(self.lbl1)

        self.lbl2 = SquareImageLabel(kep2)
        self.mezok_layout.addWidget(self.lbl2)

        self.lbl3 = SquareImageLabel(kep3)
        self.mezok_layout.addWidget(self.lbl3)

        # Nyertél / Nem nyertél felirat
        self.eredmeny_label = QLabel()
        self.layout.addWidget(self.eredmeny_label)

        # Kreditek számláló
        self.kreditek_label = QLabel(f"Kreditek: {kreditek}")
        self.layout.addWidget(self.kreditek_label)

        # Gombok
        self.gombok_widget = QWidget()
        self.layout.addWidget(self.gombok_widget)

        self.gombok_layout = QHBoxLayout(self.gombok_widget)

        self.jatek_gomb = QPushButton("JÁTÉK")
        self.jatek_gomb.clicked.connect(self.jatek)
        self.jatek_gomb.setStyleSheet("background-color: green;")
        self.jatek_gomb.setFixedSize(400, 60)
        self.gombok_layout.addWidget(self.jatek_gomb)

        self.kilepes_gomb = QPushButton("KILÉP")
        self.kilepes_gomb.clicked.connect(self.kilep)
        self.kilepes_gomb.setStyleSheet("background-color: #8B0000;")
        self.kilepes_gomb.setFixedSize(200, 60)
        self.gombok_layout.addWidget(self.kilepes_gomb)

        if kreditek < 10:
            self.jatek_gomb.setDisabled(True)

    def jatek(self):
        global kreditek

        if kreditek >= 10:
            kreditek -= 10

            # Három véletlenszerű szimbólum generálása
            szimbolum1 = random.choice(szimbolumok)
            szimbolum2 = random.choice(szimbolumok)
            szimbolum3 = random.choice(szimbolumok)

            kep1 = QPixmap(f"{szimbolum1}.png").scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
            kep2 = QPixmap(f"{szimbolum2}.png").scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
            kep3 = QPixmap(f"{szimbolum3}.png").scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)

            self.lbl1.setPixmap(kep1)
            self.lbl2.setPixmap(kep2)
            self.lbl3.setPixmap(kep3)

            # A győzelem ellenőrzése
            if szimbolum1 == szimbolum2 == szimbolum3:
                nyeremeny = 1000
                self.eredmeny_label.setText(f"Nyertél {nyeremeny} kreditet!")
                self.eredmeny_label.setStyleSheet("color: green; font-weight: bold;")
                kreditek += nyeremeny
            elif szimbolum1 == szimbolum2 or szimbolum1 == szimbolum3 or szimbolum2 == szimbolum3:
                nyeremeny = nyeremenyek.get(szimbolum1, 0)
                self.eredmeny_label.setText(f"Nyertél {nyeremeny} kreditet!")
                self.eredmeny_label.setStyleSheet("color: orange; font-weight: bold;")
                kreditek += nyeremeny
            else:
                self.eredmeny_label.setText("Nem nyertél.")
                self.eredmeny_label.setStyleSheet("color: red; font-weight: bold;")

            self.kreditek_label.setText(f"Kreditek: {kreditek}")

            if kreditek < 10:
                self.jatek_gomb.setDisabled(True)
                self.eredmeny_label.setText("Nincs elég kredit a játékhoz.")
                self.eredmeny_label.setStyleSheet("color: red; font-weight: bold;")
        else:
            self.eredmeny_label.setText("Nincs elég kredit a játékhoz.")
            self.eredmeny_label.setStyleSheet("color: red; font-weight: bold;")

    def kilep(self):
        sys.exit()


class SquareImageLabel(QLabel):
    def __init__(self, pixmap):
        super().__init__()
        self.setPixmap(pixmap)
        self.setMinimumSize(150, 150)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = event.rect()
        rect_width = rect.width()
        rect_height = rect.height()

        # Fehér téglalap rajzolása a kép mögött
        painter.setPen(QPen(Qt.GlobalColor.white))
        painter.setBrush(Qt.GlobalColor.white)
        painter.drawRect(rect)

        # Kép középre igazítása
        image_rect = QRect(rect.x() + (rect_width - rect_height) // 2, rect.y(), rect_height, rect_height)

        # Kép kirajzolása
        painter.drawImage(image_rect, self.pixmap().toImage())


app = QApplication([])
window = FelkaruRabloApp()
window.show()
sys.exit(app.exec())
