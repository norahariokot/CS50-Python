# Programme to determine the type of file entered by user
file_name = input("File name: ")

if "." in file_name:
    filename_extension = file_name.rsplit('.')[1].lower().strip()
    #print(filename_extension)
    if filename_extension == "jpg":
        filename_extension = "jpeg"
else:
    filename_extension = ""    

if filename_extension == "gif" or filename_extension == "jpg" or filename_extension == "jpeg" or filename_extension == "png":
    file_type = "image" + "/" + filename_extension
elif filename_extension == "pdf" or filename_extension == "zip":
    file_type = "application" + "/" + filename_extension
elif filename_extension =="txt" :
    file_type = "text/plain"
else:
    file_type = "application/octet-stream"  

print(file_type)    