import urllib
import json
from StringIO import StringIO
from getData import getData

info = []
info = getData('http://dadosabertos.almg.gov.br/ws/proposicoes/pesquisa/direcionada?tipo=PL&sitTrami=0&formato=json')["resultado"]

for data in info["listaItem"]:
	print "-------------------------------------------"
	print "Nome: ", data["proposicao"].encode("utf-8")
	print "Autor: ", data["autor"].encode("utf-8")
	
	print ""
	
	if "assuntoGeral" in data:
		print "Assunto Geral: ", data["assuntoGeral"].encode("uff-8")
	else:
		print "Assunto Geral: null"

	print ""

	if "indexacao" in data:
		print "Indexacao: ", data["indexacao"].encode("uff-8")
	else:
		print "Indexacao: null"

	print "-------------------------------------------"
