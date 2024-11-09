from PySide6.QtCore import QSize
from PySide6.QtGui import Qt, QIcon, QPixmap
from PySide6.QtWidgets import QFrame, QApplication, QLabel, QPushButton


class TitelBar(QFrame):
    def __init__(self, parent=None):
        super(TitelBar, self).__init__()
        self.setObjectName("tkb")
        # titel bar geometry
        self.setMinimumWidth(300)
        self.setFixedHeight(40)
        # Titelbar element
        self.app_name = QLabel(self)
        self.setParent(parent)
        # app ico
        self.app_ico = QLabel(self)
        self.app_ico.setPixmap(QPixmap("Ico/wifi.svg"))
        self.app_ico.setAlignment(Qt.AlignCenter)
        self.app_ico.setObjectName("name")
        self.app_ico.setStyleSheet(""" QLabel#name{background-color: none;
                                        border: none;
                                        border-radius: 0;
                                        border-top-left-radius: 12px;
                                        }
                                        """)
        self.app_ico.setGeometry(5, 0, 41, 41)

        # app name
        self.app_name.setGeometry(60, 0, 175, 41)
        self.app_name.setText("Wi-Fi Pass by Tkb")
        self.app_name.setStyleSheet("""font: 70 15pt "MS Shell Dlg 2";
                                        color: rgb(255, 255, 255)""")
        # btn close
        self.btn_close = QPushButton(self)
        self.btn_close.setObjectName("close")
        self.btn_close.setFlat(True)
        self.btn_close.setGeometry(self.width() - 40, 0, 41, 41)
        self.btn_close.setIcon(QIcon("Ico/close.svg"))
        self.btn_close.setIconSize(QSize(20, 20))
        # btn reduce
        self.btn_reduce = QPushButton(self)
        self.btn_reduce.setFlat(True)
        self.btn_reduce.setGeometry(self.width() - 80, 0, 41, 41)
        self.btn_reduce.setIcon(QIcon("Ico/minus.svg"))
        self.btn_reduce.setIconSize(QSize(20, 20))
        # set style sheet
        with open(r"StyleSheet/titel_bar_css.css", "r") as ss:
            self.setStyleSheet(ss.read())
        # move frameless window
        self.parent().mousePressEvent = self.win_move

    def mouseMoveEvent(self, event):
        if not self.parent().isMaximized() and event.buttons() == Qt.LeftButton:
            self.parent().move(self.parent().pos() + event.globalPos() - self.parent().clickPosition)
            self.parent().clickPosition = event.globalPos()
            event.accept()
            pass

    def win_move(self, event):
        self.parent().clickPosition = event.globalPos()
        pass

    def resizeEvent(self, event):
        self.btn_close.setGeometry(self.width() - 40, 0, 41, 41)
        self.btn_reduce.setGeometry(self.width() - 80, 0, 41, 41)
        self.update()
