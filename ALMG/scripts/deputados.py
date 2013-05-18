#!/usr/bin/python
# coding: utf-8

# Este script captura os deputados em exercício da ALMG
# link: http://dadosabertos.almg.gov.br/ws/deputados/ajuda#Lista de Deputados em Exercício
#
# O que retornar

import urllib
import json
from StringIO import StringIO
from getData import getData

#***********************************************************************************************#
# Inicia filtrando apenas os deputados em exercício.
# Isto é, do array info[] apenas importa o IDentificador de cada deputado em exercício 
info = []
info = getData('http://dadosabertos.almg.gov.br/ws/deputados/em_exercicio?formato=json')["list"]


#***********************************************************************************************#
# Tendo o IDentificador de deputados em exercício, as próximas linhas criam um array com a url
# APENAS dos deputados com o ID em questão (que estão em exercício).
# Também estou coletando PARTIDO e NOME dessa lista.

#url = []
filiacoes = []

for data in info:
#	url.append("http://dadosabertos.almg.gov.br/ws/deputados/" + str(data["id"]) + "?formato=json")
	j = {}
	j['name'] = str(data['partido'])
#	del data['partido']
	filiados = []	

	for k in info:
		if str(k['partido']) == j['name']:
			dic2 = {}
			dic2['name'] = k['nome'].encode('latin-1')
			filiados.append(dic2)

	j['children'] = filiados
	if not j in filiacoes:
		filiacoes.append(j)
 
print filiacoes
	
#***********************************************************************************************#
# Tendo o endereço de cada deputado em exercício, as próximas linhas consultam a página da ALMG 
# para capturar informação sobre deputados filtrando apenas as informações relevantes
# INFORMAÇÕES RELEVANTES: por horá é [nome] e [partido] 
	
	
	