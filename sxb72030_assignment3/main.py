import boto3
from config import QUEUE_NAME

def send_message_to_queue(message_body):
    """
    Sends a message to the specified SQS queue.
    """
    # Create an SQS client
    sqs = boto3.client('sqs')
    
    # Get the URL of the queue
    queue_url = sqs.get_queue_url(QueueName=QUEUE_NAME)['https://us-east-1.console.aws.amazon.com/sqs/v2/home?region=us-east-1#/queues/https%3A%2F%2Fsqs.us-east-1.amazonaws.com%2F017373123744%2Fnewqueue']
    
    # Send the message to the queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )