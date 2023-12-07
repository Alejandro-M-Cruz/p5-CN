import os

import boto3


def lambda_handler(event, context):
    print("Function B is running...")
    sqs = boto3.client("sqs")
    queue_url = os.environ["QUEUE_URL"]
    message = sqs.receive_message(QueueUrl=queue_url)["Messages"][0]["Body"] + "Hello from function B. "
    sqs.send_message(QueueUrl=queue_url, MessageBody=message)
    return {
        "message": message
    }
