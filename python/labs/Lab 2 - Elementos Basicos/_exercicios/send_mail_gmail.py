"""
SÉRIE DE EXERCÍCIOS 2 

Investigue o módulo smtplib e depois utilize-o para desenvolver um 
programa para enviar um email. O email deve ser apenas composto por 
texto, não sendo necessário suportar outro tipo de conteúdos (eg, HTML,
imagens, etc.) ou anexos. Recorra a um servidor de SMTP. Pode, 
por exemplo, utilizar o seu fornecedor de email, desde que este 
suporte SMTP. O programa deve solicitar interactivamente a 
introdução do endereço de email do emissor e do destinatário. 
Depois lê o conteúdo de email até o utilizador terminar com uma 
linha contendo apenas os caracteres #$% , após o que envia o email.
"""

import re
import smtplib


END = "#$%"
EMAIL_RE = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'  # com case insensitive
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SOURCE_ADDR = 'teste23189@gmail.com'
PWD = 'Pzbm23$ab'

##
## Leitura e validação do email do destinatário

while True:
    dest_addr = input("Email do destinatário: ")
    if re.search(EMAIL_RE, dest_addr, re.IGNORECASE):
        subject = input("Assunto: ")
        break
    else:
        print("Email inválido!")

##
## Lê conteúdo do email

email = ["Subject: " + subject]
email_line = input()
while email_line != END:
    email.append(email_line)
    email_line = input()

##
## Abre ligação e envia email

print("A enviar email para", dest_addr, "...")
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(SOURCE_ADDR, PWD)
    server.sendmail(SOURCE_ADDR, dest_addr, '\n'.join(email))
print("...")
print("Email enviado com sucesso!")


# Alternativas para a leitura de linhas de texto
# 
# Alternativa 1:
# 
# email = ["Subject: " + subject]
# while True:
#     linha = input()
#     if linha == END:
#         break
#     email.append(linha)

# Alternativa 2 (a melhor):
# 
# email = ["Subject: " + subject]
# for linha in iter(input, END):
#     email.append(linha)







