# Take input from user
upto = int(input("Find prime numbers upto : "))
print("\nAll prime numbers upto", upto, "are : ")
for num in range(2, upto + 1):
    i = 2
    for i in range(2, num):
        if(num % i == 0):
            i = num
            break;
    # If the number is prime then print it.
    if(i != num):
        print(num, end=" ")