from simple_salesforce import Salesforce
import json

def fazer_login(usuario, senha, security_token, sandbox=False):
    """
    Faz login no Salesforce e retorna uma instância do objeto Salesforce.

    :param usuario: Nome de usuário do Salesforce.
    :param senha: Senha do Salesforce.
    :param security_token: Token de segurança do Salesforce.
    :param sandbox: Indica se você está se conectando a um ambiente de sandbox. Padrão é False.
    :return: Objeto Salesforce.
    """
    # Criar uma instância do objeto Salesforce
    sf = Salesforce(username=usuario, password=senha, security_token=security_token)

    # Retornar a instância do Salesforce
    return sf





# Agora, você pode usar 'salesforce' para interagir com o Salesforce.


