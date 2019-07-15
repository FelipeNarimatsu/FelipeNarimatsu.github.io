import csv
exampleFile = open('TrabalhoFinal.csv') 
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData


print(exampleData[0][0])
print(exampleData[1][0])


exampleFile = open('TrabalhoFinal.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

outputFile = open('TrabalhoFinal.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])

outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])

outputWriter.writerow([1, 2, 3.141592, 4])

outputFile.close()