#call the main function
def main():
    #declares local variables
    number = 5
    number_list = [8,9,2,1,4,5,6,7,10,3]
    #displays the number
    print('Number ', number)
    #displays the list of numbers
    print('List of numbers: ', number_list, sep='')
    #Display the list of numbers that are larger
    #than the number
    print('List of numbers that are larger than ',number)
    #Call the larger_than_n_list function,
    #passing a number and number list as arguments.
    display_larger_than_n_list(number, number_list)
# The display_largger_than_n_list function acceps two arguments:
#a list, and a number. The function displays all of the numbers
#in the list that are greater than that number.
def display_larger_than_n_list(n, n_list):
    #Declare an empty list
    larger_than_n_list = []
    #Loop through the values in the list.
    for valie in n_list:
        #Determins if a value is greatter than n.
        #if so, append the value to the list
        if valie > n:
            larger_than_n_list.append(valie)
    #Display the list.
    print("larger_than_n_list",larger_than_n_list)
#Call the main function
main()