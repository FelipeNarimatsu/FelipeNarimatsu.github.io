import csv

outputFile = open('NovoCSV.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])

outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])

outputWriter.writerow([1, 2, 3.141592, 4])
outputWriter.writerow(['ALUNO:', 'P1', 'P2', 'P3', 'Status:'])
outputWriter.writerow(['Victor Costa', 29, 35, 50, 'OverpowerBRUTO222'])

outputFile.close()