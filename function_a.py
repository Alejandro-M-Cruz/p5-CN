import os
from time import sleep

import boto3


def lambda_handler(event, context):
    print("Function A is running...")
    sleep(5)
    sqs = boto3.client("sqs")
    message = "Hello from function A. "
    sqs.send_message(QueueUrl=os.environ["QUEUE_URL"], MessageBody=message)
    return {
        "message": message
    }
