# import libraries
import os
import sys
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QColor, QSyntaxHighlighter, QTextCharFormat
import qdarktheme
from PyQt6 import uic, QtGui
from Scanner import Scanner
from Parser_class import Parser
from SyntaxHighlighting import SyntaxHighlighter
import networkx as nx
import matplotlib
matplotlib.use("TkAgg")


# Create Gui Class that inherit from QMainWindow class
class MyGUI(QMainWindow): 

    def __init__(self): # Constructor
        super(MyGUI, self).__init__() # Call super class constructor
        uic.loadUi("scannerui.ui", self) # Load ui file
        self.show() # Show window
        self.setWindowTitle("TinyCompiler") # Set window title 
        self.setWindowIcon(QtGui.QIcon('Icon\icon.png')) # Set window icon

        self.highlighter = SyntaxHighlighter(self.plainTextEdit.document())

        # Attripute to store file name/path
        self.Filename = "" 

        # Attribute to store scanner object
        self.Scanned = None 

        # Attribute to store parser object
        self.Parsed = None

        # Attribute to store AST
        self.G = None

        # BushButtons signals Actions
        self.EnterButton.clicked.connect(self.Enter) # Enter button signal
        self.scanButton.clicked.connect(self.Scan) # Scan button signal
        self.parseButton.clicked.connect(self.Parse) # Parse button signal
        self.drawButton.clicked.connect(self.Draw) # Draw button signal
        self.browseButton.clicked.connect(self.Browse) # Browse button signal
        self.generateButton.clicked.connect(self.Generate) # Generate button signal
        
        # menuBar signals Actions
        self.actionlightmode.triggered.connect(self.ToggleLightMode) # Light mode action signal
        self.actionClose.triggered.connect(self.close) # Close action signal

    # reset method to reset all buttons and textEdit
    def reset(self):
        self.EnterButton.setEnabled(False) # Disable EnterButton
        self.scanButton.setEnabled(False) # Disable scanButton
        self.parseButton.setEnabled(False) # Disable parseButton
        self.drawButton.setEnabled(False) # Disable drawButton
        self.generateButton.setEnabled(False) # Disable generateButton
        self.highlighter.clear_highlight() # Clear highlight
        self.plainTextEdit.clear() # Clear plainTextEdit
        self.lineEdit.clear() # Clear lineEdit
        self.plainTextEdit.setEnabled(False) # Disable plainTextEdit

    # Method to close window
    def close(self) -> bool:
        return super().close()


    #Method to switch between light modes
    def ToggleLightMode(self):
        if self.actionlightmode.isChecked():
            self.setStyleSheet(qdarktheme.load_stylesheet('light'))
        else:
            self.setStyleSheet(qdarktheme.load_stylesheet('dark'))

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
        self.plainTextEdit.setEnabled(True) # Enable plainTextEdit
        self.Scanned = Scanner(str(self.Filename)) # Create Scanner object
        tokens = self.Scanned.generate_tokens_UI() # Get tokens from Scanner

        if tokens != "": # Check if Scanner succeeded
            self.plainTextEdit.setPlainText(str(tokens)) # Write tokens into plainTextEdit
            self.parseButton.setEnabled(True) # Enable parseButton
            self.generateButton.setEnabled(True) # Enable generateButton
        # POP error message if Scanner failed
        else: 
            message2 = QMessageBox() 
            message2.setIcon(QMessageBox.Icon.Critical) 
            message2.setWindowTitle("Error")
            message2.setText("Scanner Failed.\nPlease check code.")
            message2.exec()

    # Method to create tokens file
    def Generate(self): 
        self.Scanned.generate_tokens() # Generate tokens file -> tokens.txt


    
    def pygraphviz_layout_with_rank(self, G, prog="dot", root=None, sameRank=[], args=""): # Layout for AST
        try: # pygraphviz_layout was removed in networkx 2.0
            import pygraphviz 
        except ImportError: 
            raise ImportError('requires pygraphviz ',
                              'http://networkx.lanl.gov/pygraphviz ',
                              '(not available for Python3)')    
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
        f = plt.figure(1, figsize=(13, 8.65)) # figure size
        for shape in ['s', 'o']: # draw nodes
            nx.draw_networkx_nodes(graph, pos, node_color='y', node_size=1300, node_shape=shape, label=labels, nodelist=[
                sNode[0] for sNode in filter(lambda x: x[1]["shape"] == shape, graph.nodes(data=True))]) # draw nodes
        nx.draw_networkx_edges(graph, pos, arrows=False) # draw edges
        nx.draw_networkx_labels(graph, pos, labels=labels, font_size=8) # draw labels
        f.canvas.manager.window.wm_geometry("+%d+%d" % (600, 0)) # set window position
        plt.show() # show graph

    def Parse(self):    # Take file name and path it into parser class to create AST and show it
        self.Parsed = Parser() # create object from parser class
        self.Parsed.set_tokens_types_and_tokens_values(self.Scanned.tokens_types, self.Scanned.tokens_values) # pass tokens to parser

        succes, index = self.Parsed.run() # call run method to create AST
        if succes: # if parser succeeded
            self.drawButton.setEnabled(True) # enable drawButton
        else:
            # Create formatted strings
            fmt = QTextCharFormat()
            fmt.setBackground(QColor('red'))

            self.highlighter.clear_highlight()

            try:
                self.highlighter.highlight_line(index, fmt)
            except ValueError:
                pass

            #print("Parser Failed.\nSyntax Error at token: " + token + " at index: " + str(index)) # print error message
            message4 = QMessageBox()
            message4.setIcon(QMessageBox.Icon.Critical)
            message4.setWindowTitle("Error")
            message4.setText("Parser Failed.\nSyntax Error at Token number: " + str(index+1))
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




# Main function to call it into __main__
def main():
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet())    
    window = MyGUI()
    app.exec()


if __name__ == "__main__":
    main()