import os
import sys
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QFile, QTextStream, QDir
import qdarktheme
from PyQt6 import uic, QtGui
from scanner import Scanner
from parser_class import Parser
import networkx as nx
import matplotlib
matplotlib.use("TkAgg")


# Create Gui Class that inherit from QMainWindow class
class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("scannerui.ui", self)
        self.show()
        self.setWindowTitle("Scanner")
        self.setWindowIcon(QtGui.QIcon('Icon\icon.png'))

        # Attripute to store file name/path
        self.Filename = ""

        # BushButtons signals Actions
        self.EnterButton.clicked.connect(self.Enter)
        self.scanButton.clicked.connect(self.Scan)
        self.parseButton.clicked.connect(self.Parse)
        self.browseButton.clicked.connect(self.Browse)


    # Browse method to get file path and write it into lineEdit
    def Browse(self):
        fileName,_ = QFileDialog.getOpenFileName(self, 'OpenFile' ,"~","Text Files (*.txt)")
        fileName = str(fileName.rstrip(os.sep))
        self.lineEdit.setText(fileName)
        
    # Check for file exist or not and store file name into filename attribute
    def Enter(self):
        if (self.lineEdit.text() != "" and os.path.exists(self.lineEdit.text())):
            _ ,file_extension = os.path.splitext(self.lineEdit.text())
            if file_extension == ".txt":
                self.Filename = str(self.lineEdit.text())
                self.scanButton.setEnabled(True)
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
    # Take file name and path it into scanner class to create tokens and show it
    def Scan(self):
        self.plainTextEdit.setEnabled(True)
        Scanned = Scanner(str(self.Filename))
        tokens = Scanned.generate_tokens_UI()

        if tokens != "":
            self.plainTextEdit.setPlainText(str(tokens))
            self.parseButton.setEnabled(True)
        # POP error message if Scanner failed
        else:
            message2 = QMessageBox()
            message2.setIcon(QMessageBox.Icon.Critical)
            message2.setWindowTitle("Error")
            message2.setText("Scanner Failed.\nPlease check code.")
            message2.exec()

    
    def pygraphviz_layout_with_rank(self, G, prog="dot", root=None, sameRank=[], args=""):
        try:
            import pygraphviz
        except ImportError:
            raise ImportError('requires pygraphviz ',
                              'http://networkx.lanl.gov/pygraphviz ',
                              '(not available for Python3)')
        if root is not None:
            args += "-Groot=%s" % root
        A = nx.nx_agraph.to_agraph(G)
        for sameNodeHeight in sameRank:
            if type(sameNodeHeight) == str:
                print("node \"%s\" has no peers in its rank group" %
                      sameNodeHeight)
            A.add_subgraph(sameNodeHeight, rank="same")
        A.layout(prog=prog, args=args)
        node_pos = {}
        for n in G:
            node = pygraphviz.Node(A, n)
            try:
                xx, yy = node.attr["pos"].split(',')
                node_pos[n] = (float(xx), float(yy))
            except:
                print("no position for node", n)
                node_pos[n] = (0.0, 0.0)
        return node_pos

    def draw(self, same_rank_nodes):
        graph = self.G
        # pos = nx.get_node_attributes(graph, 'pos')
        pos = self.pygraphviz_layout_with_rank(
            graph, prog='dot', sameRank=same_rank_nodes)
        # pos = nx.nx_pydot.graphviz_layout(graph, prog='dot')
        labels = dict((n, d['value']) for n, d in graph.nodes(data=True))
        f = plt.figure(1, figsize=(13, 8.65))
        for shape in ['s', 'o']:
            nx.draw_networkx_nodes(graph, pos, node_color='y', node_size=1300, node_shape=shape, label=labels, nodelist=[
                sNode[0] for sNode in filter(lambda x: x[1]["shape"] == shape, graph.nodes(data=True))])
        nx.draw_networkx_edges(graph, pos, arrows=False)
        nx.draw_networkx_labels(graph, pos, labels=labels, font_size=8)
        f.canvas.manager.window.wm_geometry("+%d+%d" % (600, 0))
        plt.show()

    def Parse(self):
        scanned_code = Scanner(self.Filename)
        scanned_code.Scan()
        parse_code = Parser()
        parse_code.set_tokens_list_and_code_list(scanned_code.tokens_types, scanned_code.tokens_values)
        parse_code.run()
        nodes_list = parse_code.nodes_table
        edges_list = parse_code.edges_table
        self.G = nx.DiGraph()
        for node_number, node in nodes_list.items():
            self.G.add_node(
                node_number, value=node[0] + '\n' + node[1], shape=node[2])
        self.G.add_edges_from(edges_list)
        parse_code.clear_tables()
        self.draw(parse_code.same_rank_nodes)





# Main function to call it into __main__
def main():
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet())    
    window = MyGUI()
    app.exec()



if __name__ == "__main__":
    main()