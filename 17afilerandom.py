# import the required modules
import random
# define the main function
def main():
    # prompt the user to enter the numbers
    n = int(input("Please enter the number of random numbers to be hold in a file: "))
    # create a new text file
    outfile = open("randomNumbers.txt", "w")
    # write numbers in the text file
    for i in range(n):
        outfile.write(str(random.randint(1, 500)))
        outfile.write(' ')
    outfile.close()
    infile = open("randomNumbers.txt", "r")
    for i in range(n):
        ran = infile.read()
        print(ran,end=' ')
    # close the file
    infile.close()
# call the main function
main()