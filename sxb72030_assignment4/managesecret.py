import boto3
import json
client = boto3.client('secretsmanager')



def createSecret():

    response = client.create_secret(
        Name='my-topic-secret-name',
        SecretString='{"username": "admin", "password": "Sreenu@123"}'
    )

    return response

def listSecrets():
    response = client.list_secrets()
    return response['SecretList']

def fetchSecret():
    response = client.get_secret_value(
    SecretId='my-topic-secret-name'
    )
    database_secrets = json.loads(response['SecretString'])
    return database_secrets['password']

def deleteSecret():
    response = client.delete_secret(
    SecretId='my-topic-secret-name',
    RecoveryWindowInDays=10,
    ForceDeleteWithoutRecovery=False
    )
    return response

createresp = createSecret()
print(createresp)

listresp = listSecrets()
print(listresp)

#deleteresp =deleteSecret()
#print(deleteresp)
