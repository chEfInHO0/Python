from imbox import Imbox
from datetime import datetime
from os import listdir, mkdir
user = open('./config/email.txt','r').read()
pwd = open('./config/pwd.txt','r').read()
host = 'imap.gmail.com'

mail = Imbox(host,username=user, password=pwd, ssl=True)
messages = mail.messages()


for uid,message in messages:
    if len(message.attachments)>0:
        print(f'''
            Assunto : {message.subject}\n
            Corpo do Email : {message.body}\n
            Remetente : {message.sent_from}\n
            Destinatario : {message.sent_to}\n
            Cc: {message.cc}\n
            Cabecalho : {message.headers}\n
            Data : {message.date}\n
            Anexos : {message.attachments}
        ''')
        # Salvar o anexo no computador
        for f in message.attachments:
            cwd = listdir() # lista todos os itens presentes na pasta
            if 'anexosGmail' not in cwd: # se a pasta nao existir,ela e criada 
                mkdir('anexosGmail')
            with open(f"./anexosGmail/{f['filename']}", 'wb') as file:
                    file.write(f["content"].read())
                    file.close()
        # Este e um teste para salvar os arquivos em uma pasta 
        # Agora temos que realizar o metodo para o salvamento em cada pasta referente a um remetente/assuto/algo do genero
        break