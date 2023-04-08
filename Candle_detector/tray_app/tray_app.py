import os
import sys
import pyscreenshot as pssht
import pathlib
import cv2
import drawer
from PySide2 import QtWidgets, QtGui
from PIL import Image
from darknet_facade import load_darknet, detect_candles


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    """
    CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
    """
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip('Candle Detector version 0.1')
        menu = QtWidgets.QMenu(parent)

        open_app = menu.addAction("Run single prediction")
        open_app.triggered.connect(self.single_prediction)
        open_app.setIcon(QtGui.QIcon("icon.png"))

        open_cal = menu.addAction("Run regular predictions")
        open_cal.triggered.connect(self.regular_predictions)
        open_cal.setIcon(QtGui.QIcon("icon.png"))

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: sys.exit())
        exit_.setIcon(QtGui.QIcon("icon.png"))

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        
        pass

    def single_prediction(self):
        screenshot = pssht.grab()
        image_name = 'screen_candle.png'
        screenshot.save(image_name)
        img_path = os.path.join(pathlib.Path().absolute(), image_name)
        predictions = detect_candles()

    def regular_predictions(self):
        """
        this function will open application
        :return:
        """
        pass


def main():
    load_darknet()
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icon.png"), w)
    tray_icon.show()
    tray_icon.showMessage('Candle Generator', 'Hello, Lets detect some candles!!!')
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
