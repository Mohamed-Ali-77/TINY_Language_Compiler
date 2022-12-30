# import libraries
import os
import sys
import subprocess
import datetime
import matplotlib.pyplot as plt
import qtawesome as qta
import PyQt6
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QColor, QSyntaxHighlighter, QTextCharFormat, QAction, QPixmap
import qdarktheme
from PyQt6 import uic, QtGui, QtWidgets
from scanner import Scanner
from Parser_class import Parser
from SyntaxHighlighting import SyntaxHighlighter
import networkx as nx
import pygraphviz     
import matplotlib
from ui_GUI import Ui_MainWindow
matplotlib.use("TkAgg")


# Create Gui Class that inherit from QMainWindow class
class MyGUI(QMainWindow, Ui_MainWindow): 

    def __init__(self): # Constructor
        super(MyGUI, self).__init__() # Call super class constructor
        #uic.loadUi("GUI.ui", self) # Load ui file
        self.setupUi(self) # Setup ui file
        self.show() # Show window
        self.setWindowTitle("Tiny Compiler") # Set window title 
        self.setWindowIcon(QtGui.QIcon('Icon\icons8-compiler-32.png')) # Set window icon
        self.highlighter = SyntaxHighlighter(self.plainTextEdit.document())

        # Set lineEdit placeholder text
        self.lineEdit.setPlaceholderText("Path or File name")
        self.lineEdit.addAction(QtGui.QIcon('Icon\icons8-type-64.png'),QtWidgets.QLineEdit.ActionPosition.LeadingPosition) # Set lineEdit style sheet


        # Set browse button icon
        self.browseButton.setIcon(QtGui.QIcon('Icon\\search.ico'))

        # Set problem button icon
        self.problemsButton.setIcon(QtGui.QIcon('Icon\warning.ico'))
        self.problemsButton.setIconSize(PyQt6.QtCore.QSize(15, 15))

        # Set tokens button icon
        self.tokensButton.setIcon(QtGui.QIcon('Icon\\tokens.png'))
        self.tokensButton.setIconSize(PyQt6.QtCore.QSize(15, 15))

        # Create formatted strings
        self.fmt = QTextCharFormat()
        self.fmt.setBackground(QColor('red'))

        self.highlighter.clear_highlight()

        # Attripute to store file name/path
        self.Filename = "" 

        # Attribute to store scanner object
        self.Scanned = None

        # Attribute to store parser object
        self.Parsed = None

        # Attribute to store parser error tokens and indices
        self.success_flag = None
        self.parser_error_tokens = []
        self.parser_error_indcies = []


        # Attribute to store scanner error lines and tokens
        self.tokens = ""
        self.scanner_flag = None
        self.scanner_error_line = []

        # Attribute to store AST
        self.G = None

        self.label.setStyleSheet("QLabel { color : gold; }") # Set label style sheet
        self.label_2.setStyleSheet("QLabel { color : gold; }") # Set label style sheet
        self.label_3.setStyleSheet("QLabel { color : gold; }") # Set label style sheet
        #self.label_4.setStyleSheet("QLabel { color : gold; }")


        # BushButtons signals Actions
        self.EnterButton.clicked.connect(self.Enter) # Enter button signal
        self.scanButton.clicked.connect(self.Scan) # Scan button signal
        self.parseButton.clicked.connect(self.Parse) # Parse button signal
        self.drawButton.clicked.connect(self.Draw) # Draw button signal
        self.browseButton.clicked.connect(self.Browse) # Browse button signal
        self.generateButton.clicked.connect(self.Generate) # Generate button signal
        self.generateproblemsButton.clicked.connect(self.GenerateProblems) # Generate problems button signal
        self.tokensButton.clicked.connect(self.Tokens) # Tokens button signal
        self.problemsButton.clicked.connect(self.Problems) # Problems button signal
        self.codeButton.clicked.connect(self.Code) # Code button signal
        self.helpButton.clicked.connect(self.Help) # Help button signal
        self.helpButton.setFlat(True) # Help button flat
        
        
        # MenuBar signals Actions
        self.actionlightmode.triggered.connect(self.ToggleLightMode) # Light mode action signal
        self.actionClose.triggered.connect(self.close) # Close action signal
        self.actionAbout.triggered.connect(self.About) # About action signal
        self.actionShortcuts.triggered.connect(self.Shortcuts) # Shortcuts action signal
        self.actionHow_to_use.triggered.connect(self.How_to_use) # How to use action signal

        # Set label text to current date and time
        self.label_4.setStyleSheet("QLabel { color : gold; }") # Set label style sheet
        def update_datetime():
            datetime = QDateTime.currentDateTime()
            datetime.toLocalTime()
            self.label_4.setText("📅Date:  {}                        ⏳Time:  {}".format(datetime.toString("dd-MM-yyyy"), datetime.toString("hh:mm:ss")))

        timer = QTimer(self) # create timer
        timer.timeout.connect(update_datetime) # connect timer to update_datetime function
        timer.start(1000)  # update every 1000 milliseconds (1 second) 

        # set shortcuts
        self.actionClose.setShortcut('Ctrl+Q')
        self.actionlightmode.setShortcut('Ctrl+L')
        self.actionAbout.setShortcut('Ctrl+A')
        self.EnterButton.setShortcut('Return')
        self.scanButton.setShortcut('Ctrl+S')
        self.parseButton.setShortcut('Ctrl+P')
        self.drawButton.setShortcut('Ctrl+D')
        self.browseButton.setShortcut('Ctrl+B')
        self.generateButton.setShortcut('Ctrl+G')
        self.tokensButton.setShortcut('Ctrl+T')
        self.problemsButton.setShortcut('Ctrl+E')
        self.codeButton.setShortcut('Ctrl+C')
        self.helpButton.setShortcut('Ctrl+H')
        self.actionHow_to_use.setShortcut('Ctrl+U')

    def Time_and_Date(self):
        self.label_4.setText(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    # Methods to handle signals
    def How_to_use(self):
        QMessageBox.about(self, "How to use","1- Enter the code By Browse button or enter the path in linedit.\n2- Click on Scan button to scan the code.\n3- Click on Parse button to parse the code.\n4- Click on Draw button to draw the AST.\n5- Click on Generate button to generate tokens file.\n6- Click on Tokens button to view the tokens.\n7- Click on Problems button to view the problems.\n8- Click on Code button to view the code.\n9- Click on Close button in the menu bar to close the application.\n10- Click on About button to view the application information.\n12- Click on Shortcuts button to view the application shortcuts.\n13- Click on Light mode button to toggle between light and dark mode.")
        

    def Help(self):
        QMessageBox.about(self, "Help","The Tiny Compiler app is a powerful tool for compiling code written in the Tiny language. It offers a range of features, including syntax highlighting, error checking, and code completion, to help you write and debug your code more efficiently.\
To use the app, simply open a new file and start writing your code. When you're ready to compile, click the \"Browse\" button to enter your code.")

    def Shortcuts(self):
        QMessageBox.about(self, "Shortcuts", "Ctrl+Z: Shortcuts\nCtrl+Q: Close\nCtrl+L: Light Mode\nCtrl+A: About\nReturn: Enter\nCtrl+S: Scan\nCtrl+P: Parse\nCtrl+D: Draw\nCtrl+B: Browse\nCtrl+G: Generate\nCtrl+T: Tokens\nCtrl+E: Problems\nCtrl+C: Code")


    def About(self):
        QMessageBox.about(self, "About", "Tiny language Compiler\nVersion: 1.0\nDeveloped by: Mohamed Ali\n\
                        Mohamed Emad\n\
                        Mohamed Elsayed\n\
                        Moamen Waleed\n\
                        Mohamed Assran\n\
\nOS: Windows 10\n\
Python Version: 3.11.0\nPyQt6 Version: 6.1.2\nMatplotlib Version: 3.4.2\nNetworkx Version: 2.6.3\nQDarkTheme Version: 2.8.1")

    # Method to Show Code in plainTextEdit
    def Code(self):
        self.highlighter.clear_highlight() # Clear highlight
        self.plainTextEdit.setEnabled(True) # Enable plainTextEdit
        self.label_2.setText("Code")
        self.plainTextEdit.clear()
        text_file = open(self.Filename, "r")
        tiny_code = text_file.read() # Read file
        tiny_code = tiny_code.encode('cp1252').decode('utf-8')  # Convert to utf-8
        self.plainTextEdit.setPlainText(tiny_code) # Set plainTextEdit text
        
        
    # Method to show tokens in plainTextEdit
    def Tokens(self):
        self.highlighter.clear_highlight() # Clear highlight
        self.plainTextEdit.setEnabled(True) # Enable plainTextEdit
        self.label_2.setText("Tokens")
        self.plainTextEdit.clear()
        self.plainTextEdit.setPlainText(self.tokens)
        self.fmt.setBackground(QColor('red'))
        if not self.success_flag:
            for i in self.parser_error_indcies:
                self.highlighter.highlight_line(i, self.fmt)

        if not self.scanner_flag:
            for ele in self.scanner_error_line:
                self.highlighter.highlight_line(ele[1], self.fmt)

    #Method TO show problems in plainTextEdit
    def Problems(self):
        self.generateproblemsButton.setEnabled(True)
        self.highlighter.clear_highlight() # Clear highlight
        self.label_2.setText("Problems")
        self.plainTextEdit.setEnabled(True) # Enable plainTextEdit
        self.plainTextEdit.clear()
        self.fmt.setBackground(QColor('rosybrown'))
        self.highlighter.highlight_line(0, self.fmt)
        self.plainTextEdit.appendPlainText("Error Type   "+ "    Token "+ "   "+" Number")
        if not self.success_flag:
            for i in range(len(self.parser_error_tokens)):
                self.plainTextEdit.appendPlainText("Syntax  Error:   "+ self.parser_error_tokens[i] + "     "+str(self.parser_error_indcies[i]))
        if not self.scanner_flag:
            for ele in self.scanner_error_line:
                self.plainTextEdit.appendPlainText("Token Error:   "+ ele[0] + "   "+str(ele[1]))

    # reset method to reset all buttons and textEdit
    def reset(self):
        self.EnterButton.setEnabled(False) # Disable EnterButton
        self.scanButton.setEnabled(False) # Disable scanButton
        self.parseButton.setEnabled(False) # Disable parseButton
        self.drawButton.setEnabled(False) # Disable drawButton
        self.generateButton.setEnabled(False) # Disable generateButton
        self.tokensButton.setEnabled(False) # Disable tokensButton
        self.problemsButton.setEnabled(False) # Disable problemsButton
        self.codeButton.setEnabled(False) # Disable codeButton
        self.highlighter.clear_highlight() # Clear highlight
        self.plainTextEdit.clear() # Clear plainTextEdit
        self.lineEdit.clear() # Clear lineEdit
        self.plainTextEdit.setEnabled(False) # Disable plainTextEdit
        self.label_2.setText("") # Set label_2 text
        self.parser_error_tokens = [] # Clear parser_error_tokens
        self.parser_error_indcies = [] #clear parser_error_indicies
        self.scanner_error_line = [] # Clear scanner_error_line
        self.tokens = "" # Clear tokens
        if self.G != None:
            self.G.clear() # Clear graph
        



    # Method to close window
    def close(self) -> bool:
        return super().close()


    #Method to switch between light modes
    def ToggleLightMode(self):
        if self.actionlightmode.isChecked():
            self.setStyleSheet(qdarktheme.load_stylesheet('light',custom_colors={"primary": "#004578"}))
            self.label.setStyleSheet("QLabel { color : #004578; }")
            self.label_2.setStyleSheet("QLabel { color : #004578; }")
            self.actionlightmode.setText("Dark Mode")
            self.actionlightmode.setIcon(QtGui.QIcon('Icon\icons8-night-mode-67.png'))
            self.label_3.setStyleSheet("QLabel { color : #004578; }")

        else:
            self.setStyleSheet(qdarktheme.load_stylesheet('dark',custom_colors={"primary": "#fb1"}))
            self.label.setStyleSheet("QLabel { color : gold; }")
            self.label_2.setStyleSheet("QLabel { color : gold; }")
            self.label_3.setStyleSheet("QLabel { color : gold; }")
            self.actionlightmode.setText("Light Mode")
            self.actionlightmode.setIcon(QtGui.QIcon('Icon\icons8-light-mode-78.png'))



    # Method to browse method to get file path and write it into lineEdit
    def Browse(self):
        self.reset()
        fileName,_ = QFileDialog.getOpenFileName(self, 'OpenFile' ,"~","Text Files (*.txt)")    # Get file path
        fileName = str(fileName.rstrip(os.sep)) # Remove \ from file path
        self.lineEdit.setText(fileName) # Write file path into lineEdit
        self.EnterButton.setEnabled(True) # Enable EnterButton
        
    # Method to check for file exist or not and store file name into filename attribute
    def Enter(self): # Enter method to get file name and path
        if (self.lineEdit.text() != "" and os.path.exists(self.lineEdit.text())): # Check if file exist
            _ ,file_extension = os.path.splitext(self.lineEdit.text()) # Get file extension
            if file_extension == ".txt": # Check if file extension is .txt
                self.Filename = str(self.lineEdit.text()) # Store file name into filename attribute
                self.scanButton.setEnabled(True) # Enable scanButton
                self.plainTextEdit.clear()
                self.codeButton.setEnabled(True) # Enable codeButton
            # POP error message if wrong filename wrtitten by hand in lineedit 
            else:
                message3 = QMessageBox()
                message3.setIcon(QMessageBox.Icon.Information)
                message3.setWindowTitle("Information")
                message3.setText("Please Enter Right File Extension")
                message3.exec()
        # POP error message if filename not specified
        else:
            message = QMessageBox()
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("Information")
            message.setText("Please Enter Right File Path")
            message.exec()


    # Method to take file name and path it into scanner class to create tokens and show it
    def Scan(self): 
        #self.plainTextEdit.setEnabled(True) # Enable plainTextEdit
        self.Scanned = Scanner(str(self.Filename)) # Create Scanner object
        self.scanner_flag, self.tokens, self.scanner_error_line = self.Scanned.generate_tokens_UI() # Get tokens from Scanner
        if self.scanner_flag: # Check if Scanner succeeded
            self.tokensButton.setEnabled(True) # Write tokens into plainTextEdit
            #self.plainTextEdit.setPlainText(str(self.tokens)) # Write tokens into plainTextEdit
            self.parseButton.setEnabled(True) # Enable parseButton
            self.generateButton.setEnabled(True) # Enable generateButton
        # POP error message if Scanner failed
        else:
            self.tokensButton.setEnabled(True) # Write tokens into plainTextEdit
            self.problemsButton.setEnabled(True) # Enable problemsButton
            # Highlight error line   
            #try:
                #self.highlighter.highlight_line(self.scanner_error_line, self.fmt)
            #except ValueError:
                #pass

            # POP error message if Scanner failed
            message2 = QMessageBox() 
            message2.setIcon(QMessageBox.Icon.Critical) 
            message2.setWindowTitle("Error")
            message2.setText("Scanner Failed.\nPlease Check Proplems output for more information.")
            message2.exec()

    def GenerateProblems(self):
        problems = self.plainTextEdit.toPlainText()
        f = open("output_problems/problems_"+ str(os.path.basename(self.Filename)), "w+") # open file to write
        f.write(problems) # write output to file
        f.close()   # close file


    # Method to create tokens file
    def Generate(self): 
        self.Scanned.generate_tokens() # Generate tokens file -> tokens.txt


    # Method to take tokens and parse it into parser class to create AST and show it
    def pygraphviz_layout_with_rank(self, G, prog="dot", root=None, sameRank=[], args=""): # Layout for AST
        if root is not None:  # add root to args for pygraphviz
            args += "-Groot=%s" % root # add root to args for pygraphviz
        A = nx.nx_agraph.to_agraph(G) # create a new graph with pygraphviz
        for sameNodeHeight in sameRank: # add same rank nodes
            if type(sameNodeHeight) == str: # if sameNodeHeight is a string
                print("node \"%s\" has no peers in its rank group" % 
                      sameNodeHeight) # print error message
            A.add_subgraph(sameNodeHeight, rank="same") # add same rank nodes
        A.layout(prog=prog, args=args) # layout with pygraphviz
        node_pos = {} # empty dictionary to store positions
        for n in G: # write pos into node_pos
            node = pygraphviz.Node(A, n) # get node from pygraphviz
            try: # try to get position
                xx, yy = node.attr["pos"].split(',') # split position
                node_pos[n] = (float(xx), float(yy)) # write position
            except: # if no position found for node n 
                print("no position for node", n)    # print error message 
                node_pos[n] = (0.0, 0.0) # write position
        return node_pos # return node_pos

    
    def draw_AST(self, same_rank_nodes):    # Draw AST
        graph = self.G  # nx.DiGraph()
        pos = self.pygraphviz_layout_with_rank(graph, prog='dot', sameRank=same_rank_nodes)  

        labels = dict((n, d['value']) for n, d in graph.nodes(data=True)) # labels for nodes
        f = plt.figure(1, figsize=(13, 10)) # figure size
        for shape in ['s','o']: # draw nodes
            nodelist = [sNode[0] for sNode in filter(lambda x: x[1]["shape"] == shape, graph.nodes(data=True))]
            nx.draw_networkx_nodes(graph, pos, node_color='#565656', node_size=1800, node_shape=shape, label=labels, nodelist=nodelist) # draw nodes
        nx.draw_networkx_edges(graph, pos, arrows=False) # draw edges
        nx.draw_networkx_labels(graph, pos, labels=labels, font_size=8, font_color='#FFFFFF', font_weight='500', alpha =1, font_family = "Georgia") # draw labels
        f.canvas.manager.window.wm_geometry("+%d+%d" % (150, 0)) # set window position
        plt.gca().set_facecolor('#f5deb3') # set background color
        plt.show() # show graph

    def Parse(self):    # Take file name and path it into parser class to create AST and show it
        self.Parsed = Parser() # create object from parser class
        self.Parsed.set_tokens_types_and_tokens_values(self.Scanned.tokens_types, self.Scanned.tokens_values) # pass tokens to parser

        self.success_flag, self.parser_error_tokens, self.parser_error_indcies = self.Parsed.run() # call run method to create AST
        if self.success_flag: # if parser succeeded
            self.drawButton.setEnabled(True) # enable drawButton
        else:
            try:
                for i in self.parser_error_indcies:
                    self.highlighter.highlight_line(i, self.fmt)
            except ValueError:
                pass
            
            self.problemsButton.setEnabled(True) # enable problemsButton

            #print("Parser Failed.\nSyntax Error at token: " + token + " at index: " + str(index)) # print error message
            message4 = QMessageBox()
            message4.setIcon(QMessageBox.Icon.Critical)
            message4.setWindowTitle("Error")
            message4.setText("Parser Failed.\nCheck Proplems output for more information.")
            message4.exec()


    def Draw(self): # Method to draw AST
        nodes_list = self.Parsed.nodes_table # get nodes table from parser
        edges_list = self.Parsed.edges_table # get edges table from parser
        self.G = nx.DiGraph() # create graph
        for node_number, node in nodes_list.items(): # add nodes to graph
            self.G.add_node(node_number, value=node[0] + '\n' + node[1], shape=node[2]) # add nodes to graph
        self.G.add_edges_from(edges_list) # add edges to graph
        self.Parsed.clear_tables() # clear tables
        self.draw_AST(self.Parsed.same_rank_nodes) # draw graph
        self.G.clear() # clear graph




# Main function to call it into __main__
def main():
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet(custom_colors={"primary": "#ffe134"})) 
    window = MyGUI()
    app.exec()


if __name__ == "__main__":
    os.system("pip freeze > requirements.txt")
    os.system("pip install -r requirements.txt")
    main()
    #os.remove("requirements.txt")