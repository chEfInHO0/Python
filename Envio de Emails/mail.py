import ssl
import smtplib
import mimetypes
from email.message import EmailMessage
import os

teste = False

email_senha = open('./config/pwd.txt','r',encoding='utf-8').read() #Recomendação de usar o metodo de leitura de arquivos para pegar a senha ao invés de colocar ela no script em texto pleno
email_login = open('./config/email.txt','r',encoding='utf-8').read()
email_destinos = open('./config/dest.txt','r',encoding='utf-8').read().split(';') # Lista de destinatários, pode ser uma tupla também
assunto = 'Teste'
email_corpo = open('./config/body.txt','r',encoding='utf-8').read() #Mesma recomendação que o campo de senha
smtp_email = 'smtp.gmail.com' # email para o servidor smtp
porta = 465 # Porta que o servidor smtp usa
att_path = './anexos/dog.png' # Caminho do anexo
mimetype,mime_subtype = mimetypes.guess_type(att_path)[0].split('/')
print(mimetype, mime_subtype)
msg = EmailMessage() 

msg['From'] = email_login
msg['To'] = email_destinos
msg['Subject'] = assunto
msg.set_content(email_corpo) # , subtype='html' usar para formatar em html o conteudo dentro do corpo do body
_ssl = ssl.create_default_context()

with open(att_path, 'rb') as att:
    msg.add_attachment(att.read(), maintype=mimetype, subtype=mime_subtype, filename=att_path)
    att.close()

if not teste:
    with smtplib.SMTP_SSL(f'{smtp_email}', porta, context=_ssl) as smtp:
        smtp.login(email_login, email_senha)
        smtp.sendmail(email_login,email_destinos,msg.as_string())
        smtp.close()
else:
    print('Teste concluido')