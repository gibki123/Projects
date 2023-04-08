import sys
from PySide2.QtGui import QPainter, QPen
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtWinExtras import QtWin
from PySide2.QtCore import Qt


class BoundingBox():
    def __init__(self, pos_x, pos_y, width, height, category):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.category = category

class TranslucentApp(QMainWindow):

    def __init__(self, rects):
        super().__init__()
        self.rectangles = rects
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background:transparent")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowState(Qt.WindowMaximized);
        self.show()

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        for rectangle in self.rectangles:
            self.draw_rectangle(painter, rectangle)
        painter.end()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def draw_rectangle(self, painter, bBox):
        pen = QPen(Qt.yellow, 4, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawRect(bBox.pos_x, bBox.pos_y, bBox.width, bBox.height)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     rects = [BoundingBox(20, 20, 400, 100, 1), BoundingBox(40, 40, 100, 400, 1)]
#     window = TranslucentApp(rects)
#     sys.exit(app.exec_())
