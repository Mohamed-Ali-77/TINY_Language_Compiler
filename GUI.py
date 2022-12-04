import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QFile, QTextStream, QDir
import qdarktheme
from PyQt6 import uic, QtGui
from scanner import Scanner



class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("scannerui.ui", self)
        self.show()
        self.setWindowTitle("Scanner")
        self.setWindowIcon(QtGui.QIcon('barcode-scanner.png'))

        self.Filename = ""


        self.EnterButton.clicked.connect(self.Enter)
        self.scanButton.clicked.connect(self.Scan)
        self.parseButton.clicked.connect(self.Parse)
        self.browseButton.clicked.connect(self.Browse)


    def Browse(self):
        fileName,_ = QFileDialog.getOpenFileName(self, 'OpenFile' ,"~","Text Files (*.txt)")
        fileName = str(fileName.rstrip(os.sep))
        self.lineEdit.setText(fileName)
        

    def Enter(self):
        if (self.lineEdit.text() != "" and os.path.exists(self.lineEdit.text())):
            _ ,file_extension = os.path.splitext(self.lineEdit.text())
            if file_extension == ".txt":
                self.Filename = str(self.lineEdit.text())
                self.scanButton.setEnabled(True)
            else:
                message3 = QMessageBox()
                message3.setWindowTitle("Error")
                message3.setText("Please Enter Right File Extension!")
                message3.exec()
        else:
            message = QMessageBox()
            message.setWindowTitle("Error")
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
            message2.setWindowTitle("Error")
            message2.setText("Scanner Failed!")
            message2.exec()

    
    def Parse(self):
        pass





def main():
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet())    
    window = MyGUI()
    app.exec()



if __name__ == "__main__":
    main()