import boto3
import json
region_name = "us-east-1"

client = boto3.client('secretsmanager')



def createSecret():

    response = client.create_secret(
        Name='DatabaseProdSecrets',
        SecretString='{"username": "admin", "password": "Sreenu@123"}'
    )

    return response

def listSecrets():
    response = client.list_secrets()
    return response['SecretList']

def fetchSecret():
    response = client.get_secret_value(
    SecretId='DatabaseProdSecrets'
    )
    database_secrets = json.loads(response['SecretString'])
    return database_secrets['password']

def deleteSecret():
    response = client.delete_secret(
    SecretId='DatabaseProdSecrets',
    RecoveryWindowInDays=10,
    ForceDeleteWithoutRecovery=False
    )
    return response

#createresp = createSecret()
#print(createresp)

listresp = listSecrets()
print(listresp)

#deleteresp =deleteSecret()
#print(deleteresp)

