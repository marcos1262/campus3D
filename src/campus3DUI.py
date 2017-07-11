# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, mainWindow, glWindow):
        mainWindow.setObjectName("MainWindow")
        mainWindow.resize(1300, 700)
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        # self.centralWidget.resizeEvent = (self.resizeEvent)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.centralWidget.setPalette(palette)

        self.painel_jogo = QtWidgets.QWidget(self.centralWidget)
        self.painel_jogo.setGeometry(QtCore.QRect(0, 0, 1300, 700))
        self.painel_jogo.setObjectName("painel_jogo")

        self.jogo = glWindow(self.painel_jogo)
        self.jogo.setGeometry(QtCore.QRect(0, 0, 1300, 700))
        self.jogo.setObjectName("jogo")

        # self.labelTickets = QtWidgets.QLabel(self.painel_jogo)
        # self.labelTickets.setEnabled(True)
        # self.labelTickets.setGeometry(QtCore.QRect(10, 10, 154, 17))
        # self.labelTickets.setObjectName("labelPontos")
        #
        # self.labelTempo = QtWidgets.QLabel(self.painel_jogo)
        # self.labelTempo.setEnabled(True)
        # self.labelTempo.setGeometry(QtCore.QRect(10, 30, 154, 17))
        # self.labelTempo.setObjectName("labelNivel")

        self.labelCenter = QtWidgets.QLabel(self.painel_jogo)
        self.labelCenter.setEnabled(True)
        self.labelCenter.setGeometry(QtCore.QRect(550, 340, 200, 20))
        self.labelCenter.setObjectName("labelCenter")

        self.jogo.raise_()
        # self.labelTickets.raise_()
        # self.labelTempo.raise_()
        self.labelCenter.raise_()
        self.painel_jogo.raise_()
        mainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.jogo.setFocus()

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.labelTickets.setText(_translate("MainWindow", ""))
        # self.labelTempo.setText(_translate("MainWindow", ""))
        self.labelCenter.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, QtWidgets.QOpenGLWidget)
    MainWindow.show()
    sys.exit(app.exec_())
