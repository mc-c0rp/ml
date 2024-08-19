from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget, QPushButton, QLabel
from PyQt5 import uic
import os
# res - resources (samaya vazhnaya directory in this project suka)
import exs # setup json examples
import mine # blogodarya ei proishodit magic (minecraft zapuskaet)
import save # save manager (sohranyaet and proveryaet vse json, moe izobretenye)

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
        self.play.clicked.connect(self.launch)
        self.add_ver()
        self.welcomeText.setText(f"Привет, {user['nickname']}.")
    
    def add_ver(self):
        versions = mine.get_ver()
        for ver in versions:
            self.versionBox.addItem(str(ver))

    def launch(self):
        mine.launch(user['nickname'], self.versionBox.currentText())

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