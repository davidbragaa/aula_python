import csv

with open ("files/exemplo_vendas.csv", "r") as csvfiles:

    #criando um leitor de CSV
    reader = csv.reader(csvfiles, delimiter=",")

    #Ignorando a primeira linha (cabeçalho)

    for row in reader:
        #Imprimindo cada linha

        print(row)