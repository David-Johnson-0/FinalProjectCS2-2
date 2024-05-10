# Imports the gui files and their content as well as the needed libraries
from gui.log import *
from gui.reg import *
from gui.home import *
from gui.dep import *
from gui.wit import *
from PyQt6.QtWidgets import *
import hashlib
import re

class Logic(QMainWindow):
    # Initialization function
    def __init__(self):
        super().__init__()
        self.account = None
    # Opens login screen
    def show_log(self):
        self.login = LogLogic(self)
        self.close_page()
        self.setCentralWidget(self.login)
        self.login.show()
    # Opens registration screen
    def show_reg(self):
        self.reg = RegLogic(self)
        self.close_page()
        self.setCentralWidget(self.reg)
        self.reg.show()
    # Opens withdraw screen
    def show_wit(self):
        self.wit = WitLogic(self)
        self.close_page()
        self.setCentralWidget(self.wit)
        self.wit.show()
    # Opens deposit screen
    def show_dep(self):
        self.dep = DepLogic(self)
        self.close_page()
        self.setCentralWidget(self.dep)
        self.dep.show()
    # Opens home screen
    def show_home(self):
        self.home = HomeLogic(self)
        self.close_page()
        self.setCentralWidget(self.home)
        self.home.show()
    # Closes the current page
    def close_page(self):
        if self.centralWidget() is not None:
            self.centralWidget().close()
    # Hashes the password of the user
    def hash_password(self, password):
        password_bytes = password.encode('utf-8')
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password_bytes)
        hashed_pass = sha256_hash.hexdigest()
        return hashed_pass


class LogLogic(QMainWindow, Ui_LoginDisplay):
    # Initializes the UI and establishes connections.
    def __init__(self, Logic):
        super().__init__(Logic)
        self.setupUi(self)
        self.logic = Logic

        self.RegisterButton.clicked.connect(lambda: self.logic.show_reg())
        self.SubmitButton.clicked.connect(lambda: self.validate())
        pass
    # Reads the email and validates that the email is in the text file (a registered user).
    def validate(self):
        email = self.usernameinput.text()
        with open('files/login_info.txt', 'r') as file:
            for line in file:
                if line.startswith(email):
                    content = line.split()
                    if content[1] == self.logic.hash_password(self.pwinput.text()):
                        self.logic.account = content[0]
                        self.logic.show_home()
                    else:
                        self.pwinput.clear()
                        self.usernameinput.clear()
                        self.setfocus(self.usernameinput)

class RegLogic(QMainWindow, Ui_Reg):
    # Initializes screen and establshes connections
    def __init__(self, Logic):
        super().__init__(Logic)
        self.setupUi(self)
        self.logic = Logic

        self.SubmitButton.clicked.connect(lambda: self.register())
        self.BackButton.clicked.connect(lambda: self.logic.show_log())
        pass
    # Takes in the email and password the user enters and, if the passwords match, adds them to the text file.
    # Otherwise, the inputs are reset and the user must input again.
    def register(self):
        email = self.EmailInput.text()
        pass1 = self.PWInput.text()
        pass2 = self.PWInput2.text()
        if self.val_inputs():
            if pass1 == pass2:
                with open('files/login_info.txt', 'a') as file:
                    file.write(f'{email} {self.logic.hash_password(pass1)} {self.DOBInput.text()} {self.FNameInput.text()} {self.LNameInput.text()}\n')
                    self.logic.show_log()
            else:
                self.PWInput.setText(None)
                self.PWInput2.setText(None)
                self.EmailInput.setText(None)
                self.DOBInput.setText(None)
                self.LNameInput.setText(None)
                self.FNameInput.setText(None)
                self.setfocus(self.FNameInput)
        else:
            pass
    # Validates the inputs, ensuring the formatting is accurate and the passwords are valid.
    def val_inputs(self):
        if self.is_empty(self.PWInput.text()):
            return False
        if self.is_empty(self.PWInput2.text()):
            return False
        if self.is_empty(self.LNameInput.text()):
            return False
        if self.is_empty(self.FNameInput.text()):
            return False
        if self.is_empty(self.EmailInput.text()):
            return False
        if self.is_empty(self.DOBInput.text()):
            return False
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
        if not re.match(pattern, self.EmailInput.text()):
            return False
        return True
    # Checks if input is empty.
    def is_empty(self, name):
        if name == "":
            return True
        else:
            return False

class HomeLogic(QMainWindow, Ui_Home):
    # Initializes home screen and establishes button connections (where the user goes with each button
    def __init__(self, Logic):
        super().__init__(Logic)
        self.setupUi(self)
        self.logic = Logic
        with open("files/login_info.txt", 'r') as file:
            for line in file:
                if line.startswith(self.logic.account):
                    row = line.split()
                    self.SavingButton.setText(f'{row[3]}\'s Saving Account')
                    self.CheckButton.setText(f'{row[3]}\'s Checking Account')

        self.SignOutButton.clicked.connect(lambda: self.logic.show_log())
        self.WDButton.clicked.connect(lambda: self.logic.show_wit())
        self.DepButton.clicked.connect(lambda: self.logic.show_dep())
        pass

class DepLogic(QMainWindow, Ui_DepWindow):
    # Initializes deposit page
    def __init__(self, Logic):
        super().__init__(Logic)
        self.setupUi(self)
        self.logic = Logic

        self.BackButton.clicked.connect(lambda: self.logic.show_home())
        pass

class WitLogic(QMainWindow, Ui_Withdraw):
    # Initializes withdraw page
    def __init__(self, Logic):
        super().__init__(Logic)
        self.setupUi(self)
        self.logic = Logic

        self.BackButton_2.clicked.connect(lambda: self.logic.show_home())
        pass
