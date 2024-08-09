from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from os import path, chdir, remove


def setPath():
    currDir = path.abspath(__file__).split('\\')
    currDir.pop()
    currDir = '\\'.join(currDir)
    chdir(currDir)


def prepareData(file: str):
    setPath()
    ids = []
    with open(file, 'r') as arq:
        dataSet = arq.readlines()
        for data in dataSet:
            ids.append(data.replace('\n', ''))
    return ids


def start(ids: list, debug: bool = False):
    data = ''
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    if debug:
        driver.get('C:\\Users\\Luccas\\Desktop\\Code\\Particular\\Tore\\Alessandra.html')
        dados = driver.find_elements(By.CLASS_NAME, 'break-word')
        for dado in dados:
            data += dado.text+'&@!&'
        data += '\n\n'
    else:
        driver.get('https://app.lojaintegrada.com.br/painel/login')
        driver.execute_script("alert('Quando o login for efetuado, volte ao prompt e pressione Enter')")
        input('Após o LOGIN, pressione ENTER\n')
        print('ENTER pressionado, continuando a execução do script \n\n\n')
        for id in ids:
            print(id)
            driver.get(f'https://app.lojaintegrada.com.br/painel/cliente/{id}/detalhar')
            dados = driver.find_elements(By.CLASS_NAME, 'break-word')
            for dado in dados:
                data += dado.text+'&@!&'
            data += '\n\n'
    driver.quit()
    return data


def main():
    file_content = ''
    file_name = ''
    busca = int(input("Buscar clientes de Harion[0] / Tore[1] "))
    while busca not in [0, 1, 2]:
        busca = int(input("Buscar clientes de Harion[0] / Tore[1] "))
        print(busca)
    if busca == 0:
        harion = prepareData('id_clientes_harion.txt')
        file_content = start(harion)
        file_name = 'harion_complete_data.txt'
    elif busca == 1:
        tore = prepareData('id_clientes_tore.txt')
        file_content = start(tore)
        file_name = 'tore_complete_data.txt'
    else:
        teste = prepareData('teste.txt')
        file_content = start(teste, True)
        file_name = 'tore_TESTE_data.txt'

    try:
        file = open(file_name, 'r', encoding='utf-8')
        print(file.read())
        file.close()
        remove(file_name)
        print('Arquivo encontrado, e reescrito')
        with open(file_name, 'x', encoding='utf-8') as f:
            f.write(file_content)
    except FileNotFoundError:
        with open(file_name, 'x', encoding='utf-8') as f:
            f.write(file_content)


main()
