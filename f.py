firstLine = input()
a = firstLine.replace(" ","")
lines = int(a[0])
returnLines = int(a[2])
lineLength = int(a[1])
proteins = []
returnProteins = []
priority = [0,1,2,3,4,5,6,7,8,9]
average = 0
currentProtein = []

for i in range(lines):
    protein = input()
    protein = protein.split(" ")
    proteins.append([protein[0], int(protein[1])])
    # proteins.append(input())


for i in range(returnLines):
    for protein in proteins:
        proteinName = protein[0]
        proteinNum = protein[1]
        if currentProtein == []:
            currentProtein = protein
        elif abs(average - currentProtein[1]) < abs(average - proteinNum):
            currentProtein = protein
        else:
            pass

    # Update the average
    leng = len(returnProteins)
    average = average * leng
    average += currentProtein[1]
    average = average / (leng + 1)

    returnProteins.append(currentProtein)
    proteins.remove(currentProtein)
    currentProtein = []

for protein in returnProteins:
    print(protein[0])
