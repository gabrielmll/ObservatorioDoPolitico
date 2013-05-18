import urllib
import json
from StringIO import StringIO
from getData import getData

info = []
info = getData('http://dadosabertos.almg.gov.br/ws/comissoes/lista?formato=json')["list"]

for comissao in info:
	print comissao["nome"].encode("utf-8")
