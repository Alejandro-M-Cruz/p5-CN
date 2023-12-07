import os

import boto3


def lambda_handler(event, context):
    print("Function A is running...")
    sqs = boto3.client("sqs")
    message = "Hello from function A. "
    sqs.send_message(QueueUrl=os.environ["QUEUE_URL"], MessageBody=message)
    return {
        "message": message
    }
