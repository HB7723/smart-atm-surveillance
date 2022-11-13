from PyQt5 import QtCore, QtWidgets

from ui import Ui_MainWindow

danger = 0


class WorkerThread(QtCore.QThread):
    ##signal##
    signal = QtCore.pyqtSignal(list, name="signal1")

    def __init__(self, parent=None):
        super(WorkerThread, self).__init__(parent)

    def run(self):
        global danger

        danger = 1

        self.signal.emit([danger])


class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    signal = QtCore.pyqtSignal(str)
