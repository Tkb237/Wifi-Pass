from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QTableWidgetItem


class TabWidItem(QTableWidgetItem):
    """Erstellen eines benutzerdefinierte QTableWidgetItem, damit der Text zentriert ist"""
    def __init__(self, val):
        super(TabWidItem, self).__init__()
        self.setTextAlignment(Qt.AlignCenter)
        if isinstance(val, str):
            self.setText(val)


class TabWidItemFont(QTableWidgetItem):
    def __init__(self, val):
        super(TabWidItemFont, self).__init__()
        self.setTextAlignment(Qt.AlignCenter)
        font = QFont()
        font.setBold(True)
        self.setFont(font)
        if isinstance(val, str):
            self.setText(val)
