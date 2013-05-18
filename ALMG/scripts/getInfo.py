import urllib
import json
from StringIO import StringIO
from getData import getData
from out import output

def infoDeputado(status):
	cont = 0
	if status == 1:
		listaDeputado = []
		listaDeputado = getData('http://dadosabertos.almg.gov.br/ws/deputados/situacao/1?formato=json')["list"]

		lista = []
		dicio = {"lista":lista}

		for deputado in listaDeputado:
			print deputado["nome"], "-", deputado["partido"]
#			saida = deputado["nome"]+" - "+deputado["partido"]
#			output("saida.out", saida.encode('utf-8'))
#			lista.append(regDeputado(deputado["id"])

			saida = "{\n\t\"nome\": \""+deputado["nome"]+"\",\n\t\"partido\": \""+deputado["partido"]+"\",\n\t\"redesSociais\": ["
			output("teste.out", saida.encode('utf-8'))
			regDeputado(deputado["id"])

			saida = "\t],\n},\n"
			output("teste.out", saida.encode('utf-8'))
#			verbaDeputado(deputado["id"])

	print dicio["lista"]

def regDeputado(numId):
	url = 'http://dadosabertos.almg.gov.br/ws/deputados/'+str(numId)+'?formato=json'
	registroDeputado = []
	registroDeputado = getData(url)["deputado"]


	#print	"\n\tRedes Sociais\n"
#	output("saida.out", "\n\tRedes Sociais\n")

#	dicio = {}

	for redeSoc in registroDeputado["redesSociais"]:
		print "\t\t", redeSoc["redeSocial"]["nome"], "-", redeSoc["url"]
#		dicio.update({redeSoc["redeSocial"]["nome"]:redeSoc["url"]})
#		saida = "\t\t"+redeSoc["redeSocial"]["nome"]+" - "+redeSoc["url"]+"\n"
#		output("saida.out", saida.encode('utf-8'))
	
		saida = "\t\t{\n\t\t\"redeSocial\": {\n\t\t\t\"nome\": \""+redeSoc["redeSocial"]["nome"]+"\",\n\t\t\t\"url\": \""+redeSoc["url"]+"\",\n\t\t},\n\t}"
		output("teste.out", saida.encode('utf-8'))

#	return dicio
	#print "-----//-----\n\n"
#	output("saida.out", "\n-----//-----\n\n")

def verbaDeputado(numId):
	url = 'http://dadosabertos.almg.gov.br/ws/prestacao_contas/verbas_indenizatorias/legislatura_atual/deputados/'+str(numId)+'/datas?formato=json'

	deputado = []
	deputado = getData(url)["list"]

	for dataVerba in deputado:
		ano = dataVerba["dataReferencia"]["$"][0]+dataVerba["dataReferencia"]["$"][1]+dataVerba["dataReferencia"]["$"][2]+dataVerba["dataReferencia"]["$"][3]
		mes = dataVerba["dataReferencia"]["$"][5]+dataVerba["dataReferencia"]["$"][6]
		
		if mes[0] == "0":
			mes = mes[1]

		url2 = 'http://dadosabertos.almg.gov.br/ws/prestacao_contas/verbas_indenizatorias/deputados/'+str(numId)+'/'+str(ano)+'/'+str(mes)+'?formato=json'
		print url2
'''		valores = getData(url2)["list"]

		for verba in valores:
			print verba.keys()
'''


