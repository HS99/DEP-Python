outfile = open("unique.txt", "w")
# write in the text file
text = "This is a text file containing words. Few words are repeated while few others are unique"
outfile.write(text)
outfile.close()
text_file = open('unique.txt', 'r')
text = text_file.read()
#cleaning
text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]
#finding unique
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
#sort
unique.sort()
#print
print(unique)