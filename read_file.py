#!/usr/bin/python
# -*- coding: utf-8 -*-


import geopandas as gp
import ogr
import numpy as np




"""
name_file = 'soja.shp'
atribute = "DryYield ("
atribute1 = 'local_moran'
dataframe = gp.GeoDataFrame.from_file(name_file)
data = dataframe
"""

def atrib(mps):
	dataSource = ogr.Open(mps)
	daLayer = dataSource.GetLayer(0)
	layerDefinition = daLayer.GetLayerDefn()
	count_item = np.arange(0,len(daLayer))
	Atributos = []
	a = np.arange(0,len(daLayer))
	for i in range(layerDefinition.GetFieldCount()):
		at = layerDefinition.GetFieldDefn(i).GetName()
		Atributos.append(at)
	atrib = []
	for i in Atributos:
		atrib.append(i)
	return atrib	
