with open('index.html','r') as webpage:
	with open('output.txt','a') as wf:
		for line in wf.readlines():
			if '<a href = ' in line:
				pos = line.find('<a href=')
				first_quote = line.find('\"',)
				second_qoute = line.find('\"',first_quote+1)
				url = line[first_quote+1:second_qoute]
				wf.write(url+ '\n')

  