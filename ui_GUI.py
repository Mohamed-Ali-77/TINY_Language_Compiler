# Form implementation generated from reading ui file 'g:\Faculty-Files\Senior -2- 1st term\Design of Compilers\TINY Language Compiler\TINY_Language_Compiler\GUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 625)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("g:\\Faculty-Files\\Senior -2- 1st term\\Design of Compilers\\TINY Language Compiler\\TINY_Language_Compiler\\Icon/icons8-compiler-32.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 2, 0, 1, 2)
        self.helpButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("g:\\Faculty-Files\\Senior -2- 1st term\\Design of Compilers\\TINY Language Compiler\\TINY_Language_Compiler\\Icon/question.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.helpButton.setIcon(icon1)
        self.helpButton.setAutoDefault(False)
        self.helpButton.setDefault(False)
        self.helpButton.setFlat(True)
        self.helpButton.setObjectName("helpButton")
        self.gridLayout.addWidget(self.helpButton, 0, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(10)
        font.setBold(False)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("border-right-color: rgb(244, 255, 44);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("g:\\Faculty-Files\\Senior -2- 1st term\\Design of Compilers\\TINY Language Compiler\\TINY_Language_Compiler\\Icon/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.browseButton.setIcon(icon2)
        self.browseButton.setIconSize(QtCore.QSize(18, 18))
        self.browseButton.setAutoDefault(False)
        self.browseButton.setDefault(False)
        self.browseButton.setFlat(False)
        self.browseButton.setObjectName("browseButton")
        self.verticalLayout.addWidget(self.browseButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EnterButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnterButton.setEnabled(False)
        self.EnterButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("g:\\Faculty-Files\\Senior -2- 1st term\\Design of Compilers\\TINY Language Compiler\\TINY_Language_Compiler\\Icon/enter.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.EnterButton.setIcon(icon3)
        self.EnterButton.setObjectName("EnterButton")
        self.horizontalLayout.addWidget(self.EnterButton)
        self.scanButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanButton.setEnabled(False)
        self.scanButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("g:\\Faculty-Files\\Senior -2- 1st term\\Design of Compilers\\TINY Language Compiler\\TINY_Language_Compiler\\Icon/qr-code-scan.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.scanButton.setIcon(icon4)
        self.scanButton.setObjectName("scanButton")
        self.horizontalLayout.addWidget(self.scanButton)
        self.parseButton = QtWidgets.QPushButton(self.centralwidget)
        self.parseButton.setEnabled(False)
        self.parseButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("g:\\Faculty-Files\\Senior -2- 1st term\\Design of Compilers\\TINY Language Compiler\\TINY_Language_Compiler\\Icon/parsing.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.parseButton.setIcon(icon5)
        self.parseButton.setObjectName("parseButton")
        self.horizontalLayout.addWidget(self.parseButton)
        self.drawButton = QtWidgets.QPushButton(self.centralwidget)
        self.drawButton.setEnabled(False)
        self.drawButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("g:\\Faculty-Files\\Senior -2- 1st term\\Design of Compilers\\TINY Language Compiler\\TINY_Language_Compiler\\Icon/path.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.drawButton.setIcon(icon6)
        self.drawButton.setObjectName("drawButton")
        self.horizontalLayout.addWidget(self.drawButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.codeButton = QtWidgets.QPushButton(self.centralwidget)
        self.codeButton.setEnabled(False)
        self.codeButton.setMinimumSize(QtCore.QSize(189, 29))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("g:\\Faculty-Files\\Senior -2- 1st term\\Design of Compilers\\TINY Language Compiler\\TINY_Language_Compiler\\Icon/icons8-code-file-48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.codeButton.setIcon(icon7)
        self.codeButton.setObjectName("codeButton")
        self.horizontalLayout_3.addWidget(self.codeButton)
        self.tokensButton = QtWidgets.QPushButton(self.centralwidget)
        self.tokensButton.setEnabled(False)
        self.tokensButton.setMinimumSize(QtCore.QSize(189, 29))
        self.tokensButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon = QtGui.QIcon.fromTheme("accessories-character-map")
        self.tokensButton.setIcon(icon)
        self.tokensButton.setObjectName("tokensButton")
        self.horizontalLayout_3.addWidget(self.tokensButton)
        self.problemsButton = QtWidgets.QPushButton(self.centralwidget)
        self.problemsButton.setEnabled(False)
        self.problemsButton.setMinimumSize(QtCore.QSize(189, 29))
        self.problemsButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("g:\\Faculty-Files\\Senior -2- 1st term\\Design of Compilers\\TINY Language Compiler\\TINY_Language_Compiler\\Icon/warning.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.problemsButton.setIcon(icon8)
        self.problemsButton.setObjectName("problemsButton")
        self.horizontalLayout_3.addWidget(self.problemsButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 2, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setEnabled(False)
        self.generateButton.setObjectName("generateButton")
        self.horizontalLayout_7.addWidget(self.generateButton)
        self.generateproblemsButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateproblemsButton.setEnabled(False)
        self.generateproblemsButton.setObjectName("generateproblemsButton")
        self.horizontalLayout_7.addWidget(self.generateproblemsButton)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 923, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.menuMode.setFont(font)
        self.menuMode.setObjectName("menuMode")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setStrikeOut(False)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionlightmode = QtGui.QAction(MainWindow)
        self.actionlightmode.setCheckable(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("g:\\Faculty-Files\\Senior -2- 1st term\\Design of Compilers\\TINY Language Compiler\\TINY_Language_Compiler\\Icon/icons8-light-mode-78.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionlightmode.setIcon(icon9)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.actionlightmode.setFont(font)
        self.actionlightmode.setObjectName("actionlightmode")
        self.actionClose = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("g:\\Faculty-Files\\Senior -2- 1st term\\Design of Compilers\\TINY Language Compiler\\TINY_Language_Compiler\\Icon/close.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClose.setIcon(icon10)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.actionClose.setFont(font)
        self.actionClose.setObjectName("actionClose")
        self.actionAbout = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("g:\\Faculty-Files\\Senior -2- 1st term\\Design of Compilers\\TINY Language Compiler\\TINY_Language_Compiler\\Icon/icons8-info-48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAbout.setIcon(icon11)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.actionAbout.setFont(font)
        self.actionAbout.setObjectName("actionAbout")
        self.actionShortcuts = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("g:\\Faculty-Files\\Senior -2- 1st term\\Design of Compilers\\TINY Language Compiler\\TINY_Language_Compiler\\Icon/shortsut.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionShortcuts.setIcon(icon12)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.actionShortcuts.setFont(font)
        self.actionShortcuts.setObjectName("actionShortcuts")
        self.actionHow_to_use = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("g:\\Faculty-Files\\Senior -2- 1st term\\Design of Compilers\\TINY Language Compiler\\TINY_Language_Compiler\\Icon/icons8-how-quest-50.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionHow_to_use.setIcon(icon13)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.actionHow_to_use.setFont(font)
        self.actionHow_to_use.setObjectName("actionHow_to_use")
        self.menuMode.addAction(self.actionlightmode)
        self.menuFile.addAction(self.actionClose)
        self.menuhelp.addAction(self.actionAbout)
        self.menuhelp.addSeparator()
        self.menuhelp.addAction(self.actionShortcuts)
        self.menuhelp.addSeparator()
        self.menuhelp.addAction(self.actionHow_to_use)
        self.menuhelp.addSeparator()
        self.menuhelp.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.helpButton.setToolTip(_translate("MainWindow", "help"))
        self.label_3.setText(_translate("MainWindow", "© All Copy rights reserved to the team                                "))
        self.label.setText(_translate("MainWindow", "File Path : "))
        self.browseButton.setToolTip(_translate("MainWindow", "Browsing file"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.lineEdit.setToolTip(_translate("MainWindow", "Enter file Path"))
        self.EnterButton.setToolTip(_translate("MainWindow", "Enter the file "))
        self.EnterButton.setText(_translate("MainWindow", "Enter"))
        self.scanButton.setToolTip(_translate("MainWindow", "Scan code"))
        self.scanButton.setText(_translate("MainWindow", "Scan"))
        self.parseButton.setToolTip(_translate("MainWindow", "Parse Code"))
        self.parseButton.setText(_translate("MainWindow", "Parse"))
        self.drawButton.setToolTip(_translate("MainWindow", "Draw AST"))
        self.drawButton.setText(_translate("MainWindow", "Draw"))
        self.codeButton.setToolTip(_translate("MainWindow", "Code"))
        self.codeButton.setText(_translate("MainWindow", "Code"))
        self.tokensButton.setToolTip(_translate("MainWindow", "Tokens"))
        self.tokensButton.setText(_translate("MainWindow", "Tokens"))
        self.problemsButton.setToolTip(_translate("MainWindow", "Problems"))
        self.problemsButton.setText(_translate("MainWindow", "Problems"))
        self.generateButton.setToolTip(_translate("MainWindow", "Generate tokens file"))
        self.generateButton.setText(_translate("MainWindow", "Generate Tokens File"))
        self.generateproblemsButton.setText(_translate("MainWindow", "Generate Problems File"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuhelp.setTitle(_translate("MainWindow", "About"))
        self.actionlightmode.setText(_translate("MainWindow", " Light Mode"))
        self.actionlightmode.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionShortcuts.setText(_translate("MainWindow", "Shortcuts"))
        self.actionShortcuts.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use"))
