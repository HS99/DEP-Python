# Creating an HTML file
Func = open("hypertext.html", "w")
# Adding input data to the HTML file
Func.write("<html>\n<head>\n<title> \nOutput Data in an HTML file \
		</title>\n</head> <body><h1>Welcome to <u>Nizam College</u></h1>\
		\n<h2>MCA <u>Sem II</u> Department of Informatics</h2> \n</body></html>")
# Saving the data into the HTML file
Func.close()
Func = open("hypertext.html", "r")
# Adding input data to the HTML file
str = Func.read()
print("Read from HTML file - ", str)
# Saving the data into the HTML file
Func.close()