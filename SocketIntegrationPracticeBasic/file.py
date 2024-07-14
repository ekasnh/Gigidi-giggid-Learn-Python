#f = open('file1.txt')
#print(f'cursor position - {f.tell()}')
#f.seek(0)
#print(f.read())
#print(f.readline(), end ='')
#f.close()

#with block 
#context manager 

#with open('file1.txt')as f:
#	data = f.read()
#	print(data)

#print(f.closed)

with open('D:\PythonProjects\salary.txt','r') as rf:
	with open('output.txt','a') as wf:
		for line in rf.readlines():
			name,salary = line.split(',')
			wf.write(f'{name}\'s salary is {salary}')
