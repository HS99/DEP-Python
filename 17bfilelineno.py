# define the main function
def main():
    # prompt the user to enter the numbers
    n = int(input("Please enter the number of lines to be entered in a file: "))
    # create a new text file
    outfile = open("linenos.txt", "w")
    # write numbers in the text file
    for i in range(n):
        line=input("Enter the line ")
        outfile.write(line)
        outfile.write('\n')
    outfile.close()
    infile = open("linenos.txt", "r")
    for i in range(n):
        line = infile.readline()
        print(i+1,': ',line,end='')
    # close the file
    infile.close()
# call the main function
main()