# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front_end.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(638, 476)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 130, 621, 281))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_1)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 601, 61))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.button_abrir = QtGui.QPushButton(self.groupBox_3)
        self.button_abrir.setGeometry(QtCore.QRect(520, 20, 71, 31))
        self.button_abrir.setObjectName(_fromUtf8("button_abrir"))
        self.lineEdit_abrir = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_abrir.setGeometry(QtCore.QRect(10, 20, 501, 31))
        self.lineEdit_abrir.setObjectName(_fromUtf8("lineEdit_abrir"))
        self.button_next1 = QtGui.QPushButton(self.tab_1)
        self.button_next1.setGeometry(QtCore.QRect(460, 220, 151, 31))
        self.button_next1.setObjectName(_fromUtf8("button_next1"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_1)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 601, 61))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.checkBox_knn = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_knn.setGeometry(QtCore.QRect(10, 20, 301, 17))
        self.checkBox_knn.setObjectName(_fromUtf8("checkBox_knn"))
        self.lineEdit_knn = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_knn.setGeometry(QtCore.QRect(430, 20, 21, 20))
        self.lineEdit_knn.setObjectName(_fromUtf8("lineEdit_knn"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(320, 20, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(460, 20, 46, 13))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_limite_knn = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_limite_knn.setGeometry(QtCore.QRect(500, 20, 71, 20))
        self.lineEdit_limite_knn.setObjectName(_fromUtf8("lineEdit_limite_knn"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.checkBox_yield = QtGui.QCheckBox(self.tab_2)
        self.checkBox_yield.setGeometry(QtCore.QRect(20, 10, 241, 21))
        self.checkBox_yield.setObjectName(_fromUtf8("checkBox_yield"))
        self.groupBox_14 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_14.setEnabled(False)
        self.groupBox_14.setGeometry(QtCore.QRect(10, 40, 591, 151))
        self.groupBox_14.setObjectName(_fromUtf8("groupBox_14"))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_14)
        self.comboBox_3.setGeometry(QtCore.QRect(140, 20, 221, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.label_6 = QtGui.QLabel(self.groupBox_14)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 101, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_Intervalo = QtGui.QLineEdit(self.groupBox_14)
        self.lineEdit_Intervalo.setGeometry(QtCore.QRect(420, 60, 161, 20))
        self.lineEdit_Intervalo.setObjectName(_fromUtf8("lineEdit_Intervalo"))
        self.label_4 = QtGui.QLabel(self.groupBox_14)
        self.label_4.setGeometry(QtCore.QRect(240, 60, 171, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.radioButton_yl_IIQ = QtGui.QRadioButton(self.groupBox_14)
        self.radioButton_yl_IIQ.setGeometry(QtCore.QRect(20, 60, 171, 17))
        self.radioButton_yl_IIQ.setObjectName(_fromUtf8("radioButton_yl_IIQ"))
        self.radioButton_yl_3Std = QtGui.QRadioButton(self.groupBox_14)
        self.radioButton_yl_3Std.setGeometry(QtCore.QRect(20, 90, 101, 17))
        self.radioButton_yl_3Std.setObjectName(_fromUtf8("radioButton_yl_3Std"))
        self.radioButton_yl_valor_eleccion = QtGui.QRadioButton(self.groupBox_14)
        self.radioButton_yl_valor_eleccion.setGeometry(QtCore.QRect(20, 120, 111, 17))
        self.radioButton_yl_valor_eleccion.setObjectName(_fromUtf8("radioButton_yl_valor_eleccion"))
        self.lineEdit_cantidad_desvios_estandar = QtGui.QLineEdit(self.groupBox_14)
        self.lineEdit_cantidad_desvios_estandar.setGeometry(QtCore.QRect(250, 90, 121, 20))
        self.lineEdit_cantidad_desvios_estandar.setObjectName(_fromUtf8("lineEdit_cantidad_desvios_estandar"))
        self.label_9 = QtGui.QLabel(self.groupBox_14)
        self.label_9.setGeometry(QtCore.QRect(170, 90, 81, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_14)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 120, 81, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_10 = QtGui.QLabel(self.groupBox_14)
        self.label_10.setGeometry(QtCore.QRect(170, 120, 46, 13))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox_14)
        self.label_11.setGeometry(QtCore.QRect(300, 120, 16, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_14)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 120, 101, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 190, 601, 61))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.button_back1 = QtGui.QPushButton(self.groupBox_4)
        self.button_back1.setGeometry(QtCore.QRect(10, 20, 131, 31))
        self.button_back1.setObjectName(_fromUtf8("button_back1"))
        self.button_next2 = QtGui.QPushButton(self.groupBox_4)
        self.button_next2.setGeometry(QtCore.QRect(460, 20, 131, 31))
        self.button_next2.setObjectName(_fromUtf8("button_next2"))
        self.button_back1.raise_()
        self.button_next2.raise_()
        self.groupBox_14.raise_()
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_15 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_15.setEnabled(False)
        self.groupBox_15.setGeometry(QtCore.QRect(10, 40, 591, 141))
        self.groupBox_15.setObjectName(_fromUtf8("groupBox_15"))
        self.comboBox_4 = QtGui.QComboBox(self.groupBox_15)
        self.comboBox_4.setGeometry(QtCore.QRect(160, 20, 171, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_15)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.comboBox_dato_rec = QtGui.QComboBox(self.groupBox_15)
        self.comboBox_dato_rec.setGeometry(QtCore.QRect(140, 70, 191, 22))
        self.comboBox_dato_rec.setObjectName(_fromUtf8("comboBox_dato_rec"))
        self.comboBox_dato_rec.addItem(_fromUtf8(""))
        self.comboBox_dato_rec.addItem(_fromUtf8(""))
        self.comboBox_dato_rec.addItem(_fromUtf8(""))
        self.comboBox_dato_rec.addItem(_fromUtf8(""))
        self.label_17 = QtGui.QLabel(self.groupBox_15)
        self.label_17.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.checkBox_record = QtGui.QCheckBox(self.tab_3)
        self.checkBox_record.setGeometry(QtCore.QRect(20, 10, 241, 21))
        self.checkBox_record.setObjectName(_fromUtf8("checkBox_record"))
        self.button_next3 = QtGui.QPushButton(self.tab_3)
        self.button_next3.setGeometry(QtCore.QRect(480, 210, 131, 31))
        self.button_next3.setObjectName(_fromUtf8("button_next3"))
        self.button_back2 = QtGui.QPushButton(self.tab_3)
        self.button_back2.setGeometry(QtCore.QRect(10, 210, 131, 31))
        self.button_back2.setObjectName(_fromUtf8("button_back2"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.checkBox_distancia1 = QtGui.QCheckBox(self.tab)
        self.checkBox_distancia1.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.checkBox_distancia1.setObjectName(_fromUtf8("checkBox_distancia1"))
        self.groupBox_distancia = QtGui.QGroupBox(self.tab)
        self.groupBox_distancia.setEnabled(True)
        self.groupBox_distancia.setGeometry(QtCore.QRect(20, 40, 561, 161))
        self.groupBox_distancia.setObjectName(_fromUtf8("groupBox_distancia"))
        self.label_7 = QtGui.QLabel(self.groupBox_distancia)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 141, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox_distancia = QtGui.QComboBox(self.groupBox_distancia)
        self.comboBox_distancia.setEnabled(True)
        self.comboBox_distancia.setGeometry(QtCore.QRect(120, 30, 231, 22))
        self.comboBox_distancia.setObjectName(_fromUtf8("comboBox_distancia"))
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_distancia)
        self.radioButton_4.setEnabled(True)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 70, 171, 17))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_5 = QtGui.QRadioButton(self.groupBox_distancia)
        self.radioButton_5.setEnabled(True)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 100, 101, 17))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.radioButton_6 = QtGui.QRadioButton(self.groupBox_distancia)
        self.radioButton_6.setEnabled(True)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 130, 111, 17))
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.label_13 = QtGui.QLabel(self.groupBox_distancia)
        self.label_13.setEnabled(True)
        self.label_13.setGeometry(QtCore.QRect(130, 100, 81, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_distancia)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 100, 113, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_12 = QtGui.QLabel(self.groupBox_distancia)
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QtCore.QRect(210, 70, 181, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_distancia)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 70, 113, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_14 = QtGui.QLabel(self.groupBox_distancia)
        self.label_14.setEnabled(True)
        self.label_14.setGeometry(QtCore.QRect(160, 130, 46, 13))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_lim_abajo_d = QtGui.QLineEdit(self.groupBox_distancia)
        self.lineEdit_lim_abajo_d.setEnabled(True)
        self.lineEdit_lim_abajo_d.setGeometry(QtCore.QRect(200, 130, 113, 20))
        self.lineEdit_lim_abajo_d.setFrame(True)
        self.lineEdit_lim_abajo_d.setObjectName(_fromUtf8("lineEdit_lim_abajo_d"))
        self.label_15 = QtGui.QLabel(self.groupBox_distancia)
        self.label_15.setEnabled(True)
        self.label_15.setGeometry(QtCore.QRect(320, 130, 46, 13))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.lineEdit_lim_arriba_d = QtGui.QLineEdit(self.groupBox_distancia)
        self.lineEdit_lim_arriba_d.setEnabled(True)
        self.lineEdit_lim_arriba_d.setGeometry(QtCore.QRect(330, 130, 113, 20))
        self.lineEdit_lim_arriba_d.setObjectName(_fromUtf8("lineEdit_lim_arriba_d"))
        self.button_back3_2 = QtGui.QPushButton(self.tab)
        self.button_back3_2.setGeometry(QtCore.QRect(20, 220, 131, 31))
        self.button_back3_2.setObjectName(_fromUtf8("button_back3_2"))
        self.button_next3_2 = QtGui.QPushButton(self.tab)
        self.button_next3_2.setGeometry(QtCore.QRect(470, 220, 131, 31))
        self.button_next3_2.setObjectName(_fromUtf8("button_next3_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.groupBox = QtGui.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 601, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit_guardar_2 = QtGui.QPushButton(self.groupBox)
        self.lineEdit_guardar_2.setGeometry(QtCore.QRect(520, 20, 71, 31))
        self.lineEdit_guardar_2.setObjectName(_fromUtf8("lineEdit_guardar_2"))
        self.lineEdit_guardar = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_guardar.setGeometry(QtCore.QRect(10, 20, 501, 31))
        self.lineEdit_guardar.setObjectName(_fromUtf8("lineEdit_guardar"))
        self.button_back4 = QtGui.QPushButton(self.tab_4)
        self.button_back4.setGeometry(QtCore.QRect(20, 130, 131, 31))
        self.button_back4.setObjectName(_fromUtf8("button_back4"))
        self.button_procesar = QtGui.QPushButton(self.tab_4)
        self.button_procesar.setGeometry(QtCore.QRect(470, 130, 131, 31))
        self.button_procesar.setObjectName(_fromUtf8("button_procesar"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.groupBox_5 = QtGui.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 420, 631, 51))
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 10, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 10, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.progress = QtGui.QProgressBar(self.groupBox_5)
        self.progress.setGeometry(QtCore.QRect(290, 10, 151, 23))
        self.progress.setProperty("value", 0)
        self.progress.setObjectName(_fromUtf8("progress"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 20, 261, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 50, 331, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setEnabled(True)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 641, 111))
        self.label_16.setText(_fromUtf8(""))
        self.label_16.setPixmap(QtGui.QPixmap(_fromUtf8("cabecera2.jpg")))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName(_fromUtf8("label_16"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Filter Map", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Mapa de rendimiento", None))
        self.button_abrir.setText(_translate("Dialog", "Abrir .Shp", None))
        self.button_next1.setText(_translate("Dialog", "Siguiente >", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Autocorrelacion espacial", None))
        self.checkBox_knn.setText(_translate("Dialog", "Limpieza de datos no autocorrelacionados espacialmente", None))
        self.lineEdit_knn.setText(_translate("Dialog", "8", None))
        self.label_3.setText(_translate("Dialog", "Vecinos mas cercanos:", None))
        self.label_8.setText(_translate("Dialog", "Limite: ", None))
        self.lineEdit_limite_knn.setText(_translate("Dialog", "0.01", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Dialog", "Seleccion de datos", None))
        self.checkBox_yield.setText(_translate("Dialog", "Clasificar por outliers de datos de rendimiento", None))
        self.groupBox_14.setTitle(_translate("Dialog", " Rango ", None))
        self.label_6.setText(_translate("Dialog", "Rendimiento / Yield: ", None))
        self.lineEdit_Intervalo.setText(_translate("Dialog", "1.5", None))
        self.label_4.setText(_translate("Dialog", "Valor limite del intervalo intercuantil", None))
        self.radioButton_yl_IIQ.setText(_translate("Dialog", "Intervalo intercuantil (Tukey)", None))
        self.radioButton_yl_3Std.setText(_translate("Dialog", "- X Std / X Std", None))
        self.radioButton_yl_valor_eleccion.setText(_translate("Dialog", "Valores a eleccion", None))
        self.lineEdit_cantidad_desvios_estandar.setText(_translate("Dialog", "3", None))
        self.label_9.setText(_translate("Dialog", "N° de Desvios:  ", None))
        self.label_10.setText(_translate("Dialog", "Entre: ", None))
        self.label_11.setText(_translate("Dialog", "y", None))
        self.button_back1.setText(_translate("Dialog", "<  Anterior", None))
        self.button_next2.setText(_translate("Dialog", "Siguiente >", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Rendimiento", None))
        self.groupBox_15.setTitle(_translate("Dialog", "Atributo ", None))
        self.label_5.setText(_translate("Dialog", "Atributo Record / grabacion: ", None))
        self.comboBox_dato_rec.setItemText(0, _translate("Dialog", "Activ.", None))
        self.comboBox_dato_rec.setItemText(1, _translate("Dialog", "Activado", None))
        self.comboBox_dato_rec.setItemText(2, _translate("Dialog", "On", None))
        self.comboBox_dato_rec.setItemText(3, _translate("Dialog", "Activado.", None))
        self.label_17.setText(_translate("Dialog", "Dato  deseado", None))
        self.checkBox_record.setText(_translate("Dialog", "Clasificar por outliers de datos de grabacion", None))
        self.button_next3.setText(_translate("Dialog", "Siguiente >", None))
        self.button_back2.setText(_translate("Dialog", "<  Anterior", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Record", None))
        self.checkBox_distancia1.setText(_translate("Dialog", "Clasificar por outliers de datos de distancia minima entre puntos", None))
        self.groupBox_distancia.setTitle(_translate("Dialog", "Atributo", None))
        self.label_7.setText(_translate("Dialog", "Atributo distancia", None))
        self.radioButton_4.setText(_translate("Dialog", "Intervalo intercuantil (Tukey)", None))
        self.radioButton_5.setText(_translate("Dialog", "- X Std / X Std", None))
        self.radioButton_6.setText(_translate("Dialog", "Valores a eleccion", None))
        self.label_13.setText(_translate("Dialog", "N° de Desvios:  ", None))
        self.lineEdit_5.setText(_translate("Dialog", "3", None))
        self.label_12.setText(_translate("Dialog", "Valor limite del intervalo intercuantil", None))
        self.lineEdit_4.setText(_translate("Dialog", "1.5", None))
        self.label_14.setText(_translate("Dialog", "Entre: ", None))
        self.lineEdit_lim_abajo_d.setText(_translate("Dialog", "5", None))
        self.label_15.setText(_translate("Dialog", "y", None))
        self.lineEdit_lim_arriba_d.setText(_translate("Dialog", "20", None))
        self.button_back3_2.setText(_translate("Dialog", "< Anterior", None))
        self.button_next3_2.setText(_translate("Dialog", "Siguiente >", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Distancia", None))
        self.groupBox.setTitle(_translate("Dialog", "Mapa de rendimiento", None))
        self.lineEdit_guardar_2.setText(_translate("Dialog", "Guardar .shp", None))
        self.button_back4.setText(_translate("Dialog", "<  Anterior", None))
        self.button_procesar.setText(_translate("Dialog", "Procesar informacion", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Guardar", None))
        self.pushButton_4.setText(_translate("Dialog", "Salir", None))
        self.pushButton_2.setText(_translate("Dialog", "Visualizar mapa de rendimiento", None))
        self.pushButton_3.setText(_translate("Dialog", "Limpiar todo ", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Cleaner Map Yield</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "Plugin para poder eliminar datos atipicos en mapas de rendimientos", None))

