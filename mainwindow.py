from GUI.GUIv4 import *
import numpy as np
import sys
import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QRadioButton, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import scipy.signal as signal

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from PyQt5 import QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        #GRAFICOS
        # Grafico Amplitud Filtros 1er orden
        self.figure1_amp = Figure()
        self.canvas1_amp = FigureCanvas(self.figure1_amp)
        self.axes1_amp = self.figure1_amp.subplots()
        self.bodeamplitudelayout_1.addWidget(NavigationToolbar(self.canvas1_amp, self))
        self.bodeamplitudelayout_1.addWidget(self.canvas1_amp)

        self.axes1_amp.set_xscale('log')

        # Grafico Fase Filtros 1er orden
        self.figure1_fase = Figure()
        self.canvas1_fase = FigureCanvas(self.figure1_fase)
        self.axes1_fase = self.figure1_fase.subplots()
        self.bodefaselayout_1.addWidget(NavigationToolbar(self.canvas1_fase, self))
        self.bodefaselayout_1.addWidget(self.canvas1_fase)

        self.axes1_fase.set_xscale('log')

        # Grafico Ceros Filtros 1er orden
        self.figure1_ceros = Figure()
        self.canvas1_ceros = FigureCanvas(self.figure1_ceros)
        self.axes1_ceros = self.figure1_ceros.subplots()
        self.zeroeslayout_1.addWidget(NavigationToolbar(self.canvas1_ceros, self))
        self.zeroeslayout_1.addWidget(self.canvas1_ceros)

        # Grafico Salida Filtros 1er orden
        self.figure1_out = Figure()
        self.canvas1_out = FigureCanvas(self.figure1_out)
        self.axes1_out = self.figure1_out.subplots()
        self.outputexcitationlayout_1.addWidget(NavigationToolbar(self.canvas1_out, self))
        self.outputexcitationlayout_1.addWidget(self.canvas1_out)

        # Grafico Amplitud Filtros 2do orden
        self.figure2_amp = Figure()
        self.canvas2_amp = FigureCanvas(self.figure2_amp)
        self.axes2_amp = self.figure2_amp.subplots()
        self.bodeamplitudelayout_2.addWidget(NavigationToolbar(self.canvas2_amp, self))
        self.bodeamplitudelayout_2.addWidget(self.canvas2_amp)

        self.axes2_amp.set_xscale('log')

        # Grafico Fase Filtros 2do orden
        self.figure2_fase = Figure()
        self.canvas2_fase = FigureCanvas(self.figure2_fase)
        self.axes2_fase = self.figure2_fase.subplots()
        self.bodefaselayout_2.addWidget(NavigationToolbar(self.canvas2_fase, self))
        self.bodefaselayout_2.addWidget(self.canvas2_fase)

        self.axes2_fase.set_xscale('log')

        # Grafico Ceros Filtros 2do orden
        self.figure2_ceros = Figure()
        self.canvas2_ceros = FigureCanvas(self.figure2_ceros)
        self.axes2_ceros = self.figure2_ceros.subplots()
        self.zeroeslayout_2.addWidget(NavigationToolbar(self.canvas2_ceros, self))
        self.zeroeslayout_2.addWidget(self.canvas2_ceros)

        # Grafico Salida Filtros 2do orden
        self.figure2_out = Figure()
        self.canvas2_out = FigureCanvas(self.figure2_out)
        self.axes2_out = self.figure2_out.subplots()
        self.outputexcitationlayout_2.addWidget(NavigationToolbar(self.canvas2_out, self))
        self.outputexcitationlayout_2.addWidget(self.canvas2_out)

        # Grafico Amplitud RLC
        self.figurerlc_amp = Figure()
        self.canvasrlc_amp = FigureCanvas(self.figurerlc_amp)
        self.axesrlc_amp = self.figurerlc_amp.subplots()
        self.bodeamplitudelayout_rlc.addWidget(NavigationToolbar(self.canvasrlc_amp, self))
        self.bodeamplitudelayout_rlc.addWidget(self.canvasrlc_amp)

        self.axesrlc_amp.set_xscale('log')

        # Grafico Fase RLC
        self.figurerlc_fase = Figure()
        self.canvasrlc_fase = FigureCanvas(self.figurerlc_fase)
        self.axesrlc_fase = self.figurerlc_fase.subplots()
        self.bodefaselayout_rlc.addWidget(NavigationToolbar(self.canvasrlc_fase, self))
        self.bodefaselayout_rlc.addWidget(self.canvasrlc_fase)

        self.axesrlc_fase.set_xscale('log')

        # Grafico Salida RLC
        self.figurerlc_out = Figure()
        self.canvasrlc_out = FigureCanvas(self.figurerlc_out)
        self.axesrlc_out = self.figurerlc_out.subplots()
        self.outputlayout_rlc.addWidget(NavigationToolbar(self.canvasrlc_out, self))
        self.outputlayout_rlc.addWidget(self.canvasrlc_out)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()