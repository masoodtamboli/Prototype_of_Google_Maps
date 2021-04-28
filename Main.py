from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
import sys

from Dijktras import Dij_Algo
from model import graph
import networkx as nx

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.text = '''
Implementing Google Maps Using
       Dijiktras Algorithm
'''
        MainWindow.setObjectName("Google Maps")
        MainWindow.resize(1366, 768)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(40,0,0,0))
        self.Title.setObjectName("Title")
        self.label_font = QtGui.QFont()
        self.label_font.setPointSize(22)
        self.Title.setFont(self.label_font)
        self.Title.resize(550,180)

        #TextField to get source location
        self.Source = QtWidgets.QLineEdit(self.centralwidget)
        self.Source.setGeometry(QtCore.QRect(670, 30, 131, 31))
        self.Source.setObjectName("Source")
        self.Source.setPlaceholderText("Source")

        self._to = QtWidgets.QLabel(self.centralwidget)
        self._to.setGeometry(QtCore.QRect(830,30,131,31))
        self._to.setObjectName("_to")
        self.label_font = QtGui.QFont()
        self.label_font.setPointSize(15)
        self._to.setFont(self.label_font)

        #TextField for Dest 1
        self.Destination1 = QtWidgets.QLineEdit(self.centralwidget)
        self.Destination1.setGeometry(QtCore.QRect(900, 30, 131, 31))
        self.Destination1.setObjectName("Destination1")
        self.Destination1.setPlaceholderText("Destination")

        #Locate button to find best path
        self.Locate = QtWidgets.QPushButton(self.centralwidget)
        self.Locate.setGeometry(QtCore.QRect(1100, 30, 121, 31))
        self.Locate.setStyleSheet("background-color:gray;\n""border-style:outset;\n""border-radius:10px;")
        self.Locate.setObjectName("Locate")
        self.Locate.clicked.connect(lambda: self.Dijkstra())

        #Vertical Layout to show Graph
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(670, 90, 806, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.Opt_path = QtWidgets.QLabel(self.centralwidget)
        self.Opt_path.setGeometry(QtCore.QRect(40,170,0,0))
        self.Opt_path.setObjectName("Opt_path")
        self.label_font = QtGui.QFont()
        self.label_font.setPointSize(15)
        self.Opt_path.setFont(self.label_font)
        self.Opt_path.resize(550,180)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Google Maps"))
        self.Locate.setText(_translate("MainWindow", "Locate"))
        self.Title.setText(_translate("MainWindow",self.text))
        self.Opt_path.setText(_translate("MainWindow",""))
        self._to.setText(_translate("MainWindow"," to "))
    
    def Dijkstra(self):
        self.src = str(self.Source.text())
        self.dst = str(self.Destination1.text())
        SD, TP = Dij_Algo(graph, self.src, self.dst)
        self.Opt_path.setText("Shortest Distance from "+ str(self.src) +" to "+ str(self.dst) +" is : "+SD)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout.addChildWidget(self.canvas)
        G = nx.path_graph(TP)

        nx.draw(G, with_labels =1)
        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
