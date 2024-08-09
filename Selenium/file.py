import pathlib

FILE_NAME_T = 'tore_complete_data.txt'               #       
FILE_NAME_FILTERED_T = 'tore_data_filtered.txt'      #   NÃO ALTERAR       
FILE_NAME_H = 'hariom_complete_data.txt'             #   AS CONSTANTES 
FILE_NAME_FILTERED_H = 'hariom_data_filtered.txt'    #           

def _(x):
    print(x)


def filter_lvl_1(flag:int = 0):
    if flag == 0:
        file = FILE_NAME_T
    else:
        file = FILE_NAME_H
    with open(file, 'r', encoding='utf-8') as file:
        newDataSet = []
        dataSet = file.read().split('\n\n')
        for data in dataSet:
            cadInfo = data.split('&@!&')
            cleanData = []
            nome = cadInfo[0]
            email = cadInfo[1]
            del cadInfo[1]
            del cadInfo[0]
            time_to_birthday = ''
            pedidos = ''
            sexo = ''
            tel = ''
            politica = ''
            cpf = ''
            nasc = ''
            for info in cadInfo:
                if info.startswith('('):
                    tel += info+' '
                elif info.startswith('#') or info.startswith('R$'):
                    pedidos += info+' '
                elif info.startswith('-') or info.startswith('Masculino') or info.startswith('Feminino'):
                    sexo = info
                elif info.startswith('Não aceitou nova política') or info.startswith('Aceito'):
                    politica = info
                elif len(info.split('.')) == 3:
                    cpf = info
                elif len(info.split('/')) == 3 and cadInfo.index(info) == 4:
                    nasc += info+' '
                elif ('mês' in info) or ('meses' in info):
                    time_to_birthday = info
                else:
                    if (info != '') and (info not in cleanData):
                        cleanData.append(info)
            cadDate = cleanData.pop()
            endereco = ' '.join(cleanData)
            cliente = [nome, email, cpf, cadDate ,sexo, tel,
                       nasc, politica, pedidos, endereco]
            newDataSet.append(cliente)
    return newDataSet


def main(flag:int=0):
    if flag == 0:
        file = FILE_NAME_FILTERED_T
    else:
        file = FILE_NAME_FILTERED_H
    dados = filter_lvl_1(flag)
    dadosSTR = ''
    for dado in dados:
        dadosSTR += ';'.join(dado)
        dadosSTR += '\n'
    try:
        f = open(file, 'r', encoding='utf-8')
        f.read()
        f.close()
    except FileNotFoundError:
        pass
    except FileExistsError:
        pathlib.Path.unlink(file)
    finally:
        f = open(file, 'w+', encoding='utf-8')
        f.write(dadosSTR)
        f.close()


main(1)  # Colocar o 1 dentro dos () de main, atualiza a lista do Hariom, deixar vazio ou colocar o 0 atualiza a do Toré