from hashlib import algorithms_available
from GUI.GUIv7 import *
import numpy as np
import sys
import io
import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QRadioButton, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import scipy.signal as signal

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.offsetbox import AnchoredText
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from PyQt5 import QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.initGraphs()

        #H(s)
        self.num_1 = [0.0, 0.0]
        self.denom_1 = [0.0, 1.0]

        self.num_2 = [0.0, 0.0, 0.0]
        self.denom_2 = [0.0, 0.0, 1.0]

        self.num_rlc = [0.0, 0.0, 0.0]
        self.denom_rlc = [0.0, 0.0, 1.0]

        #Botones RLC
        self.button_A = 0
        self.button_B = 4

        #Updates
        self.validateEntries()
        self.setTrasferFuncions()
        self.updatePlots()
        self.updateTransferFunctions()

    def validateEntries(self):
        #Validar entradas
        self.editcero_1.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))
        self.editpolo_1.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))
        self.editganancia_1.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))
        self.editfrecuencia_1.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))
        self.editamplitud_1.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))

        self.editw0_2.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))
        self.editxi_2.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))
        self.editganancia_2.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))
        self.editfrecuencia_2.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))
        self.editamplitud_2.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))

        self.edit_r.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))
        self.edit_l.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))
        self.edit_c.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))
        self.editfrecuencia_rlc.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))
        self.editamplitud_rlc.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))
        
    def initGraphs(self):
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

        #Funcion transferencia Filtros 1er orden
        self.figureTF_1 = Figure()
        self.canvasTF_1 = FigureCanvas(self.figureTF_1)
        self.axesTF_1 = self.figureTF_1.subplots()
        self.funciontransferencialayout_1.addWidget(self.canvasTF_1)
        self.axesTF_1.axis('off')

        #Funcion transferencia Filtros 2do orden
        self.figureTF_2 = Figure()
        self.canvasTF_2 = FigureCanvas(self.figureTF_2)
        self.axesTF_2 = self.figureTF_2.subplots()
        self.funciontransferencialayout_2.addWidget(self.canvasTF_2)
        self.axesTF_2.axis('off')

        #Funcion transferencia RLC
        self.figureTF_rlc = Figure()
        self.canvasTF_rlc = FigureCanvas(self.figureTF_rlc)
        self.axesTF_rlc = self.figureTF_rlc.subplots()
        self.funciontransferencia_rlc.addWidget(self.canvasTF_rlc)
        self.axesTF_rlc.axis('off')

    def updatePlots(self):
        # Filtros de 1er orden
        self.axes1_amp.set_xlabel('$Frecuencia [rad/s]$')
        self.axes1_amp.set_ylabel('$|H(jw)| [dB]$')
        self.axes1_amp.grid(True, which='both')
        self.figure1_amp.set_tight_layout('True')
        self.figure1_amp.tight_layout()
        self.canvas1_amp.draw()

        self.axes1_fase.set_xlabel('$Frecuencia [rad/s]$')
        self.axes1_fase.set_ylabel('$Fase [\u00B0]$')
        self.axes1_fase.grid(True, which='both')
        self.figure1_fase.set_tight_layout('True')
        self.figure1_fase.tight_layout()
        self.canvas1_fase.draw()

        self.axes1_ceros.set_xlabel('$\u03C3$')
        self.axes1_ceros.set_ylabel('$j\omega$')
        self.axes1_ceros.grid(True, which='both')
        self.figure1_ceros.tight_layout()
        self.figure1_ceros.set_tight_layout('True')
        self.canvas1_ceros.draw()

        self.axes1_out.set_xlabel('$t [s]$')
        self.axes1_out.set_ylabel('$f(t)$')
        self.axes1_out.grid(True, which='both')
        self.figure1_out.set_tight_layout('True')
        self.figure1_out.tight_layout()
        self.canvas1_out.draw()

        # Filtros de 2do orden
        self.axes2_amp.set_xlabel('$Frecuencia [rad/s]$')
        self.axes2_amp.set_ylabel('$|H(jw)| [dB]$')
        self.axes2_amp.grid(True, which='both')
        self.figure2_amp.set_tight_layout('True')
        self.figure2_amp.tight_layout()
        self.canvas2_amp.draw()

        self.axes2_fase.set_xlabel('$Frecuencia [rad/s]$')
        self.axes2_fase.set_ylabel('$Fase [\u00B0]$')
        self.axes2_fase.grid(True, which='both')
        self.figure2_fase.set_tight_layout('True')
        self.figure2_fase.tight_layout()
        self.canvas2_fase.draw()

        self.axes2_ceros.set_xlabel('$\u03C3$')
        self.axes2_ceros.set_ylabel('$j\omega$')
        self.axes2_ceros.grid(True, which='both')
        self.figure2_ceros.tight_layout()
        self.figure2_ceros.set_tight_layout('True')
        self.canvas2_ceros.draw()

        self.axes2_out.set_xlabel('$t [s]$')
        self.axes2_out.set_ylabel('$f(t)$')
        self.axes2_out.grid(True, which='both')
        self.figure2_out.set_tight_layout('True')
        self.figure2_out.tight_layout()
        self.canvas2_out.draw()

        # RLC
        self.axesrlc_amp.set_xlabel('$Frecuencia [rad/s]$')
        self.axesrlc_amp.set_ylabel('$|H(jw)| [dB]$')
        self.axesrlc_amp.grid(True, which='both')
        self.figurerlc_amp.set_tight_layout('True')
        self.figurerlc_amp.tight_layout()
        self.canvasrlc_amp.draw()

        self.axesrlc_fase.set_xlabel('$Frecuencia [rad/s]$')
        self.axesrlc_fase.set_ylabel('$Fase [\u00B0]$')
        self.axesrlc_fase.grid(True, which='both')
        self.figurerlc_fase.set_tight_layout('True')
        self.figurerlc_fase.tight_layout()
        self.canvasrlc_fase.draw()

        self.axesrlc_out.set_xlabel('$t [s]$')
        self.axesrlc_out.set_ylabel('$f(t) [V]$')
        self.axesrlc_out.grid(True, which='both')
        self.figurerlc_out.set_tight_layout('True')
        self.figurerlc_out.tight_layout()
        self.canvasrlc_out.draw()

    def setTrasferFuncions(self):
        #Filtros 1er Orden
        self.at_1 = AnchoredText('$H(s) =' , prop=dict(size=16), frameon=False, loc='upper left')
        self.at_1.patch.set_boxstyle("square,pad=0.")
        self.axesTF_1.add_artist(self.at_1)
        self.canvasTF_1.draw()

        #Filtros 2do Orden
        self.at_2 = AnchoredText('$H(s) =', prop=dict(size=16), frameon=False, loc='upper left')
        self.at_2.patch.set_boxstyle("square,pad=0.")
        self.axesTF_2.add_artist(self.at_2)
        self.canvasTF_2.draw()

        #RLC
        self.at_rlc = AnchoredText('$H(s) =', prop=dict(size=20), frameon=False, loc='upper left')
        self.at_rlc.patch.set_boxstyle("square,pad=0.")
        self.axesTF_rlc.add_artist(self.at_rlc)
        self.canvasTF_rlc.draw()

    def updateTransferFunctions(self):
        #Filtros 1er Orden
        sign = "+ " if (self.num_1[1] >= 0) else " "
        numerator_1 = str(self.num_1[0]) + "s " + sign + str(self.num_1[1]) 

        sign = "+ " if (self.denom_1[1] >= 0) else " "
        denominator_1 = str(self.denom_1[0]) + "s " + sign + str(self.denom_1[1])

        self.at_1.txt.set_text('$H(s) = \\dfrac{%s}{%s}$' %(numerator_1,denominator_1))
        self.axesTF_1.add_artist(self.at_1)
        self.canvasTF_1.draw()

        #Filtros 2do Orden
        sign = "+ " if (self.num_2[1] >= 0) else " "
        sign2 = "+ " if (self.num_2[2] >= 0) else " "
        numerator_2 = str(self.num_2[0]) + "s² " + sign + str(self.num_2[1]) + "s " + sign2 + str(self.num_2[2]) 

        sign = "+ " if (self.denom_2[1] >= 0) else " "
        sign2 = "+ " if (self.denom_2[2] >= 0) else " "
        denominator_2 = str(self.denom_2[0]) + "s² " + sign + str(self.denom_2[1]) + "s " + sign2 + str(self.denom_2[2])
        
        self.at_2.txt.set_text('$H(s) = \\dfrac{%s}{%s}$' %(numerator_2,denominator_2))
        self.at_2.patch.set_boxstyle("square,pad=0.")
        self.axesTF_2.add_artist(self.at_2)
        self.canvasTF_2.draw()

        #RLC
        sign = "+ " if (self.num_rlc[1] >= 0) else " "
        sign2 = "+ " if (self.num_rlc[2] >= 0) else " "
        numerator_rlc = str(self.num_rlc[0]) + "s² " + sign + str(self.num_rlc[1]) + "s " + sign2 + str(self.num_rlc[2]) 

        sign = "+ " if (self.denom_rlc[1] >= 0) else " "
        sign2 = "+ " if (self.denom_rlc[2] >= 0) else " "
        denominator_rlc = str(self.denom_rlc[0]) + "s² " + sign + str(self.denom_rlc[1]) + "s " + sign2 + str(self.denom_rlc[2])
        
        self.at_rlc.txt.set_text('$H(s) = \\dfrac{%s}{%s}$' %(numerator_rlc,denominator_rlc))
        self.at_rlc.patch.set_boxstyle("square,pad=0.")
        self.axesTF_rlc.add_artist(self.at_rlc)
        self.canvasTF_rlc.draw()

    #Callbacks
    def bodeChanged_1(self):
        filterType_1 = self.filtertype_1.currentText()
        try:
            cero_1 = float(self.editcero_1.text())
            polo_1 = float(self.editpolo_1.text())
            ganancia_1 = float(self.editganancia_1.text())
        
            #esto es para arbitrario
            if(cero_1 == 0.0):
                self.num_1[0] = 1.0 * ganancia_1
                self.num_1[1] = 0.0
            else:
                self.num_1[0] = cero_1**(-1) * ganancia_1
                self.num_1[1] = 1.0 * ganancia_1

            if(polo_1 == 0.0):
                self.denom_1[0] = 1.0
                self.denom_1[1] = 0.0
            else:
                self.denom_1[0] = polo_1**(-1)
                self.denom_1[1] = 1.0
            
            self.updateTransferFunctions()

        except :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No puede haber entradas vacias, o con ',' \n No se puede dividir por 0")
            msg.setWindowTitle("Error")
            msg.exec_()


    def entradaChanged_1(self):
        entrytype_1 = self.entrytype_1.currentText()
        ampentrada_1 = float(self.editamplitud_1.text())
        frecentrada_1 = float(self.editfrecuencia_1.text())

    def bodeChanged_2(self):
        filterType_2 = self.filtertype_2.currentText()

        try:
            w0_2 = float(self.editw0_2.text())
            xi_2 = float(self.editxi_2.text())
            ganancia_2 = float(self.editganancia_2.text())
        
            #esto es para arbitrario
            self.num_2[0] = 0.0 
            self.num_2[1] = 0.0
            self.num_2[2] = 1.0 * ganancia_2

            self.denom_2[0] = 1.0
            self.denom_2[1] = 2 * xi_2 / w0_2
            self.denom_2[2] = w0_2 ** (-2)
            
            self.updateTransferFunctions()

        except :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No puede haber entradas vacias, o con ',' \n No se puede dividir por 0")
            msg.setWindowTitle("Error")
            msg.exec_()

    def entradaChanged_2(self):
        entrytype_2 = self.entrytype_2.currentText()
        ampentrada_2 = float(self.editamplitud_2.text())
        frecentrada_2 = float(self.editfrecuencia_2.text())

    def entradaChanged_rlc(self):
        entrytype_rlc = self.entrytype_rlc.currentText()
        R = float(self.edit_r.text())
        L = float(self.edit_l.text())
        C = float(self.edit_c.text())
        ampentrada_rlc = float(self.editamplitud_rlc.text())
        frecentrada_rlc = float(self.editfrecuencia_rlc.text())

    def bodeChanged_rlc(self):
        try:
            R = float(self.edit_r.text())
            L = float(self.edit_l.text())
            C = float(self.edit_c.text())

            termcuadrado = 0.0
            termsimple = 0.0
            termindep = 0.0

            match (self.button_A):
                case 1:
                    termcuadrado += L * C
                    termsimple += R
                    termindep += 1.0
                case 2:
                    termcuadrado += L * C
                    termsimple += 0.0
                    termindep += 1.0
                case 3: 
                    termcuadrado += 0.0
                    termsimple += 0.0
                    termindep += 1.0
                case 4:
                    termcuadrado += 0.0
                    termsimple += 0.0
                    termindep += 0.0

            match(self.button_B):
                case 1:
                    termcuadrado -= L * C
                    termsimple -= R
                    termindep -= 1.0
                case 2:
                    termcuadrado -= L * C
                    termsimple -= 0.0
                    termindep -= 1.0
                case 3: 
                    termcuadrado -= 0.0
                    termsimple -= 0.0
                    termindep -= 1.0
                case 4:
                    termcuadrado -= 0.0
                    termsimple -= 0.0
                    termindep -= 0.0
        
            #esto es para arbitrario
            self.num_rlc[0] = termcuadrado
            self.num_rlc[1] = C * termsimple
            self.num_rlc[2] = termindep

            self.denom_rlc[0] = L * C
            self.denom_rlc[1] = R * C
            self.denom_rlc[2] = 1.0
            
            self.updateTransferFunctions()

        except :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No puede haber entradas vacias, o con ',' ")
            msg.setWindowTitle("Error")
            msg.exec_()
        

    def vButton_1a(self):
        self.button_A = 1
        self.bodeChanged_rlc()
        self.entradaChanged_rlc()

    def vButton_2a(self):
        self.button_A = 2
        self.bodeChanged_rlc()
        self.entradaChanged_rlc()

    def vButton_3a(self):
        self.button_A = 3
        self.bodeChanged_rlc()
        self.entradaChanged_rlc()

    def vButton_4a(self):
        self.button_A = 4
        self.bodeChanged_rlc()
        self.entradaChanged_rlc()

    def vButton_1b(self):
        self.button_B = 1
        self.bodeChanged_rlc()
        self.entradaChanged_rlc()

    def vButton_2b(self):
        self.button_B = 2
        self.bodeChanged_rlc()
        self.entradaChanged_rlc()

    def vButton_3b(self):
        self.button_B = 3
        self.bodeChanged_rlc()
        self.entradaChanged_rlc()

    def vButton_4b(self):
        self.button_B = 4
        self.bodeChanged_rlc()
        self.entradaChanged_rlc()

################################################################

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()