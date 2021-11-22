from PyQt5 import QtWidgets, QtGui, QtCore, Qt
import sys

app = QtWidgets.QApplication(sys.argv)
win = QtWidgets.QMainWindow()
f = QtWidgets.QFileDialog()
win.setCentralWidget(f)
win.resize(300,200)
win.show()
app.exec_()