import json
from simple_salesforce import Salesforce
from salesforce import fazer_login


def lambda_handler(event, context):
    # TODO implement
    
    usuario_salesforce = "trail.jeessiica.clemente@gmail.com"
    senha_salesforce = "mule@2023"
    token_seguranca = "cdjhHTWxV3TQSJcgErO4fmjW"

    salesforce = fazer_login(usuario_salesforce, senha_salesforce, token_seguranca)
    
    novo_account = {
        'Name': 'Nome da Nova Conta',
        'Industry': 'Tecnologia',  # Substitua com a indústria desejada
        'Type': 'Cliente Potencial'  # Substitua com o tipo desejado
    }

    # Método create() para adicionar o novo registro
    resultado_create = salesforce.Account.create(novo_account)

    # Imprimir o ID do novo registro criado
    print(f"Novo Account criado com ID: {resultado_create['id']}")
    
    query_result = salesforce.query("SELECT Id, Name FROM Account LIMIT 5")
    
    for record in query_result['records']:
        print(f"Account ID: {record['Id']}, Name: {record['Name']}")
    
    
    
    
    
# lambda_handler(None, None)