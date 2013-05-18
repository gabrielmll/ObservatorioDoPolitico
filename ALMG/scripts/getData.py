#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import json
import csv
from StringIO import StringIO


# Capturar formato json retornando em um dicionario

def getData(url):
	load = json.loads(urllib.urlopen(url).read())
	dump = json.dumps(load)
	io = StringIO(dump)
	information = json.load(io)
	return information

def getDataCSV():
	filePath = './Entrada/prestacao_contas_2010/candidato/MG/DespesasCandidatos.txt'
	fileData = open(filePath, 'rb')

	data = csv.DictReader(fileData, delimiter=';')

	return data
'''	for row in data:
		print row['Nome candidato']
'''
