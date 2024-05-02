from gui.log import *
from gui.reg import *
from gui.home import *
from gui.dep import *
from gui.wit import *
from PyQt6.QtWidgets import *

class Logic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login = LogLogic(self)
        self.dep = DepLogic(self)
        self.wit = WitLogic(self)
        self.home = HomeLogic(self)
        self.reg = RegLogic(self)

    def show_log(self):
        self.close_page()
        self.setCentralWidget(self.login)
        self.login.show()

    def show_reg(self):
        self.close_page()
        self.setCentralWidget(self.reg)
        self.reg.show()

    def show_wit(self):
        self.close_page()
        self.setCentralWidget(self.wit)
        self.wit.show()

    def show_dep(self):
        self.close_page()
        self.setCentralWidget(self.dep)
        self.dep.show()

    def show_home(self):
        self.close_page()
        self.setCentralWidget(self.home)
        self.home.show()

    def close_page(self):
        if self.centralWidget() is not None:
            self.centralWidget().close()


class LogLogic(QMainWindow, Ui_LoginDisplay):
    def __init__(self, Logic):
        super().__init__(Logic)
        self.setupUi(self)
        self.logic = Logic

        self.RegisterButton.clicked.connect(lambda: self.logic.show_reg())
        self.SubmitButton.clicked.connect(lambda: self.validate())
        pass

    def validate(self):
        self.logic.show_home()
        pass
class RegLogic(QMainWindow, Ui_Reg):
    def __init__(self, Logic):
        super().__init__(Logic)
        self.setupUi(self)
        self.logic = Logic

        self.SubmitButton.clicked.connect(lambda: self.logic.show_log())
        self.BackButton.clicked.connect(lambda: self.logic.show_log())
        pass

class HomeLogic(QMainWindow, Ui_Home):
    def __init__(self, Logic):
        super().__init__(Logic)
        self.setupUi(self)
        self.logic = Logic

        self.SignOutButton.clicked.connect(lambda: self.logic.show_log())
        self.WDButton.clicked.connect(lambda: self.logic.show_wit())
        self.DepButton.clicked.connect(lambda: self.logic.show_dep())
        pass

class DepLogic(QMainWindow, Ui_DepWindow):
    def __init__(self, Logic):
        super().__init__(Logic)
        self.setupUi(self)
        self.logic = Logic

        self.BackButton.clicked.connect(lambda: self.logic.show_home())
        pass

class WitLogic(QMainWindow, Ui_Withdraw):
    def __init__(self, Logic):
        super().__init__(Logic)
        self.setupUi(self)
        self.logic = Logic

        self.BackButton_2.clicked.connect(lambda: self.logic.show_home())
        pass
