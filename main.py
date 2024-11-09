from PySide6.QtCore import Qt, QThread
from PySide6.QtGui import QPainter, QBrush, QColor, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QVBoxLayout, QAbstractItemView
from WifiPass.Wifi_pass import get_wifi_list, get_wifi_inf
from TextAlign.Text_align import TabWidItem, TabWidItemFont
from TitelBar.Title_bar import TitelBar
import wifi_qrcode_generator as qr
from GegenFreezeThread.freeze import Thread
from pathlib import Path

MAIN = Path.cwd()/"QrCodeWifi"


class WifiPass(QWidget):
    def __init__(self):
        super(WifiPass, self).__init__()
        # Custom Main Win
        self.setWindowIcon(QIcon("Ico/wifi.svg"))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setObjectName("Tkb")
        self.setWindowOpacity(0.9)
        # set StyleSheet
        with open("StyleSheet/main_css.css", "r") as ss:
            self.setStyleSheet(ss.read())
        # Erstellen der benutzerdefinierte Titelleiste
        self.titel_leiste = TitelBar(self)
        self.setGeometry(100, 100, 800, 300)

        # Erstellen der Haupttabelle
        self.tab_wifi = QTableWidget()

        self.setup_ui()
        self.tab_voll()
        self.custom_table()

    def setup_ui(self):
        # Schlachtfläche erstellen
        btn_update = QPushButton("Aktualisieren")
        btn_update.setObjectName("update")
        # Erstellen des HauptLayouts
        main_lay = QVBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)
        # Hinzufügen von Widgets zu der Tabelle
        main_lay.addWidget(self.titel_leiste)
        main_lay.addWidget(self.tab_wifi)
        main_lay.addWidget(btn_update)
        # Festlegen des Hauptlayouts
        self.setLayout(main_lay)
        # thread
        th = Thread(self.tab_voll)
        # connect button
        btn_update.clicked.connect(lambda: th.start())
        self.titel_leiste.btn_reduce.clicked.connect(self.reduce_win)
        self.titel_leiste.btn_close.clicked.connect(self.close_win)

    def custom_table(self):
        # Header festlegen
        wifi_header = ["#", "SSID", "Authentifizierung", "Sicherheitsschlüssel", "Passwort"]
        self.tab_wifi.setHorizontalHeaderLabels(wifi_header)
        # vertical Header entfernen
        self.tab_wifi.verticalHeader().setVisible(False)
        # Reihe stretch
        self.tab_wifi.verticalHeader().setStretchLastSection(True)
        self.tab_wifi.horizontalHeader().setStretchLastSection(True)
        self.tab_wifi.horizontalHeader().setSortIndicatorShown(True)
        self.tab_wifi.setSortingEnabled(True)
        # Größe festlegen
        self.tab_wifi.horizontalHeader().setDefaultSectionSize(160)
        self.tab_wifi.verticalHeader().setDefaultSectionSize(65)
        # color alternate
        self.tab_wifi.setAlternatingRowColors(False)
        self.tab_wifi.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tab_wifi.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tab_wifi.setAlternatingRowColors(True)
        # scroll bar
        self.tab_wifi.verticalScrollBar().setFixedWidth(10)
        with open(r"StyleSheet/table.css", "r") as ss:
            self.tab_wifi.setStyleSheet(ss.read())

    def tab_voll(self):
        # Wi-fi Informationen
        wifi_inf = get_wifi_inf()
        wifi_name = get_wifi_list()
        wifi_sec_type = [sec_type.replace(" ", "") for sec_type in wifi_inf[0]]
        wifi_pass = wifi_inf[1]
        wifi_auth = wifi_inf[2]
        # Ausfüllen der Tabelle
        self.tab_wifi.setRowCount(len(wifi_name))
        self.tab_wifi.setColumnCount(5)
        for i in range(len(wifi_name)):
            self.tab_wifi.setItem(i, 0, TabWidItemFont(f"{i + 1}"))
        for name in wifi_name:
            self.tab_wifi.setItem(wifi_name.index(name), 1, TabWidItem(name))
        j = 0
        for auth in wifi_auth:
            self.tab_wifi.setItem(j, 2, TabWidItem(auth))
            j += 1
        j = 0
        for sec_type in wifi_sec_type:
            self.tab_wifi.setItem(j, 3, TabWidItem(sec_type))
            j += 1

        j = 0
        for pass_wort in wifi_pass:
            self.tab_wifi.setItem(j, 4, TabWidItem(pass_wort))
            j += 1

        # #################### Generate Qr Code ########################################
        MAIN.mkdir(exist_ok=True)
        for i in range(len(wifi_name)):
            name = wifi_name[i]
            auth = wifi_auth[i]
            pass_w = wifi_pass[i]
            if auth != "Ouvert":
                qr_code = qr.wifi_qrcode(name, False, "WPA", pass_w)
                qr_code.make_image().save(f"QrCodeWifi/{name}_wifi_qr_tkb.png")
            else:
                qr_code = qr.wifi_qrcode(name, False, "nopass")
                qr_code.make_image().save(f"QrCodeWifi/{name}_wifi_qr_tkb.png")
    def generateQrCode(self):
        sender
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # use to modify the shape of the window
        rect = self.rect()
        painter.setPen(Qt.NoPen)
        brush = QBrush(QColor("#2c3034"))
        painter.setBrush(brush)
        painter.drawRoundedRect(rect, 12, 12)

        painter.end()

    def close_win(self):
        self.close()

    def reduce_win(self):
        self.showMinimized()


app = QApplication([])

main = WifiPass()
main.show()

app.exec()
