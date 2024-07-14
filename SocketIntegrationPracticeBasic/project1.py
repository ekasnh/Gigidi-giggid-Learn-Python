import os,shutil 
dictextensions = {
	'audio' : ('.mp3','.wav'),
	'video' : ('.mp4','.mpeg'),
	'documents' : ('.doc','.docx','.pdf','.txt'),
	'images' : ('.png','.jpeg'),
}

folderpath = input('wnter path ')
def file_finder(folderpath,file_extensions):
	#files = []
	#for file in os.listdir(folderpath):
	#	for extension in file_extensions:
	#		if file.endswith(extension):
	#			files.append(file)

	#return files
	return (file for file in os.listdir(folderpath) for extension in file_extensions if file.endswith(extension))


#print(file_finder(folderpath,video))
for extension_type,extension_tuple in dictextensions.items():
	folder_name = extension_type.split(',')[0] + 'files'
	folder_path = os.path.join(folderpath,folder_name)
	os.mkdir(folderpath)
	for item in file_finder(folderpath,extension_tuple):
		item_path = os.path.join(folderpath,item)
		item_new_path = os.path.join(folderpath,item)
		shutil.move(item_path,item_new_path)
		

		#print('calling file finder ')
	#print(file_finder(folderpath,extension_tuple))