from PySide6.QtCore import QThread


class Thread(QThread):
    def __init__(self, func):
        super(Thread, self).__init__()
        self.func = func

    def run(self) -> None:
        self.func()

