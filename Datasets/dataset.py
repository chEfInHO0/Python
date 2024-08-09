import pandas as pd 

lista_veiculos = ['carro','moto','caminhao']

serie_veiculo = pd.Series(lista_veiculos)

# Criamos uma series com o pandas e deixamos o index ser preenchido automaticamente, mas podemos altera-lo definindo o atributo index ao chamar a funcao
# 
print(serie_veiculo)




lista = [1,2,3,4]

dicionario = {'a':5,'b':6,'c':7,'d':8}
