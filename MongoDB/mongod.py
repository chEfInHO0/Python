from os import environ, path, chdir
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv


def setPath():
    # Altera o path do compilador para evitar erros como [File Not Found] e/ou [File Not Exists]
    currDir = path.abspath(__file__).split('\\')
    currDir.pop()
    currDir = '\\'.join(currDir)
    chdir(currDir)


def answers():
    # Carrega o arquivo csv e armazena as respostas em um dicionario
    setPath()
    user = 1
    dataFile = {}
    with open('arquivo.csv', 'r') as file:
        data = file.read().split('\n')
        del data[0]
        for d in data:
            answers = d.split(',')
            userRes = []
            for awnser in answers[2:]:
                if awnser == '"NÃ£o vi"':
                    userRes.append(0)
                else:
                    userRes.append(
                        int(awnser.encode('ISO-8859-1').decode('utf-8').replace('"', '')))
            dataFile[user] = userRes
            user += 1
    return dataFile


load_dotenv()  # Carregando os dados de acesso para o MongoDB

user = environ.get('user')
pwd = environ.get('pwd')

uri = f"mongodb+srv://{user}:{pwd}@cluster0.9zxietc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    db = client['Projeto_Integrador']
    collection = db['respostas']
    respostas = answers()
    for key, resposta in respostas.items():
        data = {}
        data['user_id'] = key
        data['user_resposta'] = resposta
        collection.insert_one(data)
except Exception as e:
    print(e)
