matOne = []
print("Enter 4 Elements for First Matrix: ")
for i in range(2):
    matOne.append([])
    for j in range(2):
        num = int(input())
        matOne[i].append(num)

matTwo = []
print("Enter 4 Elements for Second Matrix: ")
for i in range(2):
    matTwo.append([])
    for j in range(2):
        num = int(input())
        matTwo[i].append(num)

matThree = []
for i in range(2):
    matThree.append([])
    for j in range(2):
        sum = 0
        for k in range(2):
            sum = sum + (matOne[i][k] * matTwo[k][j])
        matThree[i].append(sum)

print("\nMultiplication Result of Two Given Matrix is:")
for i in range(2):
    for j in range(2):
        print(matThree[i][j], end=" ")
    print()