from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget, QPushButton, QLabel, QPlainTextEdit
from PyQt5 import uic
from PyQt5.QtCore import Qt
import os
# res - resources (samaya vazhnaya directory in this project suka)
import exs # setup json examples
import mine # blogodarya ei proishodit magic (minecraft zapuskaet)
import save # save manager (sohranyaet and proveryaet vse json, moe izobretenye)

import threading

settings = {}
user = {}

def load():
    global settings
    global user
    settings = save.loadj('settings')
    user = save.loadj('user')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file = os.path.join(os.path.dirname(__file__), 'design', 'main.ui')
        uic.loadUi(ui_file, self)
        
        # init ui
        self.init_ui()
    
    def init_ui(self):
        global user
        self.hide()
        self.play.clicked.connect(self.start)
        self.play.setText('Запустить')
        self.add_ver()
        self.welcomeText.setText(f"Привет, {user['nickname']}.")
        self.news.setPlainText(mine.get_news())
        self.bar.setVisible(False)
        self.accountButton.clicked.connect(self.showAccountWindow)
        self.update()
        self.show()
        print('mainwindow: ui initialized')
    
    def showAccountWindow(self):
        self.accountWindow = AccountWindow()
        self.accountWindow.show()

    def add_ver(self):
        versions = mine.get_ver()
        for ver in versions:
            self.versionBox.addItem(str(ver))

    # start vtorogo potoka nahui, t.k. zavisaet mainWindow
    def start(self):
        thr = threading.Thread(target=self.launch)
        self.play.setText('Запускаю...')
        QApplication.processEvents()
        thr.start()

    def launch(self):
        try:
            mine.launch(user['nickname'], self.versionBox.currentText(), self.bar)
        except Exception as ex:
            self.play.setText('Ошибка!')
            print('mainwindow: launching minecraft has crashed, ex: ' + ex)

class AccountWindow(QWidget):
    def __init__(self):
        super().__init__()
        ui_file = os.path.join(os.path.dirname(__file__), 'design', 'account.ui')
        uic.loadUi(ui_file, self)

        # init ui
        self.accountEditBtn.clicked.connect(self.save_account)
        self.accountEditClear.clicked.connect(self.clear)
        print('accountwindow: ui initialized')
    
    def save_account(self):
        global user

        n = self.accountEdit.toPlainText()
        if n != None or n != ' ':
            user['nickname'] = n.replace(' ', '')
            save.savef('user', user)
            self.hide()

    def clear(self):
        self.accountEdit.SetPlainText('')

if __name__ == "__main__":
    # preperating (podgotovka nahui)
    result = save.check() # proverka directory
    if result == 'ok':
        load()
        import sys
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    else:
        print(result)
        exit()