# Form implementation generated from reading ui file 'GUIv7.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1550, 1100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mainframe = QtWidgets.QFrame(self.centralwidget)
        self.mainframe.setObjectName("mainframe")
        self.gridLayout = QtWidgets.QGridLayout(self.mainframe)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.mainframe)
        self.tabWidget.setObjectName("tabWidget")
        self.tabprimerorden = QtWidgets.QWidget()
        self.tabprimerorden.setObjectName("tabprimerorden")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tabprimerorden)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 781, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.bodeamplitudelayout_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.bodeamplitudelayout_1.setContentsMargins(0, 0, 0, 0)
        self.bodeamplitudelayout_1.setObjectName("bodeamplitudelayout_1")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tabprimerorden)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(800, 80, 651, 391))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.bodefaselayout_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.bodefaselayout_1.setContentsMargins(0, 0, 0, 0)
        self.bodefaselayout_1.setObjectName("bodefaselayout_1")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tabprimerorden)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 480, 451, 431))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.zeroeslayout_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.zeroeslayout_1.setContentsMargins(0, 0, 0, 0)
        self.zeroeslayout_1.setObjectName("zeroeslayout_1")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tabprimerorden)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(470, 560, 981, 351))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.outputexcitationlayout_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.outputexcitationlayout_1.setContentsMargins(0, 0, 0, 0)
        self.outputexcitationlayout_1.setObjectName("outputexcitationlayout_1")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tabprimerorden)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 561, 71))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.filtromenulayout_1 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.filtromenulayout_1.setContentsMargins(0, 0, 0, 0)
        self.filtromenulayout_1.setObjectName("filtromenulayout_1")
        self.labeltipofiltro_1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labeltipofiltro_1.setObjectName("labeltipofiltro_1")
        self.filtromenulayout_1.addWidget(self.labeltipofiltro_1, 0, 0, 1, 1)
        self.labelganancia_1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelganancia_1.setObjectName("labelganancia_1")
        self.filtromenulayout_1.addWidget(self.labelganancia_1, 0, 3, 1, 1)
        self.editganancia_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.editganancia_1.setObjectName("editganancia_1")
        self.filtromenulayout_1.addWidget(self.editganancia_1, 1, 3, 1, 1)
        self.editpolo_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.editpolo_1.setObjectName("editpolo_1")
        self.filtromenulayout_1.addWidget(self.editpolo_1, 1, 2, 1, 1)
        self.labelpolo_1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelpolo_1.setObjectName("labelpolo_1")
        self.filtromenulayout_1.addWidget(self.labelpolo_1, 0, 2, 1, 1)
        self.editcero_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.editcero_1.setObjectName("editcero_1")
        self.filtromenulayout_1.addWidget(self.editcero_1, 1, 1, 1, 1)
        self.labelcero_1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelcero_1.setObjectName("labelcero_1")
        self.filtromenulayout_1.addWidget(self.labelcero_1, 0, 1, 1, 1)
        self.filtertype_1 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.filtertype_1.setObjectName("filtertype_1")
        self.filtertype_1.addItem("")
        self.filtertype_1.addItem("")
        self.filtertype_1.addItem("")
        self.filtertype_1.addItem("")
        self.filtromenulayout_1.addWidget(self.filtertype_1, 1, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tabprimerorden)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(470, 480, 601, 71))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.entradamenulayout_1 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.entradamenulayout_1.setContentsMargins(0, 0, 0, 0)
        self.entradamenulayout_1.setObjectName("entradamenulayout_1")
        self.entrytype_1 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.entrytype_1.setObjectName("entrytype_1")
        self.entrytype_1.addItem("")
        self.entrytype_1.addItem("")
        self.entrytype_1.addItem("")
        self.entrytype_1.addItem("")
        self.entradamenulayout_1.addWidget(self.entrytype_1, 2, 0, 1, 1)
        self.labelamplitud_1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.labelamplitud_1.setObjectName("labelamplitud_1")
        self.entradamenulayout_1.addWidget(self.labelamplitud_1, 1, 1, 1, 1)
        self.editamplitud_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.editamplitud_1.setObjectName("editamplitud_1")
        self.entradamenulayout_1.addWidget(self.editamplitud_1, 2, 1, 1, 1)
        self.labeltipoentrada_1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.labeltipoentrada_1.setObjectName("labeltipoentrada_1")
        self.entradamenulayout_1.addWidget(self.labeltipoentrada_1, 1, 0, 1, 1)
        self.labelfrecuencia_1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.labelfrecuencia_1.setObjectName("labelfrecuencia_1")
        self.entradamenulayout_1.addWidget(self.labelfrecuencia_1, 1, 2, 1, 1)
        self.editfrecuencia_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.editfrecuencia_1.setObjectName("editfrecuencia_1")
        self.entradamenulayout_1.addWidget(self.editfrecuencia_1, 2, 2, 1, 1)
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(self.tabprimerorden)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(580, 0, 511, 71))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.funciontransferencialayout_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.funciontransferencialayout_1.setContentsMargins(0, 0, 0, 0)
        self.funciontransferencialayout_1.setObjectName("funciontransferencialayout_1")
        self.tabWidget.addTab(self.tabprimerorden, "")
        self.tabsegundoorden = QtWidgets.QWidget()
        self.tabsegundoorden.setObjectName("tabsegundoorden")
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.tabsegundoorden)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(10, 0, 561, 71))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.filtromenulayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.filtromenulayout_2.setContentsMargins(0, 0, 0, 0)
        self.filtromenulayout_2.setObjectName("filtromenulayout_2")
        self.labeltipofiltro_2 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.labeltipofiltro_2.setObjectName("labeltipofiltro_2")
        self.filtromenulayout_2.addWidget(self.labeltipofiltro_2, 0, 0, 1, 1)
        self.labelw0_2 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.labelw0_2.setObjectName("labelw0_2")
        self.filtromenulayout_2.addWidget(self.labelw0_2, 0, 1, 1, 1)
        self.labelxi_2 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.labelxi_2.setObjectName("labelxi_2")
        self.filtromenulayout_2.addWidget(self.labelxi_2, 0, 2, 1, 1)
        self.labelganancia_2 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.labelganancia_2.setObjectName("labelganancia_2")
        self.filtromenulayout_2.addWidget(self.labelganancia_2, 0, 3, 1, 1)
        self.filtertype_2 = QtWidgets.QComboBox(self.gridLayoutWidget_8)
        self.filtertype_2.setObjectName("filtertype_2")
        self.filtertype_2.addItem("")
        self.filtertype_2.addItem("")
        self.filtertype_2.addItem("")
        self.filtertype_2.addItem("")
        self.filtertype_2.addItem("")
        self.filtertype_2.addItem("")
        self.filtromenulayout_2.addWidget(self.filtertype_2, 1, 0, 1, 1)
        self.editw0_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.editw0_2.setObjectName("editw0_2")
        self.filtromenulayout_2.addWidget(self.editw0_2, 1, 1, 1, 1)
        self.editxi_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.editxi_2.setObjectName("editxi_2")
        self.filtromenulayout_2.addWidget(self.editxi_2, 1, 2, 1, 1)
        self.editganancia_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.editganancia_2.setObjectName("editganancia_2")
        self.filtromenulayout_2.addWidget(self.editganancia_2, 1, 3, 1, 1)
        self.verticalLayoutWidget_15 = QtWidgets.QWidget(self.tabsegundoorden)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(580, 0, 511, 71))
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.funciontransferencialayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_15)
        self.funciontransferencialayout_2.setContentsMargins(0, 0, 0, 0)
        self.funciontransferencialayout_2.setObjectName("funciontransferencialayout_2")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tabsegundoorden)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 80, 781, 391))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.bodeamplitudelayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.bodeamplitudelayout_2.setContentsMargins(0, 0, 0, 0)
        self.bodeamplitudelayout_2.setObjectName("bodeamplitudelayout_2")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.tabsegundoorden)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(800, 80, 651, 391))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.bodefaselayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.bodefaselayout_2.setContentsMargins(0, 0, 0, 0)
        self.bodefaselayout_2.setObjectName("bodefaselayout_2")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.tabsegundoorden)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 480, 451, 431))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.zeroeslayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.zeroeslayout_2.setContentsMargins(0, 0, 0, 0)
        self.zeroeslayout_2.setObjectName("zeroeslayout_2")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.tabsegundoorden)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(470, 560, 981, 351))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.outputexcitationlayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.outputexcitationlayout_2.setContentsMargins(0, 0, 0, 0)
        self.outputexcitationlayout_2.setObjectName("outputexcitationlayout_2")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tabsegundoorden)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(470, 480, 601, 71))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.entradamenulayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.entradamenulayout_2.setContentsMargins(0, 0, 0, 0)
        self.entradamenulayout_2.setObjectName("entradamenulayout_2")
        self.labeltipoentrada_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.labeltipoentrada_2.setObjectName("labeltipoentrada_2")
        self.entradamenulayout_2.addWidget(self.labeltipoentrada_2, 1, 0, 1, 1)
        self.entrytype_2 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.entrytype_2.setObjectName("entrytype_2")
        self.entrytype_2.addItem("")
        self.entrytype_2.addItem("")
        self.entrytype_2.addItem("")
        self.entrytype_2.addItem("")
        self.entradamenulayout_2.addWidget(self.entrytype_2, 2, 0, 1, 1)
        self.labelamplitud_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.labelamplitud_2.setObjectName("labelamplitud_2")
        self.entradamenulayout_2.addWidget(self.labelamplitud_2, 1, 1, 1, 1)
        self.editamplitud_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.editamplitud_2.setObjectName("editamplitud_2")
        self.entradamenulayout_2.addWidget(self.editamplitud_2, 2, 1, 1, 1)
        self.labelfrecuencia_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.labelfrecuencia_2.setObjectName("labelfrecuencia_2")
        self.entradamenulayout_2.addWidget(self.labelfrecuencia_2, 1, 2, 1, 1)
        self.editfrecuencia_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.editfrecuencia_2.setObjectName("editfrecuencia_2")
        self.entradamenulayout_2.addWidget(self.editfrecuencia_2, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tabsegundoorden, "")
        self.tabrlc = QtWidgets.QWidget()
        self.tabrlc.setObjectName("tabrlc")
        self.imagen_rlc = QtWidgets.QLabel(self.tabrlc)
        self.imagen_rlc.setGeometry(QtCore.QRect(190, 0, 421, 191))
        self.imagen_rlc.setText("")
        self.imagen_rlc.setPixmap(QtGui.QPixmap("Proyectofinal_Electrotecnia\GUI\Electro.png"))
        self.imagen_rlc.setScaledContents(True)
        self.imagen_rlc.setObjectName("imagen_rlc")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.tabrlc)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(790, 0, 521, 191))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.funciontransferencia_rlc = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.funciontransferencia_rlc.setContentsMargins(0, 0, 0, 0)
        self.funciontransferencia_rlc.setObjectName("funciontransferencia_rlc")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.tabrlc)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(10, 280, 1441, 261))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.outputlayout_rlc = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.outputlayout_rlc.setContentsMargins(0, 0, 0, 0)
        self.outputlayout_rlc.setObjectName("outputlayout_rlc")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.tabrlc)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(10, 560, 741, 351))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.bodeamplitudelayout_rlc = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.bodeamplitudelayout_rlc.setContentsMargins(0, 0, 0, 0)
        self.bodeamplitudelayout_rlc.setObjectName("bodeamplitudelayout_rlc")
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.tabrlc)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(760, 560, 691, 351))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.bodefaselayout_rlc = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.bodefaselayout_rlc.setContentsMargins(0, 0, 0, 0)
        self.bodefaselayout_rlc.setObjectName("bodefaselayout_rlc")
        self.formLayoutWidget = QtWidgets.QWidget(self.tabrlc)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 171, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.menu_rlc = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.menu_rlc.setContentsMargins(0, 0, 0, 0)
        self.menu_rlc.setObjectName("menu_rlc")
        self.r_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.r_label.setObjectName("r_label")
        self.menu_rlc.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.r_label)
        self.edit_r = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edit_r.setObjectName("edit_r")
        self.menu_rlc.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.edit_r)
        self.l_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_label.setObjectName("l_label")
        self.menu_rlc.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.l_label)
        self.edit_l = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edit_l.setObjectName("edit_l")
        self.menu_rlc.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.edit_l)
        self.c_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.c_label.setObjectName("c_label")
        self.menu_rlc.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.c_label)
        self.edit_c = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edit_c.setObjectName("edit_c")
        self.menu_rlc.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.edit_c)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.tabrlc)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(620, 20, 151, 151))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.potencialeslayout_rlc = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.potencialeslayout_rlc.setContentsMargins(0, 0, 0, 0)
        self.potencialeslayout_rlc.setObjectName("potencialeslayout_rlc")
        self.V_a = QtWidgets.QGroupBox(self.gridLayoutWidget_7)
        self.V_a.setTitle("")
        self.V_a.setObjectName("V_a")
        self.vbutton_2a = QtWidgets.QRadioButton(self.V_a)
        self.vbutton_2a.setGeometry(QtCore.QRect(0, 30, 71, 41))
        self.vbutton_2a.setObjectName("vbutton_2a")
        self.vbutton_3a = QtWidgets.QRadioButton(self.V_a)
        self.vbutton_3a.setGeometry(QtCore.QRect(0, 70, 71, 31))
        self.vbutton_3a.setObjectName("vbutton_3a")
        self.vbutton_4a = QtWidgets.QRadioButton(self.V_a)
        self.vbutton_4a.setGeometry(QtCore.QRect(0, 107, 71, 31))
        self.vbutton_4a.setObjectName("vbutton_4a")
        self.vbutton_1a = QtWidgets.QRadioButton(self.V_a)
        self.vbutton_1a.setGeometry(QtCore.QRect(0, 0, 71, 31))
        self.vbutton_1a.setObjectName("vbutton_1a")
        self.potencialeslayout_rlc.addWidget(self.V_a, 0, 0, 1, 1)
        self.V_b = QtWidgets.QGroupBox(self.gridLayoutWidget_7)
        self.V_b.setTitle("")
        self.V_b.setObjectName("V_b")
        self.vbutton_2b = QtWidgets.QRadioButton(self.V_b)
        self.vbutton_2b.setGeometry(QtCore.QRect(0, 30, 71, 41))
        self.vbutton_2b.setObjectName("vbutton_2b")
        self.vbutton_3b = QtWidgets.QRadioButton(self.V_b)
        self.vbutton_3b.setGeometry(QtCore.QRect(0, 70, 71, 31))
        self.vbutton_3b.setObjectName("vbutton_3b")
        self.vbutton_4b = QtWidgets.QRadioButton(self.V_b)
        self.vbutton_4b.setGeometry(QtCore.QRect(0, 107, 71, 31))
        self.vbutton_4b.setObjectName("vbutton_4b")
        self.vbutton_1b = QtWidgets.QRadioButton(self.V_b)
        self.vbutton_1b.setGeometry(QtCore.QRect(0, 0, 71, 31))
        self.vbutton_1b.setObjectName("vbutton_1b")
        self.potencialeslayout_rlc.addWidget(self.V_b, 0, 1, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tabrlc)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 200, 601, 71))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.entradamenulayout_rlc = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.entradamenulayout_rlc.setContentsMargins(0, 0, 0, 0)
        self.entradamenulayout_rlc.setObjectName("entradamenulayout_rlc")
        self.entrytype_rlc = QtWidgets.QComboBox(self.gridLayoutWidget_5)
        self.entrytype_rlc.setObjectName("entrytype_rlc")
        self.entrytype_rlc.addItem("")
        self.entrytype_rlc.addItem("")
        self.entrytype_rlc.addItem("")
        self.entrytype_rlc.addItem("")
        self.entradamenulayout_rlc.addWidget(self.entrytype_rlc, 2, 0, 1, 1)
        self.labelamplitud_rlc = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.labelamplitud_rlc.setObjectName("labelamplitud_rlc")
        self.entradamenulayout_rlc.addWidget(self.labelamplitud_rlc, 1, 1, 1, 1)
        self.editfrecuencia_rlc = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.editfrecuencia_rlc.setObjectName("editfrecuencia_rlc")
        self.entradamenulayout_rlc.addWidget(self.editfrecuencia_rlc, 2, 2, 1, 1)
        self.labeltipoentrada_rlc = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.labeltipoentrada_rlc.setObjectName("labeltipoentrada_rlc")
        self.entradamenulayout_rlc.addWidget(self.labeltipoentrada_rlc, 1, 0, 1, 1)
        self.labelfrecuencia_rlc = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.labelfrecuencia_rlc.setObjectName("labelfrecuencia_rlc")
        self.entradamenulayout_rlc.addWidget(self.labelfrecuencia_rlc, 1, 2, 1, 1)
        self.editamplitud_rlc = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.editamplitud_rlc.setObjectName("editamplitud_rlc")
        self.entradamenulayout_rlc.addWidget(self.editamplitud_rlc, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tabrlc, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.mainframe, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.filtertype_1.activated['int'].connect(MainWindow.bodeChanged_1)
        self.entrytype_1.activated['int'].connect(MainWindow.entradaChanged_1)
        self.filtertype_2.activated['int'].connect(MainWindow.bodeChanged_2)
        self.entrytype_2.activated['int'].connect(MainWindow.entradaChanged_2)
        self.entrytype_rlc.activated['int'].connect(MainWindow.entradaChanged_rlc)

        self.editcero_1.textChanged.connect(MainWindow.bodeChanged_1)
        self.editpolo_1.textChanged.connect(MainWindow.bodeChanged_1)
        self.editganancia_1.textChanged.connect(MainWindow.bodeChanged_1)
        self.editfrecuencia_1.textChanged.connect(MainWindow.entradaChanged_1)
        self.editamplitud_1.textChanged.connect(MainWindow.entradaChanged_1)
        self.editw0_2.textChanged.connect(MainWindow.bodeChanged_2)
        self.editxi_2.textChanged.connect(MainWindow.bodeChanged_2)
        self.editganancia_2.textChanged.connect(MainWindow.bodeChanged_2)
        self.editfrecuencia_2.textChanged.connect(MainWindow.entradaChanged_2)
        self.editamplitud_2.textChanged.connect(MainWindow.entradaChanged_2)
        self.edit_r.textChanged.connect(MainWindow.bodeChanged_rlc)
        self.edit_l.textChanged.connect(MainWindow.bodeChanged_rlc)
        self.edit_c.textChanged.connect(MainWindow.bodeChanged_rlc)
        self.editfrecuencia_rlc.textChanged.connect(MainWindow.entradaChanged_rlc)
        self.editamplitud_rlc.textChanged.connect(MainWindow.entradaChanged_rlc)

        self.vbutton_1a.clicked.connect(MainWindow.vButton_1a)
        self.vbutton_2a.clicked.connect(MainWindow.vButton_2a)
        self.vbutton_3a.clicked.connect(MainWindow.vButton_3a)
        self.vbutton_4a.clicked.connect(MainWindow.vButton_4a)
        self.vbutton_1b.clicked.connect(MainWindow.vButton_1b)
        self.vbutton_2b.clicked.connect(MainWindow.vButton_2b)
        self.vbutton_3b.clicked.connect(MainWindow.vButton_3b)
        self.vbutton_4b.clicked.connect(MainWindow.vButton_4b)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labeltipofiltro_1.setText(_translate("MainWindow", "Tipo de Filtro"))
        self.labelganancia_1.setText(_translate("MainWindow", "Ganancia"))
        self.labelpolo_1.setText(_translate("MainWindow", "Polo"))
        self.labelcero_1.setText(_translate("MainWindow", "Cero"))
        self.filtertype_1.setItemText(0, _translate("MainWindow", "Arbitrario"))
        self.filtertype_1.setItemText(1, _translate("MainWindow", "Pasa Bajos"))
        self.filtertype_1.setItemText(2, _translate("MainWindow", "Pasa Altos"))
        self.filtertype_1.setItemText(3, _translate("MainWindow", "Pasa Todo"))
        self.entrytype_1.setItemText(0, _translate("MainWindow", "Senoide"))
        self.entrytype_1.setItemText(1, _translate("MainWindow", "Pulso"))
        self.entrytype_1.setItemText(2, _translate("MainWindow", "Pulso periodico"))
        self.entrytype_1.setItemText(3, _translate("MainWindow", "Diente de sierra"))
        self.labelamplitud_1.setText(_translate("MainWindow", "Amplitud"))
        self.labeltipoentrada_1.setText(_translate("MainWindow", "Tipo de Entrada"))
        self.labelfrecuencia_1.setText(_translate("MainWindow", "Frecuencia"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabprimerorden), _translate("MainWindow", "Filtros Primer Orden"))
        self.labeltipofiltro_2.setText(_translate("MainWindow", "Tipo de Filtro"))
        self.labelw0_2.setText(_translate("MainWindow", '\u03C9' + '\u2080'))
        self.labelxi_2.setText(_translate("MainWindow", '\u03BE'))
        self.labelganancia_2.setText(_translate("MainWindow", "Ganancia"))
        self.filtertype_2.setItemText(0, _translate("MainWindow", "Arbitrario"))
        self.filtertype_2.setItemText(1, _translate("MainWindow", "Pasa Bajos"))
        self.filtertype_2.setItemText(2, _translate("MainWindow", "Pasa Altos"))
        self.filtertype_2.setItemText(3, _translate("MainWindow", "Pasa Todo"))
        self.filtertype_2.setItemText(4, _translate("MainWindow", "Pasa Banda"))
        self.filtertype_2.setItemText(5, _translate("MainWindow", "Notch"))
        self.labeltipoentrada_2.setText(_translate("MainWindow", "Tipo de Entrada"))
        self.entrytype_2.setItemText(0, _translate("MainWindow", "Senoide"))
        self.entrytype_2.setItemText(1, _translate("MainWindow", "Pulso"))
        self.entrytype_2.setItemText(2, _translate("MainWindow", "Pulso periodico"))
        self.entrytype_2.setItemText(3, _translate("MainWindow", "Diente de sierra"))
        self.labelamplitud_2.setText(_translate("MainWindow", "Amplitud"))
        self.labelfrecuencia_2.setText(_translate("MainWindow", "Frecuencia"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabsegundoorden), _translate("MainWindow", "Filtros Segundo Orden"))
        self.r_label.setText(_translate("MainWindow", "R"))
        self.l_label.setText(_translate("MainWindow", "L"))
        self.c_label.setText(_translate("MainWindow", "C"))
        self.vbutton_2a.setText(_translate("MainWindow", "V2"))
        self.vbutton_3a.setText(_translate("MainWindow", "V3"))
        self.vbutton_4a.setText(_translate("MainWindow", "V4"))
        self.vbutton_1a.setText(_translate("MainWindow", "V1"))
        self.vbutton_2b.setText(_translate("MainWindow", "V2"))
        self.vbutton_3b.setText(_translate("MainWindow", "V3"))
        self.vbutton_4b.setText(_translate("MainWindow", "V4"))
        self.vbutton_1b.setText(_translate("MainWindow", "V1"))
        self.entrytype_rlc.setItemText(0, _translate("MainWindow", "Senoide"))
        self.entrytype_rlc.setItemText(1, _translate("MainWindow", "Pulso"))
        self.entrytype_rlc.setItemText(2, _translate("MainWindow", "Pulso periodico"))
        self.entrytype_rlc.setItemText(3, _translate("MainWindow", "Diente de sierra"))
        self.labelamplitud_rlc.setText(_translate("MainWindow", "Amplitud"))
        self.labeltipoentrada_rlc.setText(_translate("MainWindow", "Tipo de Entrada"))
        self.labelfrecuencia_rlc.setText(_translate("MainWindow", "Frecuencia"))
        self.editcero_1.setText(_translate("MainWindow","0.0"))
        self.editpolo_1.setText(_translate("MainWindow","0.0"))
        self.editganancia_1.setText(_translate("MainWindow","1.0"))
        self.editfrecuencia_1.setText(_translate("MainWindow","0.0"))
        self.editamplitud_1.setText(_translate("MainWindow","0.0"))

        self.editw0_2.setText(_translate("MainWindow","1.0"))
        self.editxi_2.setText(_translate("MainWindow","0.0"))
        self.editganancia_2.setText(_translate("MainWindow","1.0"))
        self.editfrecuencia_2.setText(_translate("MainWindow","0.0"))
        self.editamplitud_2.setText(_translate("MainWindow","0.0"))

        self.edit_r.setText(_translate("MainWindow","1.0"))
        self.edit_l.setText(_translate("MainWindow","1.0"))
        self.edit_c.setText(_translate("MainWindow","1.0"))
        self.editfrecuencia_rlc.setText(_translate("MainWindow","0.0"))
        self.editamplitud_rlc.setText(_translate("MainWindow","0.0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabrlc), _translate("MainWindow", "Transferencias RLC"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
