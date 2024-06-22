import boto3
from botocore.config import Config

def cognito_remove_user(cpf: str):
    config = Config(retries={'max_attempts': 2})
    client = boto3.client('cognito-idp', config=config)
    try:
        response = client.admin_delete_user(
            UserPoolId='us-east-1_EHvshsyoV',
            Username=cpf
        )
    except Exception as e:
        print(e)
        raise Exception('Não foi possivel remover o usuario solicitado, verifique se os dados estão corretos.')