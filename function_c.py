import os
from time import sleep

import boto3


def lambda_handler(event, context):
    print("Function C is running...")
    sleep(5)
    sqs = boto3.client("sqs")
    queue_url = os.environ["QUEUE_URL"]
    message = sqs.receive_message(queue_url) + "Hello from function C."
    sqs.send_message(QueueUrl=queue_url, MessageBody=message)
    return {
        "message": message
    }
