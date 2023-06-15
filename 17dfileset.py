file1 = open("fileset1.txt", "w")
# write in the text file
text1 = "This is a text file containing words which will be analyzed using sets"
file1.write(text1)
file1.close()
file2 = open("fileset2.txt", "w")
# write in the text file
text2 = "This is a text file containing words that will be analyzed using sets"
file2.write(text2)
file2.close()
file3 = open("fileset3.txt", "w")
# write in the text file
text3 = "This is a text file containing words that will be analyzed using sets"
file3.write(text2)
file3.close()

set1 =  set(open('fileset1.txt').read().split())
set2 =  set(open('fileset2.txt').read().split())
set3 =  set(open('fileset3.txt').read().split())

if set1 == set2:
    print("Contents of File1 and File2 are same")
elif set1 == set3:
    print("Contents of File1 and File3 are same")
elif set2 == set3:
    print("Contents of File2 and File3 are same")
