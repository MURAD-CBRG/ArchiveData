from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import datetime as dt
import shutil


class ArchiveReserveProgram(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('utility_interface.ui', self)

        self.setFixedSize(self.width(), self.height())

        self.statusBar().showMessage('Программа готова к использованию')

        self.btn_create.clicked.connect(self.create_copy)

    def create_copy(self):
        shutil.make_archive(f'{self.enter_place.text()}/{str(dt.datetime.now())}', 'zip',
                            root_dir=self.enter_source.text())

        self.statusBar().showMessage('Резервная копия создана')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ArchiveReserveProgram()
    window.show()
    sys.exit(app.exec())
