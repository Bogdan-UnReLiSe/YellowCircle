import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Benefer(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = random.randrange(0, 400)
        y = random.randrange(0, 400)
        d = random.randrange(0, 200)
        qp.drawEllipse(x, y, d, d)

    def paint(self):
        self.do_paint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Benefer()
    ex.show()
    sys.exit(app.exec())
