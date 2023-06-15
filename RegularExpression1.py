import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))
#######################
import re

Nameage = '''
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21
'''
ages = re.findall(r'\d[0-9]', Nameage)
names = re.findall(r'[A-Z][a-z]*', Nameage)
print(ages)
print(names)
ageDict = {}
x = 0
for eachname in names:
    ageDict[eachname] = ages[x]
    x += 1
print(ageDict)