# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(400, 800)
        Home.setMinimumSize(QtCore.QSize(400, 800))
        Home.setMaximumSize(QtCore.QSize(400, 800))
        self.centralwidget = QtWidgets.QWidget(parent=Home)
        self.centralwidget.setObjectName("centralwidget")
        self.DepButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.DepButton.setGeometry(QtCore.QRect(40, 350, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DepButton.setFont(font)
        self.DepButton.setObjectName("DepButton")
        self.HomeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.HomeLabel.setGeometry(QtCore.QRect(120, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HomeLabel.setFont(font)
        self.HomeLabel.setObjectName("HomeLabel")
        self.WDButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.WDButton.setGeometry(QtCore.QRect(240, 350, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.WDButton.setFont(font)
        self.WDButton.setObjectName("WDButton")
        self.CheckButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.CheckButton.setGeometry(QtCore.QRect(40, 220, 250, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CheckButton.setFont(font)
        self.CheckButton.setObjectName("CheckButton")
        self.SavingButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.SavingButton.setGeometry(QtCore.QRect(40, 100, 250, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SavingButton.setFont(font)
        self.SavingButton.setObjectName("SavingButton")
        self.SignOutButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SignOutButton.setGeometry(QtCore.QRect(50, 600, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SignOutButton.setFont(font)
        self.SignOutButton.setObjectName("SignOutButton")
        Home.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Home)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        Home.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Home)
        self.statusbar.setObjectName("statusbar")
        Home.setStatusBar(self.statusbar)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Home"))
        self.DepButton.setText(_translate("Home", "Deposit"))
        self.HomeLabel.setText(_translate("Home", "List of Accounts"))
        self.WDButton.setText(_translate("Home", "Withdraw"))
        self.CheckButton.setText(_translate("Home", "Checking Account"))
        self.SavingButton.setText(_translate("Home", "Savings Account"))
        self.SignOutButton.setText(_translate("Home", "Sign Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Home = QtWidgets.QMainWindow()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
    sys.exit(app.exec())
