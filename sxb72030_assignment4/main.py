import boto3
import json

# Step 1: get topic name from Secret Manager
secrets_manager = boto3.client('secretsmanager')
secret_name = 'my-topic-secret-name'
response = secrets_manager.get_secret_value(SecretId=secret_name)
secret_dict = json.loads(response['SecretString'])
topic_name = secret_dict['my-topic-secret-name']

# Step 2: read email address from JSON config file
with open('config.json', 'r') as f:
    config = json.load(f)
email_address = config['email_address']

# Step 3: create SNS client
sns = boto3.client('sns')

# Step 4: create SNS topic
response = sns.create_topic(Name=topic_name)
topic_arn = response['TopicArn']

# Step 5: subscribe email address to SNS topic
response = sns.subscribe(TopicArn=topic_arn, Protocol='email', Endpoint=email_address)
subscription_arn = response['SubscriptionArn']

