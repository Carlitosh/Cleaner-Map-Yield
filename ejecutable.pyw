#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, uic
import pysal
import matplotlib.pyplot as plt
import numpy as np
from read_file import atrib
import pandas as pd
import geopandas as gp
from front_end import Ui_Dialog

#from save_file import save_shp

# Cargar nuestro archivo .ui
#form_class = uic.loadUiType("front_end.ui")[0]

form_class = Ui_Dialog
class cleaner_map_yield(QtGui.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		
		#===============================================================
		self.groupBox_distancia.setEnabled(False)
		self.button_next1.clicked.connect(self.next1)
		self.button_next2.clicked.connect(self.next2)
		self.button_next3.clicked.connect(self.next3)
		self.button_next3_2.clicked.connect(self.next4)
		self.pushButton_4.clicked.connect(self.salir)
		
		self.button_back1.clicked.connect(self.back1)
		self.button_back2.clicked.connect(self.back2)
		self.button_back3_2.clicked.connect(self.back3)
		self.button_back4.clicked.connect(self.back4)
		self.button_abrir.clicked.connect(self.abrir)
		self.button_procesar.clicked.connect(self.procesar)
		
		self.pushButton_3.clicked.connect(self.limpiar)
		self.lineEdit_guardar_2.clicked.connect(self.guardar)
		self.checkBox_yield.stateChanged.connect(self.check_rendimiento)
		self.checkBox_record.stateChanged.connect(self.check_record)
		self.checkBox_distancia1.stateChanged.connect(self.check_distancia)
		self.progress.setValue(0)
		#===============================================================
		
		
		#===============================================================
		#Funciones del software=========================================
		
	def abrir(self):
		self.comboBox_3.clear()
		self.comboBox_4.clear()
		self.comboBox_distancia.clear()

		
		mapa = QtGui.QFileDialog.getOpenFileName(self, 'Abrir Capa vectorial', 
		'','(*.shp)')
		self.lineEdit_abrir.setText(str(mapa))
		


		
	#=========================Botones siguiente ========================
	def next1(self):
		self.tabWidget.setCurrentIndex(1)
	
	def next2(self):
		self.tabWidget.setCurrentIndex(2)
	
	def next3(self):
		self.tabWidget.setCurrentIndex(3)
		
	def next4(self):
		self.tabWidget.setCurrentIndex(4)	
			
	
	def back1(self):
		self.tabWidget.setCurrentIndex(0)
		
	def back2(self):
		self.tabWidget.setCurrentIndex(1)
	
	def back3(self):
		self.tabWidget.setCurrentIndex(2)
	
	def back4(self):
		self.tabWidget.setCurrentIndex(3)					
	
	#===============================================================
	def guardar(self):
		direc = QtGui.QFileDialog.getSaveFileName(self, 'Guardar Mapa limpio',
		 'Archivos/', selectedFilter='*.shp')
		self.lineEdit_guardar.setText(str(direc))
		
	
	#===============================================================
	def procesar(self):		
		self.progress.setValue(5)
		mps = str(self.lineEdit_abrir.text())
		interv_int =float(self.lineEdit_Intervalo.text())
		interv_int2 =float(self.lineEdit_4.text())
		
		knn = int(self.lineEdit_knn.text())
		w = pysal.knnW_from_shapefile(mps, k=knn)
		mps_dbf = mps.rstrip(".shp")
		mps_dbf = mps_dbf+".dbf"
		
		yields = str(self.comboBox_3.currentText())
		
		limite_knn =float(self.lineEdit_limite_knn.text())
		
		
		#remplazar el shp. por el dbf
		f = pysal.open(mps_dbf)
		y = np.array(f.by_col[yields])
		self.progress.setValue(10)
		records = str(self.comboBox_4.currentText())
		distancia = str(self.comboBox_distancia.currentText())
		
		name_file = mps
		atribute = yields
		atribute1 = 'local_moran'
		dataframe = gp.GeoDataFrame.from_file(name_file)
		data = dataframe
		
		
		if self.checkBox_knn.isChecked():
			knn = int(self.lineEdit_knn.text())
			w = pysal.knnW_from_shapefile(mps, k=knn)
			lm = pysal.Moran_Local(y,w)
			local_moran = lm.Is
			array = np.asarray(local_moran)
			data['local_moran'] = array.tolist()
			data =  data[(data["local_moran"] < (-1*limite_knn)) | (data["local_moran"] > limite_knn)]
		else:
			pass
			
		self.progress.setValue(20)	
		
		if 	self.checkBox_yield.isChecked():
			
			if self.radioButton_yl_IIQ.isChecked():
				xmin = np.percentile(y, 0)
				q1 = np.percentile(y, 25)
				q2 = np.percentile(y, 50)
				q3 = np.percentile(y, 75)
				xmax = np.percentile(y, 100)
				intervalo_intercuartil = q3-q1
				limite_abajo = q1-(intervalo_intercuartil*interv_int)
				limite_arriba = q3+(intervalo_intercuartil*interv_int)
				data =  data[(data[yields] < limite_arriba) & (data[yields] > limite_abajo)]
			else:
				pass
			
			if self.radioButton_yl_3Std.isChecked():
				cantidad_desvios_estandar = int(self.lineEdit_cantidad_desvios_estandar.text())
				mean = np.mean(y)
				std =	np.std(y)
				limite_abajo = mean - (std*cantidad_desvios_estandar)
				limite_arriba = mean + (std*cantidad_desvios_estandar)
				data =  data[(data[yields] < limite_arriba) & (data[yields] > limite_abajo)]	
			else:
				pass	
			if self.radioButton_yl_valor_eleccion.isChecked():
				limite_abajo = float(self.lineEdit_2.text())
				limite_arriba = float(self.lineEdit_3.text())
				data =  data[(data[yields] < limite_arriba) & (data[yields] > limite_abajo)]
			else:
				pass					
		else:
			pass
		
		self.progress.setValue(50)	
		
		if 	self.checkBox_record.isChecked():
			grabaciones = str(self.comboBox_dato_rec.currentText())
			data =  data[(data[records] == grabaciones)]
		else:
			pass
				
		if 	self.checkBox_distancia1.isChecked():
			if self.radioButton_4.isChecked():
				d = np.array(f.by_col[distancia])
				xmin_2 = np.percentile(d, 0)
				q1_2 = np.percentile(d, 25)
				q2_2 = np.percentile(d, 50)
				q3_2 = np.percentile(d, 75)
				xmax_2 = np.percentile(d, 100)
				intervalo_intercuartil_2 = q3_2-q1_2
				limite_abajo2 = q1_2-(intervalo_intercuartil_2*interv_int2)
				limite_arriba2 = q3_2+(intervalo_intercuartil*interv_int2)
				
				data =  data[(data[distancia] < limite_arriba2) & (data[distancia] > limite_abajo2)]

			else:
				pass	
			if self.radioButton_5.isChecked():
				cantidad_desvios_estandar2 = int(self.lineEdit_5.text())
				d = np.array(f.by_col[distancia])
				mean3 = np.mean(d)
				std3 =	np.std(d)
				limite_abajo3 = mean3 - (std3*cantidad_desvios_estandar2)
				limite_arriba3 = mean3 + (std3*cantidad_desvios_estandar2)
				data =  data[(data[distancia] < limite_arriba3) & (data[distancia] > limite_abajo3)]	
				
				
			else:
				pass
			if self.radioButton_6.isChecked():
				limite_abajo4 = int(self.lineEdit_lim_abajo_d.text())
				limite_arriba4 = int(self.lineEdit_lim_arriba_d.text())
				data =  data[(data[distancia] < limite_arriba4) & (data[distancia] > limite_abajo4)]
				
			else:
				pass			
		else:
			pass
		self.progress.setValue(70)
		name = str(self.lineEdit_guardar.text())
		data.to_file(name, driver='ESRI Shapefile')				 
		self.progress.setValue(100)	
	#===============================================================
	
	def check_rendimiento(self):
		if self.checkBox_yield.isChecked():
			self.groupBox_14.setEnabled(True)
			mps = str(self.lineEdit_abrir.text())
			mapa1 = str(mps)
			atributo = atrib(mapa1)
			self.comboBox_3.addItems(atributo)	
		else:
			self.groupBox_14.setEnabled(False)
	#===============================================================
	def check_record(self):
		if self.checkBox_record.isChecked():
			self.groupBox_15.setEnabled(True)
			mps = str(self.lineEdit_abrir.text())
			mapa1 = str(mps)
			atributo = atrib(mapa1)
			self.comboBox_4.addItems(atributo)			
		else:
			self.groupBox_15.setEnabled(False)
	
	
	
	def check_distancia(self):
		if self.checkBox_distancia1.isChecked():
			self.groupBox_distancia.setEnabled(True)
			mps = str(self.lineEdit_abrir.text())
			mapa1 = str(mps)
			atributo = atrib(mapa1)
			self.comboBox_distancia.addItems(atributo)
		else:
			self.groupBox_distancia.setEnabled(False)		
			
	def limpiar(self):
		self.comboBox_3.clear()
		self.comboBox_4.clear()
		self.comboBox_distancia.clear()
		
		
		self.checkBox_distancia1.setChecked(False)
		self.checkBox_record.setChecked(False)
		self.checkBox_yield.setChecked(False)
		self.tabWidget.setCurrentIndex(0)
		self.lineEdit_abrir.setText(str(""))
		self.lineEdit_guardar.setText(str(""))
	
	def salir(self):
		exit()	
		
	#===============================================================		


app = QtGui.QApplication(sys.argv)
ejemplo = cleaner_map_yield(None)
ejemplo.show()
app.exec_()			
	



