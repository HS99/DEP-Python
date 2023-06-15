# Python3 code to count vowel in a string using set
# Function to count vowel
def vowel_count(str):
    # Initializing count variable to 0
    count = 0
    consonents = 0
    #misc = 0
    # Creating a set of vowels
    vowel = set("aeiouAEIOU")
    consonentslist = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    # Loop to traverse the alphabet
    # in the given string
    for alphabet in str:
        # If alphabet is present
        # in set vowel
        if alphabet in vowel:
            count = count + 1
        elif alphabet in consonentslist:
            consonents = consonents + 1
        #else:
        #    misc = misc + 1
    print("No. of vowels :", count)
    print("No. of consonents :", consonents)
    #print("No. of other symbols :", misc)
# Driver code
str = "Nizam College"
# Function Call
vowel_count(str)
