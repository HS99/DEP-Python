import sys
a, b = sys.argv[1:3]
print("sum is", float(a) + float(b))
#Omitting upper range
import sys
a, b = sys.argv[1:]
print("sum is", float(a) + float(b))
#Using sum fumction
import sys
summ = sum(float(i) for i in sys.argv[1:])
print("sum is", summ)
