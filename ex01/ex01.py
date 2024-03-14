
soma = 0
nome_arquivo = "numerosMilhao.txt"

with open(nome_arquivo, "r") as arquivo: 

    for linha in arquivo:
        valor = int(linha.strip())
        soma += valor

print(f"O valor da soma dos numeros e: {soma}") 


#-19
#-36
#55


