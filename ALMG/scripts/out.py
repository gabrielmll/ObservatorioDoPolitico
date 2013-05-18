def output(urlOut, data):
	out = open(urlOut, "a")
	out.write(data)
	out.close()
