from gui.log import *
from gui.reg import *
from gui.home import *
from gui.dep import *
from gui.wit import *
from PyQt6.QtWidgets import *
import hashlib
import re
import csv

class Logic(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.account = None
        self.type = ''

    def show_log(self) -> None:
        self.login = LogLogic(self)
        self.close_page()
        self.setCentralWidget(self.login)
        self.login.show()

    def show_reg(self) -> None:
        self.reg = RegLogic(self)
        self.close_page()
        self.setCentralWidget(self.reg)
        self.reg.show()

    def show_wit(self) -> None:
        self.wit = WitLogic(self)
        self.close_page()
        self.setCentralWidget(self.wit)
        self.wit.show()

    def show_dep(self) -> None:
        self.dep = DepLogic(self)
        self.close_page()
        self.setCentralWidget(self.dep)
        self.dep.show()

    def show_home(self) -> None:
        self.home = HomeLogic(self)
        self.close_page()
        self.setCentralWidget(self.home)
        self.home.show()

    def close_page(self) -> None:
        if self.centralWidget() is not None:
            self.centralWidget().close()

    def hash_password(self, password) -> str:
        password_bytes = password.encode('utf-8')
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password_bytes)
        hashed_pass = sha256_hash.hexdigest()
        return hashed_pass


class LogLogic(QMainWindow, Ui_LoginDisplay):
    def __init__(self, Logic) -> None:
        super().__init__(Logic)
        self.setupUi(self)
        self.logic = Logic

        self.RegisterButton.clicked.connect(lambda: self.logic.show_reg())
        self.SubmitButton.clicked.connect(lambda: self.validate())
        pass

    def validate(self) -> None:
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
                        self.usernameinput.setFocus()

class RegLogic(QMainWindow, Ui_Reg):
    def __init__(self, Logic) -> None:
        super().__init__(Logic)
        self.setupUi(self)
        self.logic = Logic

        self.SubmitButton.clicked.connect(lambda: self.register())
        self.BackButton.clicked.connect(lambda: self.logic.show_log())
        pass
    def register(self) -> None:
        email = self.EmailInput.text()
        pass1 = self.PWInput.text()
        pass2 = self.PWInput2.text()
        if self.val_inputs():
            if pass1 == pass2:
                with open('files/login_info.txt', 'a') as file:
                    file.write(f'{email} {self.logic.hash_password(pass1)} {self.DOBInput.text()} {self.FNameInput.text()} {self.LNameInput.text()}\n')
                    self.gen_csv()
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
    def val_inputs(self) -> bool:
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
    def is_empty(self, name) -> bool:
        if name == "":
            return True
        else:
            return False
    def gen_csv(self) -> None:
        with open('files/account_info.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f'{self.EmailInput.text()}-Save', 0])
            writer.writerow([f'{self.EmailInput.text()}-Check', 0])


class HomeLogic(QMainWindow, Ui_Home):
    def __init__(self, Logic) -> None:
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
        self.WDButton.clicked.connect(lambda: self.get_checked())
        self.WDButton.clicked.connect(lambda: self.logic.show_wit())
        self.DepButton.clicked.connect(lambda: self.get_checked())
        self.DepButton.clicked.connect(lambda: self.logic.show_dep())
        pass

    def get_checked(self) -> None:
        if self.SavingButton.isChecked():
            self.logic.type = '-Save'
        elif self.CheckButton.isChecked():
            self.logic.type = '-Check'
        else:
            pass

class DepLogic(QMainWindow, Ui_DepWindow):
    def __init__(self, Logic) -> None:
        super().__init__(Logic)
        self.setupUi(self)
        self.logic = Logic
        self.DepButton.clicked.connect(lambda: self.deposit())
        self.BackButton.clicked.connect(lambda: self.logic.show_home())
        pass

    def deposit(self) -> None:
        with open('files/account_info.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for row in rows:
                if f'{row[0]}' == f'{self.logic.account}{self.logic.type}':
                    if self.DepLabel.text() == self.DepInput2.text():
                        row[1] = int(row[1]) + int(self.DepInput2.text())
                        self.DepLabel.setText('')
                        self.DepLabel.setPlaceholderText(f'${row[1]}')
                        break

        with open('files/account_info.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        self.DepInput2.setText('')

class WitLogic(QMainWindow, Ui_Withdraw):
    def __init__(self, Logic) -> None:
        super().__init__(Logic)
        self.setupUi(self)
        self.logic = Logic
        self.WitButton.clicked.connect(lambda: self.withdraw())
        self.BackButton_2.clicked.connect(lambda: self.logic.show_home())
        pass
    def withdraw(self) -> None:
        with open('files/account_info.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for row in rows:
                if f'{row[0]}' == f'{self.logic.account}{self.logic.type}':
                    if self.WitLabel_2.text() == self.WitInput2.text():
                        if (int(row[1]) - int(self.WitInput2.text())) > 0:
                            row[1] = int(row[1]) - int(self.WitInput2.text())
                            self.WitLabel_2.setText('')
                            self.WitLabel_2.setPlaceholderText(f'${row[1]}')
                            allow = True
                        else:
                            allow = False
                            continue
        if allow:
            with open('files/account_info.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
        self.WitInput2.setText('')
        pass
