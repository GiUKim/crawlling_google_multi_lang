
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.acceptDrops()
        self.setWindowTitle('image')
        self.setGeometry(0,0,400,300)
        self.label=QLabel(self)
        self.pixmap = QPixmap('image.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        self.show()
def button_clicked():
    print('button')

app = QApplication([])
app.setStyle('fusion')
window = Window()
app.exec()
