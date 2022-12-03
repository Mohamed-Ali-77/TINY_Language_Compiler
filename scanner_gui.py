import os
from PyQt6.QtWidgets import *
from PyQt6 import uic
from scanner import Scanner


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("scannerui.ui", self)
        self.show()
        
        self.Filename = ""


        self.EnterButton.clicked.connect(self.Enter)
        self.scanButton.clicked.connect(self.Scan)
        self.parseButton.clicked.connect(self.Parse)


    def Enter(self):
        if self.lineEdit.text() != "" and os.path.exists(self.lineEdit.text()):
            self.Filename = ""
            self.Filename = str(self.lineEdit.text())
            self.scanButton.setEnabled(True)
        else:
            message = QMessageBox()
            message.setText("Please Enter Right File Path!")
            message.exec()


    def Scan(self):
        self.plainTextEdit.setEnabled(True)
        Scanned = Scanner(str(self.Filename))
        tokens = Scanned.generate_tokens_UI()

        if tokens != "":
            self.plainTextEdit.setPlainText(str(tokens))
            self.parseButton.setEnabled(True)
        else:
            message2 = QMessageBox()
            message2.setText("Scanner Failed!")
            message2.exec()

    
    def Parse(self):
        pass





def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()
