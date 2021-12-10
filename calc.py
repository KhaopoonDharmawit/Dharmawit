# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outLabel = QtWidgets.QLabel(self.centralwidget)
        self.outLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outLabel.setFont(font)
        self.outLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outLabel.setLineWidth(2)
        self.outLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outLabel.setObjectName("outLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(275, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(275, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 370, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 370, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 370, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("+"))
        self.plusButton.setGeometry(QtCore.QRect(275, 370, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.plus_minus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 460, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(190, 460, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 460, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(275, 460, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def math_it(self):
        screen = self.outLabel.text()
        try:
            answer = eval(screen)
            self.outLabel.setText(str(answer))
        except:
            self.outLabel.setText("ERROR!")

    def plus_minus_it(self):
        screen = self.outLabel.text()
        if "-" in screen:
            self.outLabel.setText(screen.replace("-",""))
        else:
            self.outLabel.setText(f'-{screen}')

    def remove_it(self):
        screen = self.outLabel.text()
        screen = screen[:-1]
        self.outLabel.setText(screen)

    def dot_it(self):
        screen = self.outLabel.text()
        if screen[-1] == ".":
            pass
        else:
            self.outLabel.setText(f'{screen}.')

    def press_it(self, pressed):
        if pressed == "C":
            self.outLabel.setText("0")
        else:
            if self.outLabel.text() == "0":
                self.outLabel.setText("")
            self.outLabel.setText(f'{self.outLabel.text()}{pressed}')
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.equalButton.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
