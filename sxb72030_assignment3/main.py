import boto3
sqs=boto3.resource('sqs')
queue=sqs.create_queue(
 QueueName='my_queue'
 
 )
print("Created queue '%s' with URL=%s",'my_queue',queue.url)

import config

def send_message(queue_url):
    sqs_client = boto3.client("sqs")

    message = {"key": "value"}
    response = sqs_client.send_message(
        QueueUrl=f"https://us-east-1.console.aws.amazon.com/sqs/v2/home?region=us-east-1#/queues/https%3A%2F%2Fsqs.us-east-1.amazonaws.com%2F017373123744%2Fnewqueue/send-receive,/{config.QUEUE_NAME}",
        MessageBody=json.dumps(message)
    )
    print(response)

    send_message("new message")